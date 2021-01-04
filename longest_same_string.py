#longest_same_string.py
from build_matrix import build_matrix_
from time import sleep
def get_compare_words():
	"""获取需要比较的字符串"""
	str1 = input("Please enter the first string: ")
	str2 = input("Please enter the second string: ")
	return str1, str2

def build_mat():
	"""搭建矩阵，与分割所得字符串"""
	str1, str2 = get_compare_words()
	word_a = list(str1)
	word_b = list(str2)
	cell = build_matrix_(len(word_a), len(word_b))
	return cell, word_a, word_b

def search_lstri(cell):
	"""从矩阵中寻找最长公共字串，以及长度"""
	max = cell[0][0]
	for i in range(0, len(word_a)):
		for j in range(0, len(word_b)):
			if cell[i][j] > max:
				max = cell[i][j]

	return max
	

cell, word_a, word_b = build_mat()
print(word_a, word_b)
#嵌套循环遍历矩阵
for i in range(len(word_a)):
	for j in range(len(word_b)):
		if word_a[i] == word_b[j]:
			if i == 0 or j == 0:
				cell[i][j] += 1

			else:
				cell[i][j] = cell[i - 1][j - 1] + 1
print(cell)
print(search_lstri(cell))


