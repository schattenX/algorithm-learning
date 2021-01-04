#sum.py
import sys
from random import randint
sys.setrecursionlimit(9000000)

def sum(arr):
	"""利用递归求和"""
	if arr == []:
		return 0 
	else:
		num = arr.pop(0)
		return num + sum(arr)

def num_element(arr):
	"""计算列表元素数"""
	if arr == []:
		return 0
	else:
		del arr[0]
		return num_element(arr) + 1

def find_biggest():
	"""找出列表内最大数字"""
	arr = random_list(50)
	max = arr[0]
	for num in arr:
		if max < num:
			max = num
	return max

def random_list(times):
	"""生成随机列表"""
	arr = []
	for i in range(times):
		arr.append(randint(1,101))
	return arr
print(random_list(50))
print(find_biggest())