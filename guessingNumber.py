import random
print("Welcom to Guess A Number!")
max_number = input("Choose a number as your upper range: ")
print("Your number range is from 0 to ", max_number)

if max_number.isdigit():
    max_number = int(max_number)
    if max_number <= 0:
        print("Enter a number greater than 0")
        quit()
else:
    print("Enter a numeric value.")
    quit()

random_number = random.randint(0, max_number)
no_of_guesses = 0

while True:
    no_of_guesses += 1
    user_guess = input("Enter your guess from your range: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a valid value.")
        continue
    if user_guess == random_number:
        print("You are right:)")
        break
    elif user_guess < random_number:
        print("You are below")
    else:
        print("You are above.")
print("You got it in ", no_of_guesses, "attempts.")

# print(random_number)
