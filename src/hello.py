#!/usr/bin/env python

def print_thing(string_to_print):
	new_thing = string_to_print + "hola!"

	return new_thing

def main():
	first_string = "hello world and "
	new_string = print_thing(first_string)

	print new_string

if __name__ == "__main__":
	main()
