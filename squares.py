def sum_squares(n):
	sum = 0
	for number in range(1,n+1):
		sum += number ** 2
	return sum
	
def square_sums(m):
	a = sum(range(1,(m+1)))  ** 2
	return a
	
print sum_squares(100) - square_sums(100)