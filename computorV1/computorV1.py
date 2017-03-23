#!/usr/bin/python
import math
import re
import sys

if len(sys.argv) > 2:
	print("Too many arguments Bro")
elif len(sys.argv) == 1:
	print("Usage: ./computor \"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\"")
else:
	print("Welcome to computorV1")
	split = re.split("=" ,sys.argv[1])
	print(split)
	if (len(split) != 2):
		print("Bad boy, missing equality")
	else:
		a = []
		for i in range(len(split)):
			a.append([x.strip() for x in re.split('(\+|\-)+', split[i])])
		print(a)
		