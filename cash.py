"""cash you can win if you play with 12 numbers"""
def twelve_game(right_guesses):
	prizes = [5, 25, 150, 1000, 2500, 25000, 1000000]
	if right_guesses > 5:
		try:
			return prizes[right_guesses - 6]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 11 numbers"""
def eleven_game(right_guesses):
	prizes = [1, 10, 50, 250, 1500, 15000, 500000]
	if right_guesses > 4:
		try:
			return prizes[right_guesses - 5]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 10 numbers"""
def ten_game(right_guesses):
	prizes = [2, 20, 80, 500, 10000, 100000]
	if right_guesses > 4:
		try:
			return prizes[right_guesses - 5]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 9 numbers"""
def nine_game(right_guesses):
	prizes = [1, 5, 25, 200, 4000, 40000]
	if right_guesses > 3:
		try:
			return prizes[right_guesses - 4]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 8 numbers"""
def eight_game(right_guesses):
	prizes = [2, 10, 50, 1000, 15000]
	if right_guesses > 3:
		try:
			return prizes[right_guesses - 4]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 7 numbers"""
def seven_game(right_guesses):
	prizes = [1, 3, 20, 100, 5000]
	if right_guesses > 2:
		try:
			return prizes[right_guesses - 3]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 6 numbers"""
def six_game(right_guesses):
	prizes = [1, 7, 50, 1600]
	if right_guesses > 2:
		try:
			return prizes[right_guesses - 3]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 5 numbers"""
def five_game(right_guesses):
	prizes = [2, 20, 450]
	if right_guesses > 2:
		try:
			return prizes[right_guesses - 3]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 4 numbers"""
def four_game(right_guesses):
	prizes = [1, 4, 100]
	if right_guesses > 1:
		try:
			return prizes[right_guesses - 2]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 3 numbers"""
def three_game(right_guesses):
	prizes = [2.5, 25]
	if right_guesses > 1:
		try:
			return prizes[right_guesses - 2]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 2 numbers"""
def two_game(right_guesses):
	prizes = [1, 5]
	if right_guesses > 0:
		try:
			return prizes[right_guesses - 1]
		except:
			print "Correct guesses out of range."
			return 0
	else:
		return 0
		
"""cash you can win if you play with 1 number"""
def one_game(right_guesses):
	if right_guesses == 1:
		return 2.5
	else:
		return 0
		
""" the price you win if you play game_mode numbers and guessed right_tryies right """
def determine_price(right_tryies, game_mode):
	if game_mode == 12:
		return twelve_game(right_tryies)
	elif game_mode == 11:
		return eleven_game(right_tryies)
	elif game_mode == 10:
		return ten_game(right_tryies)
	elif game_mode == 9:
		return nine_game(right_tryies)
	elif game_mode == 8:
		return eight_game(right_tryies)
	elif game_mode == 7:
		return seven_game(right_tryies)
	elif game_mode == 6:
		return six_game(right_tryies)
	elif game_mode == 5:
		return five_game(right_tryies)
	elif game_mode == 4:
		return four_game(right_tryies)
	elif game_mode == 3:
		return three_game(right_tryies)
	elif game_mode == 2:
		return two_game(right_tryies)
	else:
		return one_game(right_tryies)
		
		
		