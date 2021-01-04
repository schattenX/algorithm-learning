#binary_search.py


def binary_search(list, item):
	low = 0
	high = len(list) - 1 
	count = 0
	while low <= high:
		mid = (low + high) // 2
		guess = list[mid]
		count += 1

		if guess == item:
			return count
		elif guess < item:
			low = mid + 1
		else:
			high = mid - 1

	return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 1)) 
print(binary_search(my_list, -1))
print(binary_search(my_list, 9))
