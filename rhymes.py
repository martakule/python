# List with three strings of the text with blanks to fill in
questions = ["Twinkle, twinkle, little (1)_____,\nHow I wonder what you (2)_____!\nUp above the world so (3)_____,\nLike a diamond in the (4)_____.", "Tweedledum and Tweedledee\nAgreed to have a (1)_____;\nFor Tweedledum said (2)_____\nHad spoiled his nice new rattle.\nJust then flew down a monstrous (3)_____,\nAs black as a tar-barrel;\nWhich frightened both the heroes so,\nThey quite forgot their (4)_____.", "Tinker, (1)_____,\nSoldier, (2)_____,\nRich Man, (3)_____ Man,\nBeggar Man, (4)_____."]

# List with three lists of answers
answers=[['star', 'are', 'high', 'sky'], ['battle', 'Tweedledee', 'crow', 'quarrel'], ['Tailor', 'Sailor', 'Poor', 'Thief']]

# List of blanks
blanks=["(1)_____","(2)_____","(3)_____","(4)_____"]

# List of levels
levels=['easy','medium','hard']

#The number of allowed wrong aswers per question
wrong_limit=5

#The word to type in when the user wants to terminate the game at any time
safe_word="stop"

# This function prompts the user to pick a level and loads the appropriate level's data from above.
# It also sets the control counter and assigns the correct poem and number of allowed wrong answers.
def level_choice():
	choice = raw_input("Pick a level by typing easy, medium, or hard.\n>")
	if choice.lower() not in levels:
		print "\n*****\n\nInvalid input.\n"
		return level_choice()
	else:
		choice=levels.index(choice)
		print "\n*****\n\nYou've picked level " + levels[choice] + "! \nComplete the rhyme below one word at a time.\nYou will have " + str(wrong_limit) + " tries for each question\nIf you want to stop the game at any time, just type in " + safe_word + ".\nGood luck!\n\n*****\n"
		rhyme=questions[choice]	
		counter=0
		chances=wrong_limit
		return game (rhyme,answers[choice],counter,chances)	
	
# This function takes, correct answers and the poem, counter, and number of allowed wrong answers 
# assigned in level_choice(). It prints the poem with blanks, asks user for answer.
# Correct answer replaces the blank with the right answer from the list.
# Wrong answer subtracts one remaining allowed wrong answer and checks for their number.
# If it's 0, it prints game over and quits. The function then adds 1 to the controlling counter.
# If it equals the length of the blanks list, it completes the game.
def game(rhyme,ans,counter,chances):
	while counter<len(blanks):
		print "Now the rhyme reads like this:\n\n" + rhyme
		user_answer=raw_input("\n*****\n\nWhat word replaces"+blanks[counter]+"?\n\n>")
		if answer_check (user_answer,ans[counter],safe_word) == True:
			chances=wrong_limit 
			rhyme=rhyme.replace((blanks[counter]),ans[counter])
		else:
			chances=chances-1
			if chances==0:
				print "*****\n\nGame over.\nThanks for playing!\n"
				quit()
			else:
				wrong_answer_countdown(chances) 
				return game(rhyme,ans,counter,chances)
		counter+=1
	if counter==len(blanks):
		print rhyme
		print "\n*****\n\nCongratulations! You completed the game.\nThanks for playing!\n"

# This function takes the number of remaining allowed wrong answers and prints a different sentence 
# for 2 and 1 tries left.
def wrong_answer_countdown(chances):
	if chances == wrong_limit-(wrong_limit-2):
		print "\n*****\n\nGive it a think! You have only " +str(chances) + " more tires!\n"
	elif chances == wrong_limit-(wrong_limit-1):
		print "\n*****\n\nMake this count! This is your " +str(chances) + " last try!\n"
	else:
		print "\n*****\n\nTry again! You have " +str(chances) + " more tires!\n"
		
# This function takes the user's answer and checks it against the provided answers.
# It also takes the safe word -- if the user's input equals it, it prints a farewell message and
# terminates the game. If the answer is correct, it prints a message and returns the True value.
# Else, it returns False to trigger the wrong answer action in game().
def answer_check (user_answer,ans,safe_word):
	if user_answer.lower()==ans.lower():
		print "\n*****\n\nCorrect!\n"
		return True 
	elif user_answer.lower()==safe_word.lower():
		print "\n*****\n\nAll right! We're stopping here. Thanks for playing!\n"
		quit()
	else:
		return False 
		
#These lines welcome the user to the game and fire off the first function.
print "\nWelcome to the Nursery Rhymes Quiz!"
level_choice()
