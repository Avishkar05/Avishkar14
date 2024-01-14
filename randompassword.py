# This code generate random password
import random

lower = "abcdefghijklmnopqrestuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRESTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"


all = lower + upper + numbers + symbols
length = 10
password = "".join(random.sample(all,length))

print(password)
