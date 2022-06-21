import random

mydict = {1: "r", 2: "p", 3: "s"}


def print_func(player, computer, win):
    win_stat_str = "You win" if win else "You lose"
    print(f"Computer played {computer}, you played {player}. " + win_stat_str)


def main(win_score):

    comp_score = 0
    my_score = 0

    while comp_score < win_score and my_score < win_score:

        i = random.randint(1, 3)
        comp = mydict[i]

        print(comp_score, my_score, win_score)

        my_move = input("r, p, or s? ").lower()

        if comp == my_move:
            print(f"You both played {comp}, draw!")

        if my_move == "r":
            if comp == "s":
                print_func(my_move, comp, True)
                my_score += 1
            if comp == "p":
                print_func(my_move, comp, False)
                comp_score += 1

        if my_move == "p":
            if comp == "s":
                print_func(my_move, comp, False)
                comp_score += 1
            if comp == "r":
                print_func(my_move, comp, True)
                my_score += 1

        if my_move == "s":
            if comp == "r":
                print_func(my_move, comp, False)
                comp_score += 1
            if comp == "p":
                print_func(my_move, comp, True)
                my_score += 1

    if my_score == win_score:
        print("You win!")
    else:
        print("Computer wins!")


main(3)
