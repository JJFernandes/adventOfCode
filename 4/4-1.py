"""
Count the number of valid passports - those that have all required fields. 
Treat cid as optional.
"""

import re


REQ_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} # "cid" is optional


def validate_passport(line: str) -> bool:
	passport = line.split(" ")

	if len(passport) >= 7:
		counter = 0
		for field in passport:
			if field.split(":")[0] in REQ_FIELDS:
				counter += 1
		if counter == 7:
			return True

	return False


def main():
	file_name = "./input.txt"

	with open(file_name, "r") as f:
		lines = [re.sub('[\n]', ' ', line) for line in f.read().split("\n\n")]
		

		counter = 0
		for line in lines:			
			if validate_passport(line):
				counter += 1

		print(counter)
		

if __name__ == "__main__":
	main()