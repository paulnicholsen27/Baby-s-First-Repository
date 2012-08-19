longest = 0
winner = 1

#find n with longest collatz string 

for n in range(1,1000000):
	a = n
	list = []
	while n != 1:
		list.append(n)
		if n%2==0:
			n = n/2
		else:
			n = 3 * n + 1
	if len(list) > longest:
		longest = len(list)
		winner = a
print winner