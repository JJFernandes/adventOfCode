# non-decreasing insertion sort
def insertion_sort(arr: list):
	for i in range(len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key


def two_entries_k_sum(arr: list, k: int):
	for num1 in arr:
		if k-num1 in arr:
			return num1, k-num1


def three_entries_k_sum(arr: list, k: int):
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if k-(arr[i] + arr[j]) in arr:
				return arr[i], arr[j], k-(arr[i]+arr[j])


def main():
	file_name = "./input.txt"

	with open(file_name, "r") as f:
		lines = [int(x) for x in f]

	insertion_sort(lines)

	num1, num2 = two_entries_k_sum(lines, 2020)
	print(f'num1: {num1}, num2: {num2} | product: {num1*num2}')
	
	# output: "num1: 947, num2: 1073 | product: 1016131"

	num1, num2, num3 = three_entries_k_sum(lines, 2020)
	print(f'num1: {num1}, num2: {num2} , num3: {num3} | product: {num1*num2*num3}')

	# output: "num1: 491, num2: 618 , num3: 911 | product: 276432018"


if __name__ == "__main__":
	main()
