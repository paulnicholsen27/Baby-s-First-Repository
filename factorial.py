def factorial(n):
	if n == 1:
		return 1
	return n * factorial(n-1)

def sum_of_digits(q):		
	sum = 0
	for chr in str(factorial(q)):
		sum += int(chr)
	return sum
	
print sum_of_digits(3)
print sum_of_digits(100)