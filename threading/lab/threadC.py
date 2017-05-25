#!/usr/bin/python2.7
# coding: utf-8
import threading
import time, os, sys

class ThreadC (threading.Thread):
    def __init__ (self, name):
        super(ThreadC, self).__init__()
        self._stop = threading.Event()
        self.name = name

    def run (self):
        while not self.stopped():
            time.sleep(1)

    def stopped (self):
        return self._stop.isSet()
