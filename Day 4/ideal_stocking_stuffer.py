#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import hashlib

def mining(input_string):
	m = hashlib.md5()
	i=1

	while True:
		test_string = input_string + str(i)
		m = hashlib.md5(test_string).hexdigest()
		#print m
		if m.startswith('000000'):
			print m
			break
		i += 1

	return i

if __name__ == "__main__":
	input_string = sys.argv[1]

	print "Puzzle 1: ", mining(input_string)