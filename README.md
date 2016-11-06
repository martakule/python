Hello!

I almost finished my project. I have only one issue I can't overcome. I spent hours observing my code on the python visualizer, and I know where the problem lies, but I don't know how to solve it: namely, how to keep a countrol count in a subordinate fuction that refers back to a higher function from resetting every time the program comes back to that function.

My code now works for all cases of correct answers. 

As you will see in the code, this is the structure:

1. level_choice() 
2. start_game(ques,ans)
3. game(filled_rhyme,ans,counter,chances)
4. answer_check (user_answer,ans)

Function start_game() includes the global counter that controls the route through each question, blank, and correct answer.
It also includes the counter for wrong answers, which ends up giving the user 5 chances for the whole game, not per question.

My "wrong answer" message is aslo simplistic: "You have " +str(chances) + " more tires!"
It's the same for all number, even 1.
The model quiz for this project has a different sentence for each number of remianing tries.

The behaviour of the model quiz makes me think the treatment of wrong answers is enclosed in a separate function that maintains a counter and print different messages depending on the number of tries left.

I had initiall put my wrong-answer counter inside answer_check (user_answer,ans), which is subordintate to game(), and which refers back to game (). Something like this:

```def answer_check (user_answer,ans):
____if user_answer.lower()==ans.lower():
        print "\nCorrect!\n"
        return True 
    else:
        index=0
	while index<chances:
	    print "You have " +str(chances-1) + " more tires!"
	    return game(arguments)
	    index=index-1
	else:
	    print "Game over"
	    quit ()```

Now, the problem with all this is that whenever you answer the same question wrong the second time, the function answer_check () is called afresh and the index is ZERO again.

This is where I hit the wall.

Please give me a hint how to get out of this.

