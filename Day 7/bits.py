#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

calculated = {}
to_calc = {}

ASSIGN_OP = 0
NOT_OP = 1
AND_OP = 2
OR_OP = 3
LSHIFT_OP = 4
RSHIFT_OP = 5

def AND(source1, source2):
	return (source1 & source2) % 65536

def OR(source1, source2):
	return (source1 | source2) % 65536

def NOT(source):
	return (~source) % 65536

def LSHIFT(source, value):
	return (source << value) % 65536

def RSHIFT(source, value):
	return (source >> value) % 65536

def assemble(instructions):

	for inst in instructions:
		interpreter(inst)

	a_value = retrieve_value('a')

	print "1. Value of 'a': ", a_value

	calculated.clear()
	to_calc.clear()

	for inst in instructions:
		interpreter(inst)

	calculated['b'] = a_value

	#to_calc.pop('b')

	print "2. Value of 'a': ", retrieve_value('a')

def retrieve_value(wire):
	#print "Retrieve: ", wire

	try:
		return int(wire)
	except ValueError:
		if not calculated.has_key(wire):
			calc(wire)

		return calculated[wire]

def calc(wire):
	#print "Calc: ", wire

	operation_index = 0
	source_1_index = 1
	source_2_index = 2
	value_index = 3


	operation = to_calc[wire][operation_index]

	if operation == ASSIGN_OP:
		#print "op: ASSIGN ", to_calc[wire][source_1_index]
		calculated[wire] = retrieve_value(to_calc[wire][source_1_index])
	elif operation == NOT_OP:
		#print "op: NOT ", to_calc[wire][source_1_index]
		calculated[wire] = NOT(retrieve_value(to_calc[wire][source_1_index]))
	elif operation == AND_OP:
		#print "op: AND ", to_calc[wire][source_1_index], ", ", to_calc[wire][source_2_index]
		calculated[wire] = AND(retrieve_value(to_calc[wire][source_1_index]), retrieve_value(to_calc[wire][source_2_index]))
	elif operation == OR_OP:
		#print "op: OR ", to_calc[wire][source_1_index], ", ", to_calc[wire][source_2_index]
		calculated[wire] = OR(retrieve_value(to_calc[wire][source_1_index]), retrieve_value(to_calc[wire][source_2_index]))
	elif operation == LSHIFT_OP:
		#print "op: LSHIFT ", to_calc[wire][source_1_index], ", ", to_calc[wire][value_index]
		calculated[wire] = LSHIFT(retrieve_value(to_calc[wire][source_1_index]), to_calc[wire][value_index])
	elif operation == RSHIFT_OP:
		#print "op: RSHIFT ", to_calc[wire][source_1_index], ", ", to_calc[wire][value_index]
		calculated[wire] = RSHIFT(retrieve_value(to_calc[wire][source_1_index]), to_calc[wire][value_index])


def interpreter(instruction):
	ins_splited = instruction.split()

	operation = 0
	source_1 = ""
	source_2 = ""
	value = 0
	destination = ""

	if ins_splited[1] == "->":
		destination = ins_splited[2]

		try:
			value = int(ins_splited[0])
			calculated[destination] = value
		except ValueError:
			source_1 = ins_splited[0]
			to_calc[destination] = (ASSIGN_OP, source_1)

	else:
		if ins_splited[0] == "NOT":
			operation = NOT_OP
			source_1 = ins_splited[1]
			destination = ins_splited[3]
		elif ins_splited[1] == "AND":
			source_1 = ins_splited[0]
			source_2 = ins_splited[2]
			operation = AND_OP
			destination = ins_splited[4]
		elif ins_splited[1] == "OR":
			source_1 = ins_splited[0]
			source_2 = ins_splited[2]
			operation = OR_OP
			destination = ins_splited[4]
		elif ins_splited[1] == "LSHIFT":
			source_1 = ins_splited[0]
			value = int(ins_splited[2])
			operation = LSHIFT_OP
			destination = ins_splited[4]
		elif ins_splited[1] == "RSHIFT":
			source_1 = ins_splited[0]
			value = int(ins_splited[2])
			operation = RSHIFT_OP
			destination = ins_splited[4]

		to_calc[destination] = (operation, source_1, source_2, value)

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as file:
		instructions = []

		for line in file:
			instructions.append(line)

		assemble(instructions)