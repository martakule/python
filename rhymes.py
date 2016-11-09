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
# It takes user input, transforms it into the index from the levels list, and keeps using that
# number to pull the correct set of questions and answers to call in the start_game() function.
# Before it calls the function, it welcomes the user to the selected level and gives the
# number of allowed wrong answers and the word to terminate the game at any point.
def level_choice():
	choice = raw_input("Pick a level by typing easy, medium, or hard.\n")
	if choice.lower() not in levels:
		print "\n*****\n\nInvalid input.\n"
		return level_choice()
	else:
		choice=levels.index(choice)
		print "\n*****\n\nYou've picked level " + levels[choice] + "! \nComplete the rhyme below one word at a time.\nYou will have " + str(wrong_limit) + " tries for each question\nIf you want to stop the game at any time, just type in " + safe_word + ".\nGood luck!\n\n*****\n"
		return start_game (questions[choice],answers[choice])	

# This function basically only stores values that cannot be stored in the next function, game().
# This is because game() includes the case of wrong answer that call game() again.
# So when these values aren't outside the function, they reset with every new call of game().
# If you know a way to solve this problem without setting up global values, please show me.
# Otherwise, if this is a valid solution, please tell me too. I'm a python noob.
# Anyway, this function assigns the level's appropriate poem to value rhyme; starts a counter to
# control the traversing through the questions and answers; and assigns the number of allowed
# wrong anwers to value chances. Then it calls game().
def start_game(ques,ans):
	global rhyme
	rhyme=ques	
	global counter
	counter=0
	global chances
	chances=wrong_limit
	return game (rhyme,ans,counter,chances)
	
# This function takes the poem, counter, and number of allowed wrong answers assigned in start_game().
# It also takes answers from the original list, through the functions above.
# It first prints the poem woth blanks. It then asks for user's answer through input.
# It calls function answer_check that takes that input, the right answer, and the safe word.
# For a correct answer, and it replaces the blank with the right answer from the list (to maintain 
# ccorrect ase/capitalization).
# For a wrong answer, it subtracts one remaining allowed wrong answer and checks for their number.
# If it's 0, it prints game over and quits. If it's more, it calls wrong_answer_countdown().
# It then adds one to the controlling counter. If it equals the length of the blanks list, it completes
# the game.
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
# for 2 and 1 tries left. The total number of tries is a variable (the maximum can be anything),
#so I set different sentences for only the last two.
def wrong_answer_countdown(chances):
	if chances > wrong_limit-(wrong_limit-2):
		print "\n*****\n\nTry again! You have " +str(chances) + " more tires!\n"
	if chances == wrong_limit-(wrong_limit-2):
		print "\n*****\n\nGive it a think! You have only " +str(chances) + " more tires!\n"
	if chances == wrong_limit-(wrong_limit-1):
		print "\n*****\n\nMake this count! This is your " +str(chances) + " last try!\n"
		
# This function takes the user's answer and checks it against the provided answers, ignoring case.
# It also takes the safe word -- if the user's input equals it, it prints a farewell message and
# terminates the game. If the answer is correct, it prints a message in this effect and returns
# the True value to feed back to game(). Else, it returns False to trigger the wrong answer
# action in game().
def answer_check (user_answer,ans,safe_word):
	if user_answer.lower()==ans.lower():
		print "\nCorrect!\n"
		return True 
	if user_answer.lower()==safe_word.lower():
		print "\nAll right! We're stopping here. Thanks for playing!\n"
		quit()
	else:
		return False 
		
#These lines welcome the user to the game and fire off the first function.
print "\nWelcome to the Nursery Rhymes Quiz!"
level_choice()
