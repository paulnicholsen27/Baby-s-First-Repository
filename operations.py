def factor(n): #lists all factors of a number
	factor_list = []
	for number in range (1,int(n**.5)+1):
		if n % number == 0:
			factor_list.append(number)
			if n / number != number:
			    factor_list.append(n/number)
	return factor_list


def prime(n): #determines if n is prime
	if n == 1:
	    return False
	factor_list = [1,n]
	for divisor in range(2,int(n**.5)+1):
	    if n % divisor == 0:
	        return False
	        break
	return True

def prime_list(n):
    list=[2]
    a = 3
    while a <= n:
        if prime(a):
            list.append(a)
            a += 2
        else:
            a += 2
    return list
    

       
def product(n): #multiplies all the numbers in a list
    a = 1
    product = 1
    while a <= n:
        product = product * a
        a += 1
    return product
    
def prime_factors(n):
	factor_list = []
	factor = 2
	while True:
		if n % factor == 0:
			factor_list.append(factor)
			n = n / factor
		else:
			factor +=1
		if n / float(factor) == 1.0:
			factor_list.append(factor)
			print factor_list
			break
# 	biggest = 1 
# 	for item in factor_list:
# 		if item > biggest:
# 			biggest = item
# 	return biggest


def palindrome(n):
	n = str(n)
	if len(n) == 0 or len(n) == 1:
		return True
	if n[0] == n[-1]:
		return palindrome(n[1:-1])
	else:
		return False

def bigpal():
	products = []		
	for i in range(100,999):
		for j in range(100,999):
			products.append(i*j)
	products.sort()
	a = -1
	while True:
		if palindrome(products[a]):
			return products[a]
		else:
			a = a - 1
			
def triangle():
    a = 1
    while True:
        if len(factor(a/2.0 * (a+1))) > 500:
            print "First is: "
            return (a/2.0 * (a+1))
        else:
            a +=1

def factor_sum(n):
    total = sum(factor(n)) - n
    return total

# factor_sums = dict([(n, factor_sum(n)) for n in range(1,10000)])
# print factor_sums
# 
# values = {}
# amic_total = 0
# for key,value in factor_sums.iteritems():
#     try:
#         if factor_sums[factor_sums[key]] == key and key!=value:
#             amic_total += key
#     except KeyError:
#         pass        
# print amic_total
