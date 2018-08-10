# Random quiz 
# define the function
def main():
    print(" " * 20 + 'Multiple Choice Question')
    print(' ' * 25 + 'Total marks = 10')
    print(' ' * 25 + 'Passed marks = 7')
    print('-' * 50)
    
    # import random module to randomize the question answer
    import random
    
    count = 0

    # Make a dictionary to containing the data
    mydata = {'Assam' : 'Dispur', 'West Bangle' : 'Kolkata', 'Sikkim' : 'Gantak', 'Bihar' : 'Patna',
            'Gujrat' : 'Ahmedabad', 'Karnatak' : 'Banglore', 'Kerela' : 'Trivandam', 'Tamilnadu' : 'Chennai',
            'Nagaland' : 'Kohima', 'Himachal Pradesh' : 'Shimla', 'J&K' : 'Kashir', 'Rajasthan' : 'Jaipur'}

    states = list(mydata.keys())
    random.shuffle(states)

    # Get the correct and wrong answer
    for i in range(10):
        # Get the correct answer
        correctAnswer = mydata[states[i]]
        # Get the wrong asnwer by deleting the correct answer
        wrongAnswers = list(mydata.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # collect any three wrong answer from the wrong answer list
        wrongAnswers = random.sample(wrongAnswers, 3)
        # make a answeroption list by adding wrong answer and correct answeer
        answerOptions = wrongAnswers + [correctAnswer]
        # randmize the answer option so that every time correct answer will not be the last option
        random.shuffle(answerOptions)
        # Ask the question
        print("{}. What is the capital of ".format(i+1) + states[i] +"? ")
        # Give the answer options
        for j in range(4):
            print("{}. {}".format('ABCD'[j], answerOptions[j]))
        # Ask the user to choose the correct answer
        # if the answer is correct then print correct asnwer and add 1 to count every time 
        # to calculate the number of correct answer given by the user
        # else print wrong answer
        answer = input().upper()
        if answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D':
            if answer == "{}".format('ABCD'[answerOptions.index(correctAnswer)]):
                print("Correct Answer\n")
                count += 1
            else:
                print("Wrong Answer\n")
        else:
            # if the user choose a option that is beyond the A-D then print invalid option
            print("Invalid Option, choose a correct Option\n")

    print("You have given {} correct answer".format(count))
    if count >= 7:
        print("Congratualtion!, You have passed")
    else:
        print("You Failed, good luck next time")

if __name__ == '__main__':
    main()
