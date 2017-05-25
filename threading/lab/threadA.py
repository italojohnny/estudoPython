#!/usr/bin/python2.7
# coding: utf-8
import threading
import time, os, sys

from threadB import ThreadB
from threadC import ThreadC

class ThreadA (threading.Thread):
    def __init__ (self, name):
        super(ThreadA, self).__init__()
        self._stop = threading.Event()
        self.name = name

    def run (self):
        time.sleep(1)
        while not self.stopped():
            try:
                b = ThreadB("nameB")
                c = ThreadC("nameC")
                d = threading.Thread(target=self.nothing, args=[], name="nameD")
                e = threading.Timer(5, self.nothing)

                sys.stderr.close()
                b.start()
                c.start()
                #d.start()
                #e.start()
                #threads_names = [x.name for x in threading.enumerate()]
                #print "\n(%s)\n%s\n" % (len(threads_names), threads_names)
                print "preparacao"
                b.join(1)
                c.join(1)
                print "feito"

            except Exception as e:
                print "error: %s" % e

    def stopped (self):
        return self._stop.isSet()


    def nothing (self):
        while True:
            time.sleep(1)
