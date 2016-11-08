# Three strings of the text with blanks to fill in
questions = ["Twinkle, twinkle, little (1)_____,\nHow I wonder what you (2)_____!\nUp above the world so (3)_____,\nLike a diamond in the (4)_____.", "Tweedledum and Tweedledee\nAgreed to have a (1)_____;\nFor Tweedledum said (2)_____\nHad spoiled his nice new rattle.\nJust then flew down a monstrous (3)_____,\nAs black as a tar-barrel;\nWhich frightened both the heroes so,\nThey quite forgot their (4)_____.", "Tinker, (1)_____,\nSoldier, (2)_____,\nRich Man, (3)_____ Man,\nBeggar Man, (4)_____."]

# Three lists of answers
answers=[['star', 'are', 'high', 'sky'], ['battle', 'Tweedledee', 'crow', 'quarrel'], ['Tailor', 'Sailor', 'Poor', 'Thief']]

# A list of blanks
blanks=["(1)_____","(2)_____","(3)_____","(4)_____"]

levels=['easy','medium','hard']

#The number of allowed wrong aswers per question
wrong_limit=5

safe_word="stop"

# This function prompts the user to pick a level and loads the appropriate level's data from above.
def level_choice():
	choice = raw_input("Pick a level by typing easy, medium, or hard.\n")
	if choice.lower() not in levels:
		print "Invalid input.\n"
		return level_choice()
	else:
		choice=levels.index(choice)
		print print "\n*****\n\nYou've picked level " + levels[choice] + "! \nComplete the rhyme below one word at a time.\nYou will have " + str(wrong_limit) + " tries for each question\nIf you want to stop the game at any time, just type in " + safe_word + "\nGood luck!\n\n*****\n"
		filled_rhyme=questions[choice]
		global counter
		counter=0
		global chances
		chances=wrong_limit
		return game (filled_rhyme,answers[choice],counter,chances)	

# This function runs the game: loops through the blanks, verifies anwers, and fills the rhyme as answers come. 
# It also ends the game when the counter hits the last number.
# Now it also handles the wrong answer, missing the counter per question and separate sentences.
def game(rhyme,ans,counter,chances):
	while counter<len(blanks):
		print "Now the rhyme reads like this:\n\n" + filled_rhyme
		user_answer=raw_input("\n*****\n\nWhat word replaces"+blanks[counter]+"?\n\n>")
		if answer_check (user_answer,ans[counter]) == True:
			chances=wrong_limit #Following advice on the forum, I added this to reset wrong answers for the whole game.
			filled_rhyme=filled_rhyme.replace((blanks[counter]),ans[counter])
		else:
			chances=chances-1
			if chances==0:
				print "*****\n\nGame over.\nThanks for playing!\n"
				quit()
			else:
				wrong_answer_countdown(chances) #And this simple print function doesn't use any counters, so it doesn't reset.
				return game(filled_rhyme,ans,counter,chances)
		counter+=1
	if counter==len(blanks):
		print filled_rhyme
		print "\n*****\n\nCongratulations! You completed the game.\nThanks for playing!"

# This function prints a different sentence for 2 and 1 tries left.
def wrong_answer_countdown(chances):
	if chances > wrong_limit-(wrong_limit-2):
		print "\n*****\n\nTry again! You have " +str(chances) + " more tires!\n"
	if chances == wrong_limit-(wrong_limit-2):
		print "\n*****\n\nGive it a think! You have only " +str(chances) + " more tires!\n"
	if chances == wrong_limit-(wrong_limit-1):
		print "\n*****\n\nMake this count! This is your " +str(chances) + " last try!\n"
		
# This function takes the user's answer and checks it against the provided answers, ignoring case.
def answer_check (user_answer,ans):
	if user_answer.lower()==ans.lower():
		print "\nCorrect!\n"
		return True 
	else:
		return False 
		
#These lines welcome the user to the game and fire off the first function.
print "\nWelcome to the Nursery Rhymes Quiz!"
level_choice()
