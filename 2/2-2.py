"""
Each policy actually describes two positions in the password, where 1 means
the first character, 2 means the second character, and so on. (Be careful;
Toboggan Corporate Policies have no concept of "index zero"!) Exactly one
of these positions must contain the given letter. Other occurrences of the
letter are irrelevant for the purposes of policy enforcement.
"""


import re


def get_positional_char(passwd: str, pos1: int, pos2: int) -> chr:
	return passwd[pos1-1], passwd[pos2-1]


def check_policy(bounds: str, letter: chr, passwd: str) -> bool:
	pos1, pos2 = map(int, tuple(bounds.split('-')))

	charAtPos1, charAtPos2 = get_positional_char(passwd, pos1, pos2)

	if charAtPos1 == letter and charAtPos2 != letter:
		return True
	elif charAtPos1 != letter and charAtPos2 == letter:
		return True
	
	return False


def main():
	file_name = "./input.txt"

	with open(file_name, "r") as f:
		lines = [re.sub('[:\n]', '', x).split(" ") for x in f]

	counter = 0

	for line in lines:
		if check_policy(line[0], line[1], line[2]):
			counter += 1

	print(counter)


if __name__ == "__main__":
	main()