""""
Sum square difference
Problem 6


Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer:
25164150
Completed on Fri, 13 Jan 2017, 02:39


"""

def main():
	num_list = xrange(1,101)

	sum_squares = sum([i**2 for i in num_list])
	square_sum = (sum([i for i in num_list]))**2

	print square_sum - sum_squares
		
if __name__ == "__main__":
	main()


	

