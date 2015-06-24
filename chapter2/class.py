'''
edit by xy


'''

# -*- coding: utf-8 -*-

class FooClass(object):
    '''my very first calss:FooClass'''
    version = 0.1
    def __init__(self, nm='xy'):
        '''constructor'''
        self.name=nm
        print 'Created a class instance for',nm

    def showname(self):
        '''display'''
        print 'Your name is',self.name
        print 'My name is',self.__class__.__name__

    def showver(self):
        '''display'''
        print self.version

    def addMe2Me(self,x):
        '''apply'''
        return x + x

fool = FooClass()
fool.showname()

fool.showver()

print fool.addMe2Me(5)

print fool.addMe2Me('xyz')

foo2 = FooClass('Jane Smith')

foo2.showname()
