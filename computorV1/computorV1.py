#!/usr/bin/python
from re import compile
import re
import sys

re_space = compile('\s+')
re_comp = compile('([-+=]?)\s*([0-9\.]+)?(\s*\*?\s*[xX](?:\s*\^\s*([0-9]+))?)?\s*')
re_comp2 = compile('\s*([+-]?[0-9\.]+)\s*([*])\s*(X\^\d)\s*')

class Computor():
	def __init__(self):
		self.left = []
		self.right = []
	
	def parsing(self, eq):
		i = 0
		left = True
		while i < len(eq):
			if eq[i:i+1] == "=" and left and len(self.left) > 0:
				left = False
				i += 1
			m = re_space.match(eq, i)
			if m != None:
				i += len(m.group(0))
				continue
			m = re_comp.match(eq, i)
			if m == None or len(m.group(0)) <= 0:
				print("\033[31m Strange Syntax Bro: '%s' \033[39m" % (eq[i:i+5]))
				
			i +=1

if len(sys.argv) > 2:
	print("Too many arguments Bro")
elif len(sys.argv) == 1:
	print("Usage: ./computor \"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\"")
else:
	print("Welcome to computorV1")
	c = Computor()
	split = re.split("(=?)" ,sys.argv[1])
	if (len(split) != 3):
		print("Bad Syntax")
	else:
		c.left = split[0]
		c.right = split[2]
		# c.parsing(sys.argv[1])
		print(vars(c))
		a = []
		for i in range(3):
			a.append(re.split('\s*([+-]?[0-9\.]+)\s*([*])\s*(X\^\d)\s*', split[i]))
			a[i] = a[i][1:-1]
			print(a[i])
		left = a[0]
		right = a[2]
