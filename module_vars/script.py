import os

print __name__      # __main__
print '__file__: ' + __file__   # script.py
print 'abspath: ' + os.path.abspath(__file__)   # /.../script.py
print 'dirname: ' + os.path.dirname(__file__)   # ''
print 'abs+dir: ' + os.path.abspath(os.path.dirname(__file__))  # /home/ian/devel

def f():            # SAME AS ABOVE
    print __name__
    print '__file__: ' + __file__
    print 'abspath: ' + os.path.abspath(__file__)
    print 'dirname: ' + os.path.dirname(__file__)
    print 'abs+dir: ' + os.path.abspath(os.path.dirname(__file__))

f()

#import sys
#sys.path.append(os.path.abspath(''))

import iansmod.junkie as module

a = module.MyModule()
