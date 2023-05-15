#!/usr/bin/env python3

from patient_v3_142 import Patient

def main():
    p1 = Patient('Mary', 34, 'James Kildare', ['aspirin'])
    p2 = Patient('Wendy', 40, 'Gregory House')

    p2.add_medication('penicillin')
    p2.add_medication('nexium')

    print(p1)
    print(p2)

if __name__ == '__main__':
    main()