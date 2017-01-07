"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

def all_divisible(x):

	num_list = xrange(1,21)
	for item in num_list:
		if x % item != 0:
			return False
	return True
	

def main():
	i = 1
	while True:
		if all_divisible(i):
			break
		else:
			i = i+1
	print i
		
			
		
	

if __name__ == "__main__":
	main()
