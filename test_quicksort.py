#test_quicksort.py
import unittest
from quicksort import quick_sort

class TestQuickSort(unittest.TestCase):
	"""对quicksort.py的测试"""
	def test_quick_sort(self):
		sorted_list = quick_sort([2, 5, 10, 0, 100, 49, 20])
		self.assertEqual(sorted_list, [0, 2, 5, 10, 20, 49, 100])

unittest.main()