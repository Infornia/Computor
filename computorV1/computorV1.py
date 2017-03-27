#!/usr/bin/python
from re import compile
import re
import sys

re_space = compile('\s+')
re_pol = compile('([-+=]?)\s*([0-9\.]+)?(\s*\*?\s*[xX](?:\s*\^\s*([0-9]+))?)?\s*')
re_comp2 = compile('([+-]?[0-9\.]+)\s*([*])\s*(X\^\d)\s*')

class Polynom():
	
	sign = None
	n = 0.0
	x = False
	pow = 0
	
	def __init__(self, m, sign = None, n = 0.0, x = False, pow = 0):
		self.sign = sign
		self.n = n
		self.x = x 
		self.pow = pow
		if m != None:
			if len(m.group(1)) > 0:
				self.sign = m.group(1)
			if m.group(2) == None:
				self.n = 1.0
			else:
				self.n = float(m.group(2))
			if m.group(3) != None:
				self.x = True
				if m.group(4) != None:
					self.pow = int(m.group(4))
				else:
					self.pow = 1
		if self.n < 0.0:
			self.sign = ["+","-"][self.sign == "-"]
			self.n = -self.n
		if self.pow == 0 and self.x:
			self.x = False

class Computor():
	def __init__(self):
		self.left = []
		self.right = []
		
	def parsing(self, eq):
		i = 0
		while i < len(eq):
			m = re_space.match(eq, i)
			if m != None:
				i += len(m.group(0))
				continue
			m = re_pol.match(eq, i)
			print(m.group())
			if m == None or len(m.group(0)) <= 0:
				print("\033[31m Strange Syntax Bro 1: '%s' \033[39m" % (eq[i:i+5]))
				return False
			try:
				p = Polynom(m)
			except:
				print("\033[31m Strange Syntax Bro 2: '%s' \033[39m" % (eq[i:i+5]))
				return False
				
				
			i +=1

if len(sys.argv) > 2:
	print("Too many arguments Bro")
elif len(sys.argv) == 1:
	print("Usage: ./computor \"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\"")
else:
	print("Welcome to computorV1")
	split = re.split("(=?)" ,sys.argv[1])
	if (len(split) != 3):
		print("Bad Syntax")
	else:
		c = Computor(split[0], split[2])
		c.parsing(split[0])
		print(vars(c))
