# Three strings of the text with blanks to fill in
easy_questions =  "Twinkle, twinkle, little (1)_____,\nHow I wonder what you (2)_____!\nUp above the world so (3)_____,\nLike a diamond in the (4)_____."

medium_questions = "Tweedledum and Tweedledee\nAgreed to have a (1)_____;\nFor Tweedledum said (2)_____\nHad spoiled his nice new rattle.\nJust then flew down a monstrous (3)_____,\nAs black as a tar-barrel;\nWhich frightened both the heroes so,\nThey quite forgot their (4)_____."

hard_questions = "Tinker, (1)_____,\nSoldier, (2)_____,\nRich Man, (3)_____ Man,\nBeggar Man, (4)_____."

# Three lists of answers
easy_answers=['star', 'are', 'high', 'sky']
medium_answers=['battle', 'Tweedledee', 'crow', 'quarrel']
hard_answers=['Tailor', 'Sailor', 'Poor', 'Thief']

# A list of blanks
blank_list=["(1)_____","(2)_____","(3)_____","(4)_____"]

#The number of allowed wrong aswers per question
wrong_limit=5

# This function prompts the user to pick a level and loads the appropriate level's data from above.
def level_choice():
	global level
	choice = raw_input("Pick a level by typing easy, medium, or hard.\n")
	level=choice
	if choice=="easy":
		return start_game(easy_questions, easy_answers)
	if choice=="medium":
		return start_game(medium_questions, medium_answers)
	if choice=="hard":
		return start_game(hard_questions, hard_answers)
	else:
		return level_choice()

# This function welcomes to a level and pulls the level's rhyme and answers. 
# It also contains the counter that controls the whole game.
# And the counter for wrong answers because I can't figure it out.
def start_game(ques,ans):
	print "\n*****\n\nYou've picked level " + level + "! \nComplete the rhyme below one word at a time.\nYou will have 5 tries for each answer\nGood luck!\n\n*****\n"
	global filled_rhyme
	filled_rhyme=ques	
	global counter
	counter=0
	global chances
	chances=wrong_limit
	game (filled_rhyme,ans,counter,chances)
	
# This function runs the game: loops through the blanks, verifies anwers, and fills the rhyme as answers come. 
# It also ends the game when the counter hits the last number.
# Now it also handles the wrong answer, missing the counter per question and separate sentences.
def game(filled_rhyme,ans,counter,chances):
	while counter<len(blank_list):
		print "Now the rhyme reads like this:\n\n" + filled_rhyme
		user_answer=raw_input("\n*****\n\nWhat word replaces"+blank_list[counter]+"?\n")
		if answer_check (user_answer,ans[counter]) == True:
			chances=wrong_limit #Following advice on the forum, I added this to reset wrong answers for the whole game.
			filled_rhyme=filled_rhyme.replace((blank_list[counter]),ans[counter])
		else:
			chances=chances-1
			if chances==0:
				print "Game over.\nThanks for playing!"
				quit()
			else:
				wrong_answer_countdown(chances) #And this simple print function doesn't use any counters, so it doesn't reset.
				return game(filled_rhyme,ans,counter,chances)
		counter+=1
	if counter==len(blank_list):
		print filled_rhyme
		print "\n*****\n\nCongratulations! You completed the game.\nThanks for playing!"

def wrong_answer_countdown(chances):
	if chances > wrong_limit-(wrong_limit-2):
		print "\nTry again!\nYou have " +str(chances) + " more tires!"
	if chances == wrong_limit-(wrong_limit-2):
		print "\nThink before you answer!\nYou have only " +str(chances) + " more tires!"
	if chances == wrong_limit-(wrong_limit-1):
		print "\nMake this count!\nThis is your " +str(chances) + " last try!"
		
#This function takes the user's answer and checks it against the provided answers, ignoring case.
def answer_check (user_answer,ans):
	if user_answer.lower()==ans.lower():
		print "\nCorrect!\n"
		return True 
	else:
		return False 
		
#These lines welcome the user to the game and fire off the first function.
print "\nWelcome to the Nursery Rhymes Quiz!"
level_choice()
