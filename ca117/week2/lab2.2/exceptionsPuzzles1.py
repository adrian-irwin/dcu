#!/usr/bin/env python3

def callme(x):
    y = None
    try:
        y = 1//x
    except ZeroDivisionError:
        print('In exception handler')
    else:
        print('Reached end of try')
    finally:
        print('Exiting the function')
    return y

def main():
    print(callme(1))
    print(callme(0))

if __name__ == '__main__':
    main()