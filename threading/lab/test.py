import time, sys


sys.stderr = open("/tmp/log.txt", 'w')
while True:
    print >> sys.stderr, time.strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(1)
