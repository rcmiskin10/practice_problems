"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Answer:
6857
Completed on Sat, 7 Jan 2017, 17:08

"""

def main():

	number = 600851475143
	div_nums = xrange(2, int(number**0.5) + 1)
	factors = (num for num in div_nums if number % num == 0 if is_prime(num))
	
	print max(factors)		
			
def is_prime(n):
	if n<2:
		return False
	if n==2:
		return False
	if n%2==0:
		return False
	for i in xrange(3, int(n**0.5) + 1, 2):
		if n%i==0:
			return False
	return True
			

if __name__ == "__main__":
	main()
