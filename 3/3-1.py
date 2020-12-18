"""
Part 1
Starting at the top-left corner of your map and following a slope of
right 3 and down 1, how many trees would you encounter?

These aren't the only trees, though; due to something you read about once
involving arboreal genetics and biome stability, the same pattern repeats
to the right many times.

Part 2
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""


def check_tree(position: int, line: str) -> bool:
	return line[position] == '#'


def count_trees(lines: list, deltaX: int, deltaY: int) -> int:
	line_length = len(lines[0])
	current_pos = 0
	tree_counter = 0

	for i in range(deltaY, len(lines), deltaY):
		if current_pos + deltaX >= line_length:
			current_pos = current_pos + deltaX - line_length
		else:
			current_pos += deltaX

		if i > 0:
			if check_tree(current_pos, lines[i]):
				tree_counter += 1

	return tree_counter

def main():
	file_name = "./input.txt"

	with open(file_name, "r") as f:
		lines = [x.rstrip("\n") for x in f]

	r1d1 = count_trees(lines, 1, 1)
	r3d1 = count_trees(lines, 3, 1) # part 1
	r5d1 = count_trees(lines, 5, 1)
	r7d1 = count_trees(lines, 7, 1)
	r1d2 = count_trees(lines, 1, 2)

	product = r1d1 * r3d1 * r5d1 * r7d1 * r1d2 # part 2

	print ( f'right 1 down 1: {r1d1}')
	print ( f'right 3 down 1: {r3d1}')
	print ( f'right 5 down 1: {r5d1}')
	print ( f'right 7 down 1: {r7d1}')
	print ( f'right 1 down 2: {r1d2}')

	print (f'product: {product}')
		

if __name__ == "__main__":
	main()