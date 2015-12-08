#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

north = '^'
south = 'v'
east = '>'
west = '<'

def presents_per_house(directions):
	matrix = {}
	y = 0
	x = 0
	houses_with_presents = 1
	matrix[x, y] = 1


	for c in directions:
		if c == north:
			y += 1
		elif c == south:
			y -= 1
		elif c == east:
			x += 1
		elif c == west:
			x -= 1

		if not matrix.has_key((x, y)):
			matrix[x, y] = 1
			houses_with_presents += 1
	#	else:
	#		matrix[x,y] += 1

	return houses_with_presents

def presents_per_house_robo_santa(directions):
	matrix = {}
	robo_santa = False
	y_santa = 0
	x_santa = 0
	x_robo_santa = 0
	y_robo_santa = 0
	houses_with_presents = 1
	matrix[0,0] = 1

	for c in directions:
		if robo_santa:
			if c == north:
				y_robo_santa += 1
			elif c == south:
				y_robo_santa -= 1
			elif c == east:
				x_robo_santa += 1
			elif c == west:
				x_robo_santa -= 1

			if not matrix.has_key((x_robo_santa, y_robo_santa)):
				matrix[x_robo_santa, y_robo_santa] = 1
				houses_with_presents += 1
		else:
			if c == north:
				y_santa += 1
			elif c == south:
				y_santa -= 1
			elif c == east:
				x_santa += 1
			elif c == west:
				x_santa -= 1

			if not matrix.has_key((x_santa, y_santa)):
				matrix[x_santa, y_santa] = 1
				houses_with_presents += 1

		robo_santa = not robo_santa

	return houses_with_presents

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as file:
		input_string = file.read()

		print "Puzzle 1: ", presents_per_house(input_string)
		print "Puzzle 2: ", presents_per_house_robo_santa(input_string)