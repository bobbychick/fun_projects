import random


def guessing_game(x):
    # random.seed()
    num = random.randint(1, x)

    guess = 0
    while guess != num:
        guess = int(input(f"Guess the number between 1 and {x}: "))

        if guess > num:
            print("Too high!")
        elif guess < num:
            print("Too low!")

    print(f"You guessed right, it was {num}!")


def computer_guess(x):

    usernum = int(input("Your secret number: "))

    while usernum > x or usernum < 1:
        usernum = int(input(f"Enter a number between 1 and {x}: "))

    compnum = random.randint(1, x)
    upper = x
    lower = 1

    while compnum != usernum:

        if compnum > usernum:
            print(f"Computer guessed {compnum}, too high!")
            if upper >= compnum:
                upper = compnum - 1
                # print(f"upper is {upper}")
            compnum = random.randint(lower, upper)
        elif compnum < usernum:
            print(f"Computer guessed {compnum}, too low!")
            if lower <= compnum:
                lower = compnum + 1
                # print(f"lower is {lower}")
            compnum = random.randint(lower, upper)

    print(f"The computer guessed correctly: {compnum}, the number was also {usernum}!")


# guessing_game(10)
computer_guess(1000)
