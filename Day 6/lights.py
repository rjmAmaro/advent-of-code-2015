#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

max_dim = 1000

def lights_on(instructions):
	matrix = [[0 for i in range(max_dim)] for i in range(max_dim)]

	lights_on_counter = 0

	for instruction in instructions:
		instruction_clean = interpreter(instruction)

		if instruction_clean[0] == 1:
			lights_on_counter = turn_lights_on(matrix, lights_on_counter, instruction_clean[1], instruction_clean[2])
		elif instruction_clean[0] == 2:
			lights_on_counter = turn_lights_off(matrix, lights_on_counter, instruction_clean[1], instruction_clean[2])
		elif instruction_clean[0] == 3:
			lights_on_counter = toggle_lights(matrix, lights_on_counter, instruction_clean[1], instruction_clean[2])

	return lights_on_counter

def turn_lights_on(matrix, counter, start, end):
	for x in range(start[0], end[0]+1):
		for y in range(start[1], end[1]+1):
			if matrix[x][y] == 0:
				matrix[x][y] = 1
				counter += 1



	return counter

def turn_lights_off(matrix, counter, start, end):
	for x in range(start[0], end[0]+1):
		for y in range(start[1], end[1]+1):
			if matrix[x][y] == 1:
				matrix[x][y] = 0
				counter -= 1

	return counter

def toggle_lights(matrix, counter, start, end):
	for x in range(start[0], end[0]+1):
		for y in range(start[1], end[1]+1):
			if matrix[x][y] == 1:
				matrix[x][y] = 0
				counter -= 1
			else:
				matrix[x][y] = 1
				counter += 1

	return counter

def calc_bightness(instructions):
	matrix = [[0 for i in range(max_dim)] for i in range(max_dim)]


	brightness_level = 0

	for instruction in instructions:
		instruction_clean = interpreter(instruction)

		p1_x = instruction_clean[1][0]
		p1_y = instruction_clean[1][1]
		p2_x = instruction_clean[2][0]
		p2_y = instruction_clean[2][1]

		if instruction_clean[0] == 1:
			brightness_level = change_bright(matrix, brightness_level, instruction_clean[1], instruction_clean[2], 1)
		elif instruction_clean[0] == 2:
			brightness_level = change_bright(matrix, brightness_level, instruction_clean[1], instruction_clean[2], -1)
		elif instruction_clean[0] == 3:
			brightness_level = change_bright(matrix, brightness_level, instruction_clean[1], instruction_clean[2], 2)

	return brightness_level

def change_bright(matrix, counter, start, end, value):
	for x in range(start[0], end[0]+1):
		for y in range(start[1], end[1]+1):
			matrix[x][y] += value
			if matrix[x][y] >= 0:
				counter += value
			else:
				matrix[x][y] = 0

	return counter

def interpreter(instruction):
	p1_x = 0
	p1_y = 0
	p2_x = 0
	p2_y = 0
	operation = 0

	instruction_split = instruction.split()

	if instruction.startswith('turn on'):
		temp_start = instruction_split[2].split(',')
		p1_x=int(temp_start[0])
		p1_y=int(temp_start[1])
		temp_end = instruction_split[4].split(',')
		p2_x=int(temp_end[0])
		p2_y=int(temp_end[1])
		operation = 1
	elif instruction.startswith('turn off'):
		temp_start = instruction_split[2].split(',')
		p1_x=int(temp_start[0])
		p1_y=int(temp_start[1])
		temp_end = instruction_split[4].split(',')
		p2_x=int(temp_end[0])
		p2_y=int(temp_end[1])
		operation = 2
	elif instruction.startswith('toggle '):
		temp_start = instruction_split[1].split(',')
		p1_x=int(temp_start[0])
		p1_y=int(temp_start[1])
		temp_end = instruction_split[3].split(',')
		p2_x=int(temp_end[0])
		p2_y=int(temp_end[1])
		operation = 3

	return (operation, (p1_x, p1_y), (p2_x, p2_y))

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as file:
		instructions = []

		for line in file:
			instructions.append(line)

		print 'Puzzle 1: ', lights_on(instructions)
		print 'Puzzle 2: ', calc_bightness(instructions)