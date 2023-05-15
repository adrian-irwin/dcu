#!/usr/bin/env python3

from classlist_v1_121 import Student, Classlist

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)

    cl.add(s1)
    cl.add(s2)

    s = cl.lookup(17345654)
    assert(isinstance(s, Student))
    assert(s.name == 'Boris Spassky')
    assert(s.address == 'Dublin')
    assert(s.sid == 17345654)

    cl.remove(17345654)
    s = cl.lookup(17345654)
    assert(s is None)

if __name__ == '__main__':
    main()