from serial import Serial

def read_serial (s):
    return s.readline()

def write_serial (s, txt):
    s.write(txt)

s = Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=0.1)


write_serial(s, "$2,dev,dev;")
while True:
    write_serial(s, "$5;$0;$3,%s,%s,%s %s,obd,trava,feedback,%s,%s,%s;")
    print read_serial(s)

