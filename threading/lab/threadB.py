#!/usr/bin/python2.7
# coding: utf-8
import threading
import time, os, sys

from threadC import ThreadC

class ThreadB (threading.Thread):
    def __init__ (self, name):
        super(ThreadB, self).__init__()
        self._stop = threading.Event()
        self.name = name

    def run (self):
        while not self.stopped():
            bc = ThreadC("nameBC")
            bc.start()
            time.sleep(1)

    def stopped (self):
        return self._stop.isSet()
