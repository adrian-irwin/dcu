#!/usr/bin/env python3

from student_v2_121 import Student

def main():

    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)
    print(s1.get_mark('CA103'))

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)
    print(s2.get_mark('CA117'))

if __name__ == '__main__':
    main()