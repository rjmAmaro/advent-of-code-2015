#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# values: l, w, h

l=0
w=1
h=2

def calc_wrapping_paper(values):
	total = 0

	for i in range(0, len(values)):
		surface1 = values[i][l]*values[i][w]
		surface2 = values[i][w]*values[i][h]
		surface3 = values[i][h]*values[i][l]
		extra = min(surface1, surface2, surface3)
		subtotal = 2*(surface1 + surface2 + surface3) + extra
		total += subtotal

	return total

def calc_ribbon(values):
	total = 0

	for i in range(0, len(values)):
		p1 = values[i][l]+values[i][w]
		p2 = values[i][l]+values[i][h]
		p3 = values[i][w]+values[i][h]

		p = min(p1, p2, p3) * 2

		extra = values[i][l]*values[i][w]*values[i][h]

		total += p + extra

	return total

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as file:
		values = []
		for line in file:
			s = line.split('x')
			values.append(tuple([int(s[0]), int(s[1]), int(s[2])]))

		print "Puzzle 1: ", calc_wrapping_paper(values)
		print "Puzzle 2: ", calc_ribbon(values)