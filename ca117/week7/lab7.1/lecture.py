#!/usr/bin/env python3

class MyFirstClass(object):
    pass

print("")

c = MyFirstClass()
print(type(c))
print("")

class Time(object):

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_seconds(self):
        return self.hour*60*60 + self.minute*60 + self.second

    def is_later_than(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def plus(self, other):
        return seconds_to_time(self.time_to_seconds() + other.time_to_seconds())

    def __str__(self):
        return 'The time is {:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second) + "\n"

def seconds_to_time(s):
    minute, second = divmod(s, 60)
    hour, minute = divmod(minute, 60)
    overflow, hour = divmod(hour, 24)
    return Time(hour, minute, second)

# a = Time(13, 43, 6)
# a.show_time()

# b = Time(21, 8, 36)
# b.show_time()

# c = Time(3, 4, 7)
# c.show_time()

# a = Time()
# print(a)

# a = Time(16)
# print(a)

# a = Time(16, 30)
# print(a)

# a = Time(16, 30, 59)
# print(a)

# t1 = Time(13, 43, 6)
# t2 = Time(14, 52, 7)
# t3 = Time(14, 43, 7)
# t4 = Time(13, 43, 7)

# print(t2.is_later_than(t1))
# print(t1.is_later_than(t2))
# print(t3.is_later_than(t2))
# print(t4.is_later_than(t1))

t1 = Time(13, 58, 23)
t2 = Time(0, 10, 0)
t3 = t1.plus(t2)
print(t3)
t4 = Time(16, 18, 36)
t5 = Time(12, 10, 19)
t6 = t4.plus(t5)
print(t6)