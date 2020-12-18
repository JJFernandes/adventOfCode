"""
Each line gives the password policy and then the password. The password
policy indicates the lowest and highest number of times a given letter must
appear for the password to be valid. For example, 1-3 a means that the
password must contain a at least 1 time and at most 3 times.
"""


import re


def get_count(passwd: str, letter: chr) -> int:
	return passwd.count(letter)


def check_policy(bounds: str, letter: chr, passwd: str) -> bool:
	lower, upper = map(int, tuple(bounds.split('-')))

	count = get_count(passwd, letter)

	if count >= lower and count <= upper:
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