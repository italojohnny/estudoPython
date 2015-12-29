#!/usr/bin/python3
import datetime
var1 = u'\u26AB'
var0 = u'\u26AA'

now = datetime.datetime.now()

hora = str('{0:06d}'.format(int(str(bin(now.hour))[2:])))
minuto = str('{0:06d}'.format(int(str(bin(now.minute))[2:])))

fhora = [var1 if c == '1' else var0 for c in hora]
fminuto = [var1 if c == '1' else var0 for c in minuto]

print("".join(fhora))
print("".join(fminuto))
