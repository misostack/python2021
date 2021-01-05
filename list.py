# list manipulation
import test

def sum(*numbers):
	sum = 0
	for n in numbers:
		sum += int(n)
	return sum

def test_sum():
	test.assert_equals(sum(1,2,3), 6)
	test.assert_equals(sum(1,2,3,4,5,6), 21)
	# assert sum(1,2,3) == 6, 'should be 6'
	# assert sum(1,2,3,4,5,6) == 21, 'should be 21'

def find_it(seq):
	# Cach 1 : vet' can, dem so lan xuat hien cua tung so trong list, neu so lan xuat hien la le return ngay lap tuc
	# neu ko tiep tuc so tiep theo
	# u_seq = set(seq)
	# for n in u_seq:
	# 	n_count = 0
	# 	for i in seq:
	# 		n_count += (0,1)[i==n]
	# 	if n_count % 2 != 0:
	# 		return n
	# Cach 2: su dung ham count cua list
	for n in set(seq):
		if seq.count(n) == 1 or seq.count(n) % 2 != 0:
			return n
	return None

def example_001():
	print('''
	Example 001:
	Given an array of integers, find the one that appears an odd number of times.
	There will always be only one integer that appears an odd number of times.
	// Dich
	Cho 1 day so nguyen, tim so tu nhien co so lan xuat hien la 1 so le.
	Biet rang chi co duy nhat 1 so co so lan xuat hien la 1 so le
	''')
	test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
	test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
	test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
	test.assert_equals(find_it([10]), 10);
	test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
	test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);	

def example_002():
	print('''
		Counting sheep
	''')
	sheeps = [True,  True,  True,  False,
	  True,  True,  True,  True ,
	  True,  False, True,  False,
	  True,  False, False, True ,
	  True,  True,  True,  True ,
	  False, False, True,  True]
	def count_sheeps(sheeps):
		# 1st-simple way: use count method of list
		# return sheeps.count(True)
		# 2nd: filter and check length
		# sheeps_filter = filter(lambda x: x == True,sheeps)
		# for k in sheeps_filter:
		# 	print(k)
		# return len(list(sheeps_filter))
		# 3rd: python comprehension
		return len([x for x in sheeps if x])

	test.assert_equals(count_sheeps(sheeps), 17, "There are 17 sheeps in total, not %s" % count_sheeps(sheeps))

def example_003():
	print("""
	             1
	          3     5
	       7     9    11
	   13    15    17    19
	21    23    25    27    29		

	Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

	row_sum_odd_numbers(1); # 1
	row_sum_odd_numbers(2); # 3 + 5 = 8	

	""")

	def row_sum_odd_numbers(n):
		if n == 0:
			return 0
		# odd always start from 1 and increment steps equal "2"
		# row 1 : 1 - 1
		# row 2 : 1 , 3 , 5 - 3
		# row 3:  1, 3, 5, 7, 9, 11 - 6
		# row 4:  1, 3, 5, 7, 9, 11, 13, 15, 17, 19 - 10 = 4 * 5/2
		if n == 1:
			return 1
		sum = 0
		max_number = n * (n + 1) - 1
		print (n, max_number)

		while(n > 0):			
			sum += max_number
			max_number -= 2
			n -= 1
		return sum

	test.assert_equals(row_sum_odd_numbers(1), 1)
	test.assert_equals(row_sum_odd_numbers(2), 8)
	test.assert_equals(row_sum_odd_numbers(13), 2197)
	test.assert_equals(row_sum_odd_numbers(19), 6859)
	test.assert_equals(row_sum_odd_numbers(41), 68921)


def main():
	print('list manipulation')
	# test_sum()
	# example_002()
	example_003()
if __name__ == '__main__':
	main()