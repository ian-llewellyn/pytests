from time import sleep
from sys import exit, stdout, stderr

def do_main():
    for i in range(5):
        stdout.write('.')
        stdout.flush()
        stderr.write('_')
        sleep(3 / (i + 1))
    raise Exception

try:
    do_main()
except KeyboardInterrupt as e:
    print '=-> Exiting!'
except Exception:
    print '=-> Exception'
