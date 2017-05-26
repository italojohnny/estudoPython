#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
# sudo apt-get install imagemagick
#import psycopg2 # sudo apt-get install python-psycopg2
import os
import sys
import commands
import re
import time
import pdb

def general_log (message):
    log = "[datahora] %s" % message
    print log # TODO redirecionar para arquivo

class Camera:# {{{
    def __init__ (self, name, source, destiny):
        self.width  = 800
        self.height = 600
        self.extensions = "\( -name '*.jpg' -or -name '*.png' \)" # TODO automatizar criacao desta string
        self.name = name
        self.folder_source = source
        self.folder_destiny = destiny

    def log (self, message):
        txt = "[Camera: %s] %s" % (self.name, message)
        general_log(txt)

    def make_subfolders (self):# {{{
        try:
            subfolders_source = self.get_subfolders(self.folder_source)
            if subfolders_source:
                subfolders_destiny = self.get_subfolders(self.folder_destiny)

                subfolders_diff = self.diff_list(subfolders_source, subfolders_destiny)
                if subfolders_diff:
                    for i in subfolders_diff:
                        directory = "%s%s" % ((self.folder_destiny if not self.folder_destiny[-1] == '/' else self.folder_destiny[:-1]), i)
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                            self.log("diretorio criado: %s" % directory)
                    return True

                else:
                    self.log("diretorio de origem e destino possuem mesma estrutura de pastas")
                    return True
            else:
                self.log("ERRO: diretorio de origiem nao encontrado")
                return False

        except Exception as e:
            self.log("ERRO CRITICO: falha ao replicar estutura de pastas: %s" % e)
            return False# }}}

    def make_files (self):
        files_source = self.get_files(self.folder_source)
        name_files_source = [i.replace(self.folder_source, '') for i in files_source]

        files_destiny = self.get_files(self.folder_destiny)
        name_files_destiny = [i.replace(self.folder_destiny, '') for i in files_destiny]

        name_files_diff = self.diff_list(name_files_source, name_files_destiny)
        final = [{'o': "%s%s"%(self.folder_source, i), 'd': "%s%s"%(self.folder_destiny, i)} for i in name_files_diff]

        cmd = ["convert -resize '%sx%s' %s %s" % (self.width, self.height, i['o'], i['d']) for i in final]
        for i in cmd:
            try:
                result, output = commands.getstatusoutput(i)
                if result == 0:
                    print 'sucesso'
                else:
                    print output
            except Exception as e:
                print e

#        for i in files_source:
#            print re.sub(r'(\ )', r'\\\1', i).replace(self.folder_source, '') #XXX parei aqui
#
#        for i in files_destiny:
#            print re.sub(r'(\ )', r'\\\1', i).replace(self.folder_source, '') #XXX parei aqui

    def diff_list (self, list1, list2):
        return list(set(list1) - set(list2))

    def get_subfolders (self, folder):
        output = commands.getstatusoutput("find %s -type d" % folder)
        if output[0] == 0:
            return sorted(filter(None, output[1].replace(folder, '').split('\n')))

        self.log("ERRO: pasta nao encontrada: %s" % folder)
        return list()

    def get_files (self, folder):
        output = commands.getstatusoutput("find %s -type f %s" % (folder, self.extensions))
        if output[0] == 0:
            return sorted(filter(None, output[1].split('\n')))

        self.log("ERRO: pasta nao encontrada: %s" % folder)
        return list()
# }}}

class DataBase:# {{{
    def __init__ (self):
        self.db_host = "127.0.0.1"
        self.db_port = "5432"
        self.db_name = ""
        self.db_user = ""
        self.db_pswd = ""
        self.connect = self.connect()

    def __del__ (self):
        if self.connect:
            sefl.connect.close()

    def log (self, message):
        txt = "[DataBase] %s" % message
        general_log(txt)

    def connect (self):
        try:
            return psycopg2.connect(
                host     = self.db_host,
                port     = self.db_port,
                dbname   = self.db_name,
                user     = self.db_user,
                password = self.db_pswd,
            )
        except:
            return False

    def get_cameras (self):
        try:
            cursor = self.connect.cursor()
            cursor.execute("SELECT name, original_folder, preview_folder FROM cameras;")
            return [Camera(i[0], i[1], i[2]) for i in cursor.fetchall()]

        except:
            return list()
# }}}

def child (camera):
    # aprimorar isso
    #cameras[0].make_subfolders()
    #cameras[0].make_files()
    while True:
        print camera.name
        time.sleep(1)

if __name__ == "__main__":
    #cameras = DataBase.get_cameras()
    cameras = [
            Camera("camera1", "/home/zak/Downloads/others/trash", "/home/zak/tmp"),
            Camera("camera2", "/home/zak/Downloads/others/trash", "/home/zak/tmp"),
            Camera("camera3", "/home/zak/Downloads/others/trash", "/home/zak/tmp"),
            Camera("camera4", "/home/zak/Downloads/others/trash", "/home/zak/tmp"),
            ]
    # cada item da lista sera manipulado por uma thread
    identification = None
    for i in range(0, len(cameras)):
        newprocess = os.fork()
        if newprocess:
            continue
        else:
            identification = i
            break

    if identification != None:
        #sys.stdout.flush()
        #sys.stderr.flush()
        #sys.stdout = open('/dev/null', 'w')
        #sys.stderr = open('/dev/null', 'w')

        child(cameras[identification])

            
