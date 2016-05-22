import time
from computer import *
from cash import determine_price
import sys

def play_kino():
	your_numbers = []
	computer_numbers = lucky_numbers()
	print "Which game mode you want to play (1 to 12)?"
	mode = int(raw_input());
	print_on_screen([])
	if mode < 1 or mode > 12:
		print "ERROR: Choose a mode between 1 to 12."
		sys.exit(0)
	print "Please select %d numbers from 1 to 80" % (mode)
	time.sleep(1)
	for i in range(mode):
		print "Number %d:" % (i+1)
		number = int(raw_input());
		if your_numbers.count(number) == 1:
			print "ERROR: Choose a value only once."
			sys.exit(0)
		if number < 1 or number > 80:
			print "ERROR: number must be between 1 to 80."
			sys.exit(0)
		your_numbers.append(number)
	print "\nYou choose:"
	print your_numbers
	time.sleep(1)
	print "\nKino result:\n"
	print_on_screen(computer_numbers)
	time.sleep(1)
	print "\nCalculating your price...\n"
	time.sleep(3)
	print "You win (in euro):"
	print determine_price(right_guesses(your_numbers, computer_numbers), mode)
		
		
		
play_kino()