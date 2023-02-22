# Simple quiz demostrating a basic work flow of python usng if else.
print("Welcome to the quiz play!")
answer = input("Do you want to play? : ")
your_score = 0
# print(answer)
# lower method converts the string to lowercase
if answer.lower() == 'yes':
    print("Below are your 10 questions..")
    # for value in range(5):

    question1 = input("	Who is the father of Computer science? : ")
    if question1.lower() == 'charles babbage':
        print("That's right!!")
        your_score += 1
    else:
        print("Sorry! The right answer is Charles Babbage.")

    question2 = input("	Help Menu is available at which button? : ")
    if question2.lower() == 'start':
        print("That's right!!")
        your_score += 1
    else:
        print("Sorry! The right answer is 'Start'.")
        # Use of single and double quotes.

    question3 = input("Full form of LAN? : ")
    if question3.lower() == 'local area network':
        print("That's right!!")
        your_score += 1
    else:
        print("Sorry! The right answer is 'Local Area Network'.")

    question4 = input("What kind of memory is both static and non-volatile?: ")
    if question4.upper() == 'ROM':
        print("That's right!!")
        your_score += 1
    else:
        print("Sorry! The right answer is ROM.")

    question5 = input("	What kind of scheme is the HTTP protocol? : ")
    if question5.lower() == 'request/response':
        print("That's right!!")
        your_score += 1
    else:
        print("Sorry! The right answer is Request/Response.")
    print(f"Your score is : {your_score}")
    print("Your won by" + str((your_score/4)*100) + "%")
# this way of printing is knowns as formating string literals.

else:
    print("Thanks for coming:)")
    # quit() method exists the program.
    quit()
