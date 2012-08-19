def fibonacci(n):
	list = [1,2]
	first = 1
	second = 2
	for number in range (3,n):
		third = first + second
		if third < 4000000:
			list.append(third)
			first = second
			second = third
		else:
			break
	sum = 0
	for fib in list:
		if fib % 2 == 0:
			sum += fib
	return sum
	
print fibonacci(4000000)