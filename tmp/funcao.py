import sys
import math

x = pow(2, int(sys.argv[1])) + pow(int(sys.argv[1]), 3)
y = pow(int(sys.argv[1]), 3) / pow(2, int(sys.argv[1]))

print('%s' % (str(x)))
print('%s' % (str(y)))
