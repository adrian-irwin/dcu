#!/usr/bin/env python3

threeDigitNumber = int(input())

firstDigit = threeDigitNumber // 100 % 10
secondDigit = (threeDigitNumber % 100 - (threeDigitNumber % 10)) // 10
thirdDigit = threeDigitNumber % 10

print(firstDigit)
print(secondDigit)
print(thirdDigit)
