#def gettime_ntp(addr='time.nist.gov'):
def gettime_ntp(addr='asdfasdfasd.gov'):
    # http://code.activestate.com/recipes/117211-simple-very-sntp-client/
    import socket
    import struct
    import sys
    import time
    TIME1970 = 2208988800L      # Thanks to F.Lundh
    client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    client.settimeout(10)
    data = '\x1b' + 47 * '\0'
    client.sendto( data, (addr, 123))
    data, address = client.recvfrom( 1024 )
    if data:
        t = struct.unpack( '!12I', data )[10]
        t -= TIME1970
        return time.ctime(t),t


print gettime_ntp()[0]
print gettime_ntp()[1]
