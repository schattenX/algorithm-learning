#build_matrix.py
def build_matrix_(row, coloumn):
	"""创建一个row*coloumn的矩阵"""
	matrix = []
	for i in range(1, row + 1):
		matrix.append([])
		index = matrix[i - 1]
		for j in range(1, coloumn + 1):
			index.append(0)
	return matrix

# mat = [
#   [10, 20, 30],
#   [40, 50, 60],
#   [70, 80, 80]
# ]

# print(mat[0][0])
# matrix = build_matrix(3, 3)
# print(matrix[1][2])