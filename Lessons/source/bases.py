#!python

import string
from math import floor, log

# A string of '01234...vwxyz'
int_to_string = string.digits + string.ascii_lowercase

# A dictionary of { '0': 0, '1': 1, ....., 'y': 34, 'z': 35 }
string_to_int = { s: i for i, s in enumerate(int_to_string) }


def decode(digits: str, base: int) -> int:													# EXAMPLE:
	""" Decode given digits in given base to number in base 10. """		#			digits = '1100', base = 2
																																		#				
	assert 2 <= base <= 36, 'base is out of range: {}'.format(base)		#	   index | digit | string_to_int[digit] | base**index | output
																																		# 1)   0   |  '0'  |          0           |   2^0 = 1   |   0        
	digits = digits.lower() # Ensure there are no capital letters     # 2)   1   |  '0'  |          0           |   2^1 = 2   |   0
	output = 0 						 	# Initialize output integer as zero       # 3)   2   |  '1'  |          1           |   2^2 = 4   |   4
																																		# 4)   3   |  '1'  |          1           |   2^3 = 8   |   12
	for index, digit in enumerate(reversed(digits)):
		output += string_to_int[digit] * (base**index)

	return output


def encode(number: int, base: int) -> str:
	""" Encode given number in base 10 to digits in given base. """

	assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
	assert number >= 0, 'number is negative: {}'.format(number)

	if number == 0:
		return '0'

	output = ''
	largest_power = floor(log(number, base))

	# Count down from largest_power to 0
	for i in range(largest_power, -1, -1):

		if number >= base**i:
			new_digit = number // (base**i)
			number -= new_digit * (base**i)
			output += int_to_string[new_digit]

		else:
			output += '0'
		
	return output


def convert(digits: str, base1: int, base2: int) -> str:
	""" Convert given digits in base1 to digits in base2. """
	# Handle up to base 36 [0-9a-z]
	assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
	assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
	
	return encode(decode(digits, base1), base2)


def main():
	"""Read command-line arguments and convert given digits between bases."""
	import sys
	args = sys.argv[1:]  # Ignore script file name
	if len(args) == 3:
		digits = args[0]
		base1 = int(args[1])
		base2 = int(args[2])
		# Convert given digits between bases
		result = convert(digits, base1, base2)
		print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
	else:
		print('Usage: {} digits base1 base2'.format(sys.argv[0]))
		print('Converts digits from base1 to base2')


if __name__ == '__main__':
	main()
