"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


Answer:
233168
Completed on Thu, 15 Sep 2016, 20:08

"""

def main():

	num_list = xrange(3,1000)
	multiples = [i for i in num_list if i % 3 == 0 or i % 5 == 0]
	sum_of_multiples = sum(multiples)	
	print sum_of_multiples

if __name__ == "__main__":
	main()
