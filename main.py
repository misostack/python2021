# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import constant

def example_001():
	a = 1 + 2 + 3 + \
		4 + 5 + 6 + \
		7 + 8 + 9
	return a

def example_002():
	a = (1* 2 * 3 *
		4 * 5 * 6 *
		7 * 8 * 9
		)
	return a

def example_003():
	a, b, c = 1, 2, 3
	x = 1; y = 2; z = 3;
	return a + b + c + x * y * z

def example_004():
	colors = [
		'red', 'green', 'blue',
		'gray', 'orange', 'pink'
	]
	return colors

def example_005():
	for i in range(1,10):
		print(i)
		if i == 5:
			break

def example_006():
	print(constant.PI)
	print(constant.GRAVITY)

def example_007():
	a = 0b01
	b = 100
	c = 0o10
	d = 0x0A #Hexadecimal Literal
	# FLOAT Literals
	f_001 = 10.5
	f_002 = 1.5e2
	f_003 = 1.5 * 100
	# COMPLEX
	#Complex Literal 
	x = 1+3.14j
	print(a,b,c,d,f_001,f_002,f_003,x,x.real, x.imag)
	# String literals
	a_str = "simple string\n"
	char = "C\n"
	lines = """
	Line 1 \n
	Line 2 \n
	Line 3 \n
	"""
	unicode = u"\u00dcnic\u00f6de"
	raw_str = r"raw \n string"	
	print(a_str,char, lines, unicode, raw_str)
	# Boolean literals: True | False
	print("1 == True", 1 == True)
	print("0 == True", 0 == True)
	print("'' == True", "" == True)
	print("0.0 == True", 0.0 == True)
	count = 10
	is_valid_answer = False
	count += is_valid_answer
	print(count)
	# Special literals: None
	drink = "Coffee"
	food = None
	def menu(x):
		if x == drink:
			print(drink)
		else:
			print(food)
	menu(drink)
	menu(food)
	# literals collections
	fruits = ['apple','mango','orange', 1, 2.0] # list
	numbers = ('a', 2, 3.0) # tuple : freeze
	user = {'first_name': 'Python', 'last_name': 'Fundamentals', 'description': 'Tutorial'} # dictionary
	vowels = {'a', 'e', 'i' , 'o', 'u'} #set : freeze
	fruits[0] = 'mango'
	print(fruits)
	print(numbers)
	k = 'description'	
	user[k] += ' Headfirst'
	print(user, user['first_name'], user['last_name'], user[k])	
	print(vowels)
	# numbers
	a = 5
	print(a, "is of type", type(a))

	a = 2.0
	print(a, "is of type", type(a))

	a = 1+2j
	print(a, "is complex number?", isinstance(1+2j,complex))

	a = 123456789123456789123456789123456789123456789123456789 # memory limit
	b = 0.123456789123456789123456789123456789123456789123456789 # 15
	print(a,b)

	# list
	a = [5,10,15,20,25,30,35,40]
	print(a[0], a[5])
	print(a[0:3])
	print(a[4:])
	print(a[:3])
	print(a[:-2])	
	# tuple
	b = (5, '2021', 'Jan', True)
	print(b[0], b[0:2], a[0:-1])
	# string
	str = "pythondevelopers"
	print(str[0:5], str[:-1])
	# set
	uniqueValues = {1,1,1,2,3,4,5} # unorder list
	print(uniqueValues)
	# dict
	obj = { 1: 'asda', 'name': 'something', 'value': 1.5e3, 'isValid': False}
	print(obj)
	# conversion
	n = "25"
	m = "1"
	total = int(n) + int(m)
	print(total)
	# collections: list, tuple, set, dict
	a = tuple([1,2,3,1,2,3])
	print(type(a), list(a), type([1,2,3]), set(a),list(set(a)))
	print(dict([['first_name', 'Python'],['last_name','Tutorial']]))
	# output format
	x = 5; y = 10;
	print('{} + {} = {}'.format(x, y, x + y))
	a = 'Python'; b = 'Tutorial';
	print('{1} {0}'.format(b,a))
	first_name = 'Python'; last_name = 'Tutorial'
	print('{first_name} {last_name}'.format(first_name=first_name, last_name=last_name))
	x = 123456.23456
	print('x = %3.2f' %x)
	import math
	print(math.pi)
	import sys
	print(sys.path)
	# modulus, floor
	x = 5;
	from fractions import Fraction
	print('{} % 2 = {}\n {} // 2 = {}\n {}^{} = {}\n {}/{}={}'.format(x, x%2, x, x//2, 2,3, 2**3, 2,3,2/3))
	print(Fraction(float(1/3)))
	# logical: and, or not
	if not False:
		print('False')
	else:
		print('True')
	for x in range(1,100):
		if isPrime(x): print('{} '.format(x))
	# same memory check
	t = 5;
	z = t;
	v = 5;
	print('Is {} and {} on the same memory? {}'.format(t,z, t is z))
	print('Is {} and {} not on the same memory? {}'.format(t,v, t is not v))
	str_a = "hello"
	str_b = "hello"
	list_a = [1,2,3]
	list_b = [1,2,3]
	print(str_a is str_b)
	print(list_a is list_b)
	print(tuple(list_a) is tuple(list_b))
	# Membership operators
	print("{} is in {} ? {}", 'e', str_a, 'e' in str_a)
	print("{} is in {} ? {}", '1', str_a, '1' not in str_a)
	print("{} is in {} ? {}", 1, list_a, 1 in list_a)
	print(id(str_a), id(str_b), id(list_a), id(list_b), id(t), id(z), id(v))
	def printHello():
	    print("Hello")

	a = printHello
	a()
	# Built-in namespace > Module: Global namespace > Function: Local namespace

def example_008():
	'''In this program, 
	we check if the number is positive or
	negative or zero and 
	display an appropriate message'''

	num = 3.4

	# Try these two variations as well:
	# num = 0
	# num = -4.5

	if num > 0:
	    print("Positive number")
	elif num == 0:
	    print("Zero")
	else:
	    print("Negative number")

	arr = [3, 5, 4, 1, 1, 1, 4, 5, 2, 2, 3]
	for x in arr:
		print(x)


def isPrime(n):
	if n == 1 or n == 2: return True
	for i in range(2,n-1):
		if( n % i == 0): return False
	return True

def multiply(a, b):
    return a * b

def double(num):
    """Function to double the value"""
    return 2*num    

def print_hi(name):
    """Function to say hello with name input"""
    print(f'Hi, {name}')    


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(multiply(1, 2))
    print(example_001())
    print(example_002())
    print(example_003())
    print(example_004())
    example_005()
    print(double.__doc__)
    print(print_hi.__doc__)
    example_006()
    example_007()
    example_008()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
