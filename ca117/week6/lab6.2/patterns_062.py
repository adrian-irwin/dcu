#!/usr/bin/env python3

import sys
from re import findall

date = r"(?:\d{1,2}[/-]){2}\d{1,2}"

phone = r"\b\d{2}[\s-]\d{7}\b"

email = r"(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*"

ldate = r"\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2}"

def main():
   lines = sys.stdin.read()
   print(findall(date, lines))
   print(findall(phone, lines))
   print(findall(email, lines))
   print(findall(ldate, lines))

if __name__ == '__main__':
   main()
