from random import randint

""" returns an array of 20 random numbers from an array of 1 to 80 """
def lucky_numbers():
	kino_table = range(1,81) # from 1 to 80
	samples = 20
	lucky_numbers = []

	for i in range(samples):
		number = kino_table[randint(0,(len(kino_table)-1))] # a random number in array kino_table
		lucky_numbers.append(number)
		kino_table.remove(number)

	return lucky_numbers
	
""" counts how many numbers from array your_guesses are in array lucky_numbers """
def right_guesses(your_guesses, lucky_numbers):
	right_tryies = 0
	for i in range(len(your_guesses)):
		if lucky_numbers.count(your_guesses[i]) == 1: # number in your_guesses is in lucky_numbers
			right_tryies += 1
	return right_tryies
	
""" prints the result of the game in a nice form """
def print_on_screen(lucky_numbers):
	counter = 0
	for i in range(80):
		if lucky_numbers.count(i+1)==1:
			print "X  ",
		else:
			if i < 10:
				print "%d  " % (i+1),
			else:
				print "%d " % (i+1),
		counter += 1
		if (counter % 10) == 0:
			print "\n"
	
			
		