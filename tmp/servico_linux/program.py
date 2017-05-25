#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from datetime import datetime
from random import randint
from time import sleep

filename = "/tmp/mylog.dat"
while True:
    value1 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    value2 = "%0.3d" % randint(0,999)
    filelog = None
    try:
        filelog = open(filename, 'a')
        filelog.write("%s -- %s\n" % (value1, value2))

    except:
        filelog = open(filename, 'w')
        filelog.write("%s -- %s\n" % (value1, value2))

    finally:
        if filelog: filelog.close()

    sleep(1)
