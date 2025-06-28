# Create a basic quiz game that:
# Contains a list of 5–10 questions stored in a dictionary (or list of dicts).
# Asks the user each question and records their answers.
# At the end, displays:
# The user’s score (e.g., 7/10)
# Correct answers for any questions they got wrong

print("welcome to quiz game!!!")
dic={"question1":"answer1",
     "question2":"answer2",
     "question3":"answer3",
     "question4":"answer4",
     "question5":"answer5",
     "question6":"answer6",
     "question7":"answer7",
     "question8":"answer8",
     "question9":"answer9",
     "question10":"answer10"}
print("please answer the following question")
score=0
for key in dic:
    ans = input(f"what is the correct answer for {key} ")
    if ans == dic.get(key):
        print("correct")
        score+=1
    else:
        print("the correct answer is :" ,dic.get(key))
print(f"you have completed the quiz , you scored : {score}/10")


