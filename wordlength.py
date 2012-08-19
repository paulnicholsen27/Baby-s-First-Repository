words = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', 
	'9':'nine', '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', 
	'15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen', '20':'twenty',
	'30':'thirty', '40':'forty', '50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty',
	'90':'ninety'}
		
def letter_count(n):
	if 1<=n<=19:
		return len(words[str(n)])
	if 20<=n<=99:
		n = str(n)
		if n[1]=='0':
			return len(words[n])
		return len(words[n[0] + '0']) + len(words[n[1]])
	if n >= 99:
		n=str(n)
		if n[1:]=='00':
			return len(words[n[0]]) + 7 #7 for hundred
		return len(words[n[0]]) + letter_count(int(n[1:])) + 10 #10 for 'hundred and'

sum = 0

for number in range(1,1000):
	sum += letter_count(number)
print sum + 11 #11 for one thousand