from random import randint


def check_answer(number):
    print("Welcome to the number guessing game")
    print("Computer has chosen a number between 1-100. GUESS IT 👍")
    print("Easy --> 15 Chances || Medium --> 10 Chances || Hard --> 5 Chances")
    a = input("Choose 'easy' mode or 'medium' mode or 'hard' mode: ")

    if a.lower() == "easy":
        n = 15
    elif a.lower() == "medium":
        n = 10
    elif a.lower() == "hard":
        n = 5
    else:
        n = 15
        print("So Sorry! You have not entered a valid statement!! We automatically took the input as 'easy'")

    for i in range(n):
        guess = int(input("Make a guess: "))
        if i+1<n:
            if number<guess:
                if guess-number>10:
                    print(f"The number {guess} is TOO HIGH. Guess again")
                    print(f"You have {n-i-1} chances remaining")
                elif guess-number<=10:
                    print(f"The number {guess} is HIGH. Guess again")
                    print(f"You have {n-i-1} chances remaining")
            elif number>guess:
                if number-guess>10:
                    print(f"The number {guess} is TOO LOW. Guess again")
                    print(f"You have {n-i-1} chances remaining")
                if number-guess<=10:
                    print(f"The number {guess} is LOW. Guess again")
                    print(f"You have {n-i-1} chances remaining")
            elif number==guess:
                print("You have guess it CORRECTLY!! Congratulations :)")
                break
        else:
            print("So Sorry!! You are out of chances. Please try again next time :)")
    c = input("Do you want to play again?    Type 'yes' or 'no' \n")
    if c == 'yes':
        print("")
        check_answer(number)
    else:
        print("Thank You for using our game :)")
        exit()



number = randint(1,100)
check_answer(number)
