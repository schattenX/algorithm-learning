#call_stack.py
def fact(x):
	"""求x的阶乘"""
	if x == 1:
		return 1
	else:
		return x * fact(x - 1)

print(fact(10))
