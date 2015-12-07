#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def search_destination_floor(input_string):
	go_up = '('
	go_down = ')'
	dest_floor = input_string.count(go_up) - input_string.count(go_down)
	return dest_floor

def search_basement_moment(input_string):
	go_up = '('
	go_down = ')'
	floor = 0
	
	for i in range(0, len(input_string)):
		if input_string[i] == go_up:
			floor += 1
		else:
			floor -= 1

		if floor == -1:
			return i+1

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as file:
		input_string = file.read()
		print "Puzzle 1: ", search_destination_floor(input_string)
		print "Puzzle 2: ", search_basement_moment(input_string)