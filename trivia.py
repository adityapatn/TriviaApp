questions = [{"q":"What are the answers for 1 + 1, 2 + 2, and 3 * 3?", "a1":"2", "a1pt":1, "a2":"4", "a2pt":1, "a3":"9", "a3pt":2},
             ]

score = 0
totalscore = 0
sayscore = True

intromsg = "\nEach question may contain one or several parts. Answers should be exact with correct capitalization, spelling, etc. Answers that are numbers should be written as digits, not words. Answers should be given in the order in which they are asked for. Press enter after answering each part. Questions that give options only accept the option letter as answers. Questions with [T/F] at the beginning require 'True' or 'False', 'T' or 'F', or '1' or '0' as answers. Good luck!\n"

tf = {True:True, 1:True, "1":True, "T":True, "True":True, "yes":True, "yeah":True, False:False, 0:False, "0":False, "F":False, "False":False, "no":False, "nah":False}

def start():
    print(intromsg)
    sayscore = input("[T/F] I would like to be shown my score after every question: ").strip()
    #print("sayscore: " + str(sayscore))
    sayscore = tf[sayscore]
    #print("sayscore: " + str(sayscore))
    qamount = int(input("How many questions in this set? "))
    if qamount > len(questions):
        print("That number of questions is too large. Defaulting to maximum number of questions allowed (" + str(len(questions)) + ").")
        qamount = len(questions)

    for i in range(len(questions)):
        ask(questions[i])

    print("You have reached the end of the question set.")
    print("Your score was " + str(score) + " out of " + str(totalscore) + " possible points, or " + str(round((score / totalscore) * 100, 2)) + "%.")
    again = input("[T/F] I would like to play again: ")
    again = tf[again]
    if again == True:
        start()
    else:
        print("Thanks for playing!")
        pass

def ask(question):
    global score
    global sayscore
    global totalscore
    q = question["q"]
    print(q)

    for i in range(int((len(questions[0]) - 1) / 2)):
        qpart = i + 1
        a = question["a" + str(qpart)]
        pts = question["a" + str(qpart) + "pt"]
        guess = input("")
        if (guess.strip() == a):
            score += pts
            if pts == 1:
                print("Correct. +1pt.")
            else:
                print("Correct. +" + str(pts) + "pts.")
        else:
            print("Incorrect.")
        totalscore += pts
        
    if sayscore == True:
        print("Your score is " + str(score) + " out of " + str(totalscore) + " possible points.")

#add congratulation message at the end, number of questions asked in the set