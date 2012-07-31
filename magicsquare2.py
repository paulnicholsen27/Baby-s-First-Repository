def magicsquare():
	import os #clears screen
	os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
	print "A magic square is a square of distinct numbers with an odd number of"
	print "rows and columns, where all of the elements in each row and each column"
	print "add up to the same number.  Let's make one."
	n = raw_input('How many rows and columns would you like? ') #determines square size
	try:
		n = int(n)
	except ValueError: #Checks input is a number
		print "That's not a number.  You're not playing right."
		print "Here's a 3 X 3 Magic Square."
		n = 3	
	if n <= 0: #if n is zero or negative
		print "How exactly would you expect me to draw "
		print "something with " + str(n) + " rows?"
		print "Here's a 7 X 7 Magic Square.  It's quite nice."
		n = 7
	if isinstance(n, int) == False: #n is a non-integer number
		decimal_place = str(n).find(".")
		decimal_part = str(n)[decimal_place:]
		print "Really?  I can't quite make " + decimal_part + " rows, can I?"
		m = n + .5  #round to nearest integer
		m = int(m)
		if m % 2 == 0: #changes to odd if even
			if m > n: #number was rounded up
				n = m - 1
			if m < n: #number was rounded down
				n = m + 1
		else:
			n = m
		print "The closest odd number to your number is " + str(n) + "."
	if n == 2:
		print "There is no way to make a 2 X 2 Magic Square."
		print "I'm terribly sorry.  Here's a 5 X 5 square instead."
		n = 5
	if n % 2 == 0: #checks for even
		n = n + 1
		print "I like to make odd-ordered Magic Squares.  I'm funny that way."
		print "Let's go a little higher.  How about " + str(n) + " ?"
	square = []
	for a in range (0,n):
		square.append([]) #create rows
	for row in square:
		for a in range (0,n):
			row.append([]) #create blank entries in rows
	for a in range(0,n):
		i = a + 1
		for b in range(0,n):
			j = b + 1
			square[a][b] = n * ((i + j - 1 + int(n/2)) % n) + ((i + 2*j - 2) % n) + 1
	for item in square:
		item = ["%02d" % n for n in item] #converts single-digit numbers to double
		print " ".join(item) #removes quotes
	sum = str(n*(n**2 + 1) / 2) #computes sum of row/column
	return "Every row, column, and major diagonal adds up to " + sum + "!"
	
print magicsquare()