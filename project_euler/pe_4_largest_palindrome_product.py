"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Answer:
906609
Completed on Mon, 10 Oct 2016, 04:33


"""


def is_palindrome(num):
	string = str(num)
	reverse = string[::-1]
	reverse_num = int(reverse)
	palin_list = []
	if num == reverse_num:
		return True
	else: 
		return False

def main():
		
	three_digits = range(100,1000)
	length = len(three_digits)-1
	i = 0
	palin_list = []
	while i <= length:
		for item in three_digits:
			number = three_digits[i] * item
			if is_palindrome(number):
				palin_list.append(number)	 		
		i = i+1
	print max(palin_list)
	
if __name__ == "__main__":
	main()
