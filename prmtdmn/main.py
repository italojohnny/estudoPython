#!/usr/bin/python2.7
#import psycopg2 # sudo apt-get install python-psycopg2
import os
import commands
import re

class Camera:# {{{
    def __init__ (self, name, source, destiny):
        self.width  = 500
        self.height = 400
        self.extensions = "\( -name '*.jpg' -or -name '*.png' \)" # TODO automatizar criacao desta string
        self.name = name
        self.folder_source = source
        self.folder_destiny = destiny

    def make_subfolders (self):
        subfolders_source = self.get_subfolders(self.folder_source)
        subfolders_destiny = self.get_subfolders(self.folder_destiny)
        subfolders_diff = self.diff_list(subfolders_source, subfolders_destiny)
        if subfolders_diff:
            for i in subfolders_diff:
                directory = "%s%s" % ((self.folder_destiny if not self.folder_destiny[-1] == '/' else self.folder_destiny[:-1]), i)
                if not os.path.exists(directory):
                    os.makedirs(directory)

    def make_files (self):
        files_source = self.get_files(self.folder_source)
        files_destiny = self.get_files(self.folder_destiny)

        for i in files_source:
            print re.sub(r'(\ )', r'\\\1', i) #XXX parei aqui

    def diff_list (self, list1, list2):
        return list(set(list1) - set(list2))

    def get_subfolders (self, folder):
        output = commands.getstatusoutput("find %s -type d" % folder)
        if output[0] == 0:
            return sorted(filter(None, output[1].replace(folder, '').split('\n')))
        return list()

    def get_files (self, folder):
        output = commands.getstatusoutput("find %s -type f %s" % (folder, self.extensions))
        if output[0] == 0:
            return sorted(filter(None, output[1].split('\n')))
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

if __name__ == "__main__":
    #cameras = DataBase.get_cameras()
    #cameras = [Camera("camera1", "/home/zak/Downloads/others/trash", "/tmp")]
    cameras = [Camera("camera1", "/home/zak/Downloads/others/trash", "/home/zak/tmp")]
    if not cameras: exit(0)
    # cada item da lista sera manipulado por uma thread

    cameras[0].make_subfolders()
    cameras[0].make_files()


    
