Hello!

I almost finished my project. I have only one issue I can't overcome. I spent hours observing my code on the python visualizer, and I know where the problem lies, but I don't know how to solve it: namely, how to keep a countrol count in a subordinate fuction that refers back to a higher function from resetting every time the program comes back to that function.

My code now works for all cases of correct answers. 

As you will see in the code, this is the structure:

1. level_choice() 
2. start_game(ques,ans)
3. game(filled_rhyme,ans,counter,chances)
4. answer_check (user_answer,ans)

Function start_game() includes the global counter that controls the route through each question blank, and correct answer.
It also includes the counter for wrong answers, which ends up giving the user 5 chances for the whole game, not per question.

My 

