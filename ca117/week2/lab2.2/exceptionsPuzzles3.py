#!/usr/bin/env python3

def callme(x):
    try:
        y = 1//x
        return y
    except ZeroDivisionError:
        print('In exception handler')
    else:
        print('Reached end of try')
    finally:
        print('Exiting the function')

def main():
    print(callme(1))
    print(callme(0))

if __name__ == '__main__':
    main()