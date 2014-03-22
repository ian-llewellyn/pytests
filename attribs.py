import sys

class TestClass():
    def __init__(self, **kwargs):
        self.sys = 'abc'
        self.argv = 'def'
        for key in kwargs.keys():
            # FIXME: filter for acceptable keys
            setattr(self, key, kwargs[key])

    def get_attr(self, attr):
        return getattr(self, attr, None)

tc = TestClass(ian='is cool', yes='he is')

print dir(tc)
print tc.get_attr('ian')
print tc.get_attr('pop')
