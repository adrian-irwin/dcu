#!/usr/bin/env python3

month = int(input()) - 1
dayOfMonth = int(input()) - 1

dayOfYear = ((month) * 30) + dayOfMonth
weekDay = (dayOfYear % 7) + 1

print(weekDay)
