import os

print __name__      # uniqueue.junkie
print '__file__: ' + __file__   # /.../uniqueue/junkie.pyc
print 'abspath: ' + os.path.abspath(__file__)   # /.../uniqueue/junkie.pyc
print 'dirname: ' + os.path.dirname(__file__)   # /.../uniqueue
print 'abs+dir: ' + os.path.abspath(os.path.dirname(__file__)) # /.../uniqueue

print '# ' + os.path.abspath('')    # /home/ian/devel
print '# ' + os.path.dirname('')    # ''

class MyModule():
    print __name__
    print '__file__: ' + __file__
    print 'abspath: ' + os.path.abspath(__file__)
    print 'dirname: ' + os.path.dirname(__file__)
    print 'abs+dir: ' + os.path.abspath(os.path.dirname(__file__))

    def __init__(self):
        print __name__
        print '__file__: ' + __file__
        print 'abspath: ' + os.path.abspath(__file__)
        print 'dirname: ' + os.path.dirname(__file__)
        print 'abs+dir: ' + os.path.abspath(os.path.dirname(__file__))

        print '# ' + os.path.abspath('')
        print '# ' + os.path.dirname('')
        pass
