#!/usr/bin/env python
import os
import sys
# new code

def print_thing(string_to_print):
	"""Print Function"""
	new_thing = string_to_print + "hola!"

	return new_thing

def main():
	"""Main Function"""
	first_string = "hello world and "
	new_string = print_thing(first_string)
	print(new_string)

if __name__ == "__main__":
	main()
