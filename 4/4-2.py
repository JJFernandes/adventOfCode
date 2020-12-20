"""
Count the number of valid passports - those that have all required fields and valid values.

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

import re


def validate_passport(line: str) -> bool:
	passport = line.split(" ")

	if len(passport) >= 7:
		counter = 0
		REQ_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
		for field in passport:
			fld_type, fld_value = map(str, tuple(field.split(':')))
			if fld_type == "byr" and fld_type in REQ_FIELDS and re.match("^[0-9]{4}$", fld_value) and int(fld_value) >= 1920 and int(fld_value) <= 2002:
				REQ_FIELDS.remove(fld_type)
				counter += 1
			elif fld_type == "iyr" and fld_type in REQ_FIELDS and re.match("^[0-9]{4}$", fld_value) and int(fld_value) >= 2010 and int(fld_value) <= 2020:
				REQ_FIELDS.remove(fld_type)
				counter += 1
			elif fld_type == "eyr" and fld_type in REQ_FIELDS and re.match("^[0-9]{4}$", fld_value) and int(fld_value) >= 2020 and int(fld_value) <= 2030:
				REQ_FIELDS.remove(fld_type)
				counter += 1
			elif fld_type == "hgt" and fld_type in REQ_FIELDS and \
				((re.match("^[0-9]{3}cm$", fld_value) and int(fld_value[:-2]) >= 150 and int(fld_value[:-2]) <= 193) \
				or (re.match("^[0-9]{2}in$", fld_value) and int(fld_value[:-2]) >= 59 and int(fld_value[:-2]) <= 76)):
				REQ_FIELDS.remove(fld_type)
				counter += 1
			elif fld_type == "hcl" and fld_type in REQ_FIELDS and re.match("^#[0-9a-f]{6}$", fld_value):
				REQ_FIELDS.remove(fld_type)
				counter += 1
			elif fld_type == "ecl" and fld_type in REQ_FIELDS and re.match("^amb|blu|brn|gry|grn|hzl|oth$", fld_value):
				REQ_FIELDS.remove(fld_type)
				counter += 1
			elif fld_type == "pid" and fld_type in REQ_FIELDS and re.match("^[0-9]{9}$", fld_value):
				REQ_FIELDS.remove(fld_type)
				counter += 1

		if counter == 7:
			print (passport)
			# print ("\n")
			return True

	return False


def main():
	file_name = "./input.txt"

	with open(file_name, "r") as f:
		lines = [re.sub('[\n]', ' ', line) for line in f.read().split("\n\n")]
		
		# last line only has one \n so it will have a space char that will mess things up
		lines[len(lines)-1] = lines[len(lines)-1].rstrip(" ")


		counter = 0
		for line in lines:			
			if validate_passport(line):
				counter += 1

		print(counter)
		

if __name__ == "__main__":
	main()