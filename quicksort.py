#quicksort.py
def quick_sort(array):
	"""进行快速排序"""
	if len(array) < 2:
		return array
	else:
		mid = len(array) // 2
		pivot = array[mid]
		#找出小于基准值的数
		less = [i for i in array[:mid] + array[mid+1:] if i <= pivot]
		#找出大于基准值的数
		greater = [i for i in array[:mid] + array[mid+1:] if i > pivot]

		return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([2, 5, 10, 10, 0, 100, 49, 20]))