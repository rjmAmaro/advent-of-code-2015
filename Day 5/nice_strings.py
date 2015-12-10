#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

def count_nice_strings(strings):
	pattern1 = re.compile(".*[aeiou].*[aeiou].*[aeiou].*")
	pattern2 = re.compile(".*((ab)|(cd)|(pq)|(xy)).*")
	pattern3 = re.compile(".*((aa)|(bb)|(cc)|(dd)|(ee)|(ff)|(gg)|(hh)|(ii)|(jj)|(kk)|(ll)|(mm)|(nn)|(oo)|(pp)|(qq)|(rr)|(ss)|(tt)|(uu)|(vv)|(ww)|(xx)|(yy)|(zz)).*")
	i = 0

	for c in strings:
		if pattern1.match(c) and not pattern2.match(c) and pattern3.match(c):
			i += 1

	return i

def real_nice_strings(strings):
	i = 0

	for c in strings:
		if check1(c) and check2(c):
			i += 1
#			print c

	return i


def check1(s):
	i_base = 0
	i_compare = 2

	for i_base in range(0, len(s)-2):
		temp_string = s[i_base:i_base+2]
#		print "Temp string: ", temp_string

		for i_compare in range(i_base+2, len(s)-2):
			temp_string_2 = s[i_compare:i_compare+2]
#			print "\tTemp string 2: ", temp_string_2
			if temp_string == temp_string_2:
#				print "\t\tT"
				return True

def check2(s):
	for i in range(0, len(s)-3):
		if s[i] == s[i+2]:
			return True

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as file:
		strings = []

		for line in file:
			strings.append(line)

		print "Puzzle 1: ", count_nice_strings(strings)
		print "Puzzle 2: ", real_nice_strings(strings)