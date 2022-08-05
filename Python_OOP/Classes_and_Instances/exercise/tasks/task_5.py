# class Time:
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def set_time(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#         return self.hours, self.minutes, self.seconds
#
#     @staticmethod
#     def time_format(clock_digits):
#         clock_digits = str(clock_digits)
#         if len(clock_digits) < 2:
#             clock_digits = "0" + clock_digits
#         return clock_digits
#
#     def get_time(self):
#         return f"{self.time_format(self.hours)}:{self.time_format(self.minutes)}:{self.time_format(self.seconds)}"
#
#     def next_second(self):
#         if self.seconds == Time.max_seconds:
#             self.seconds = 0
#             self.minutes += 1
#         else:
#             self.seconds += 1
#
#         if self.minutes == Time.max_minutes + 1:
#             self.minutes = 0
#             self.hours += 1
#
#         if self.hours == Time.max_hours + 1:
#             self.hours = 0
#
#         return self.get_time()
#
#
# time = Time(9, 30, 1)
# print(time.next_second())
# print()
# time = Time(10, 00, 59)
# print(time.next_second())
# print()
# time = Time(23, 59, 59)
# print(time.next_second())
# print()
# time = Time(13, 11, 59)
# print(time.next_second())



############ ############ solution with DATETIME
from datetime import datetime, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time_object = datetime(100, 1, 1, hour=hours, minute=minutes, second=seconds)

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    def next_second(self):
        self.time_object += timedelta(seconds=1)
        self.hours = self.time_object.hour
        self.minutes = self.time_object.minute
        self.seconds = self.time_object.second
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
print()
time = Time(10, 00, 59)
print(time.next_second())
print()
time = Time(23, 59, 59)
print(time.next_second())
print()
time = Time(13, 11, 59)
print(time.next_second())
