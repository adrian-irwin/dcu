#!/usr/bin/env python3

from student_v1_121 import Student

def main():
    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)

    assert(s1.name == 'Boris Spassky')
    assert(s1.address == 'Dublin')
    assert(s1.sid == 17345654)

    print(s1)
    print(s2)

if __name__ == '__main__':
    main()