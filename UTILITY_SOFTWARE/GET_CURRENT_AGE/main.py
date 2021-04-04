# How old am I?

#!/usr/bin/env python3

import os
import time

def clear():
	os.system('clear')


def sleeper():
	time.sleep(4)


clear()
# Getting the current time and date of birth
whole_time = time.gmtime()

current_year = whole_time[0]
current_month = whole_time[1]

year_of_birth = int(input('Enter date of birth: '))
month_of_birth = int(input('Enter month of birth: '))
clear()

my_current_age = current_year - year_of_birth


if month_of_birth > current_month:
	my_current_age -= 1
	print(f'You are {my_current_age} years old.')
	sleeper()
	clear()
else:
	print(f'You are {my_current_age} years old.')
	sleeper()
	clear()
