import sys

try:
    while not sys.stdin.closed:
        print "%s" % [hex(ord(i)) for i in sys.stdin.readline()]
        #sys.stdout.flush()
except KeyboardInterrupt:
    pass
