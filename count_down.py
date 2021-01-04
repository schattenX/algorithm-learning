#count_down.py
def count_down(i):
	print(i)
	if i <= 1:
		return
	else:
		count_down(i - 1)

count_down(100) 
