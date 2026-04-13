import random
import time


def choose_random_number():
    random_number = random.randint(1, 100)
    return random_number


# PLAYERS STATS
total_easy_attempts = 0
total_easy_wins = 0
total_easy_losses = 0
total_easy_games = 0

total_medium_attempts = 0
total_medium_wins = 0
total_medium_losses = 0
total_medium_games = 0

total_hard_attempts = 0
total_hard_wins = 0
total_hard_losses = 0
total_hard_games = 0

total_impossible_attempts = 0
total_impossible_wins = 0
total_impossible_losses = 0
total_impossible_games = 0


def track_stats(difficulty, attempts, result):
    global total_easy_attempts
    global total_easy_wins
    global total_easy_losses
    global total_easy_games

    global total_medium_attempts
    global total_medium_wins
    global total_medium_losses
    global total_medium_games

    global total_hard_attempts
    global total_hard_wins
    global total_hard_losses
    global total_hard_games

    global total_impossible_attempts
    global total_impossible_wins
    global total_impossible_losses
    global total_impossible_games

    if difficulty == "easy":
        total_easy_attempts += attempts
        total_easy_games += 1
        if result == "win":
            total_easy_wins += 1
        elif result == "loss":
            total_easy_losses += 1

    if difficulty == "medium":
        total_medium_attempts += attempts
        total_medium_games += 1
        if result == "win":
            total_medium_wins += 1
        elif result == "loss":
            total_medium_losses += 1

    if difficulty == "hard":
        total_hard_attempts += attempts
        total_hard_games += 1
        if result == "win":
            total_hard_wins += 1
        elif result == "loss":
            total_hard_losses += 1

    if difficulty == "impossible":
        total_impossible_attempts += attempts
        total_impossible_games += 1
        if result == "win":
            total_impossible_wins += 1
        elif result == "loss":
            total_impossible_losses += 1


def display_stats():
    print()

    print("Here are your statistics!")
    print()

    # EASY
    print("Easy Difficulty:")
    print("Games played: " + str(total_easy_games))
    print("Total Games won: " + str(total_easy_wins))
    print("Total Games lost: " + str(total_easy_losses))
    if total_easy_games == 0:
        print("Win/Loss: No games played!")
        print("Average attempts to end game: No games played!")
    else:
        print("Win/Loss: " + str(int((total_easy_wins / total_easy_games) * 100)) + "%")
        print("Average attempts to end game: " + (str(int(total_easy_attempts / total_easy_games))))

    print()

    # MEDIUM
    print("Medium Difficulty:")
    print("Games played: " + str(total_medium_games))
    print("Total games won: " + str(total_medium_wins))
    print("Total games lost: " + str(total_medium_losses))
    if total_medium_games == 0:
        print("Win/Loss: No games played!")
        print("Average attempts to end game: No games played!")
    else:
        print("Win/Loss: " + str(int((total_medium_wins / total_medium_games) * 100)) + "%")
        print("Average attempts to end game: " + (str(int(total_medium_attempts / total_medium_games))))

    print()

    # HARD
    print("Hard Difficulty:")
    print("Games played: " + str(total_hard_games))
    print("Total games won: " + str(total_hard_wins))
    print("Total games lost: " + str(total_hard_losses))
    if total_hard_games == 0:
        print("Win/Loss: No games played!")
        print("Average attempts to end game: No games played!")
    else:
        print("Win/Loss: " + str(int((total_hard_wins / total_hard_games) * 100)) + "%")
        print("Average attempts to end game: " + (str(int(total_hard_attempts / total_hard_games))))

    print()

    # Impossible
    print("Impossible Difficulty:")
    print("Games played: " + str(total_impossible_games))
    print("Total games won: " + str(total_impossible_wins))
    print("Total games lost: " + str(total_impossible_losses))
    if total_impossible_games == 0:
        print("Win/Loss: No games played!")
        print("Average attempts to end game: No games played!")
    else:
        print("Win/Loss: " + str(int((total_impossible_wins / total_impossible_games) * 100)) + "%")
        print("Average attempts to end game: " + (str(int(total_impossible_attempts / total_impossible_games))))

    print()

    go_back = input("Would you like to go back to the main menu? (y/n): ")
    if go_back.lower() == "y":
        print("Going back to the main menu...")
        time.sleep(3)
        print()
        main_menu()
    elif go_back.lower() == "n":
        print("Exiting game...")
        time.sleep(3)
        exit()


def explain_rules():
    print("The rules are simple:")
    time.sleep(1)
    print("First, I select a random number between 1-100")
    time.sleep(2)
    print("Then, you will choose any number between 1 and 100")
    time.sleep(3)
    print("Next, I will begin to give you hints on whether you need to guess higher or lower")
    time.sleep(4)
    print("Finally, we will repeat this process until you successfully choose the random number!")
    time.sleep(4)
    print(
        "I will also keep track of your attempted guesses and after each round you can select to see your average tries.")
    time.sleep(4)
    print()
    userinput = input("Enter X to go back to the main menu: ")
    if userinput.lower() == "x":
        print("Going back to the main menu...")
        time.sleep(3)
        print()
        main_menu()


def start_game():
    print()
    print("1. Easy (15)")
    print("2. Medium (10)")
    print("3. Hard (5)")
    print("4. Impossible (1)")
    selected_difficulty = int(input("Select an difficulty level (1/2/3/4): "))

    print()

    random_num = choose_random_number()
    game_attempts = 0
    current_guess = 0
    while current_guess != random_num:
        current_guess = int(input("Guess a number between 1 and 100: "))
        game_attempts += 1
        if current_guess == random_num:
            if selected_difficulty == 1:
                track_stats("easy", game_attempts, "win")
            if selected_difficulty == 2:
                track_stats("medium", game_attempts, "win")
            if selected_difficulty == 3:
                track_stats("hard", game_attempts, "win")
            if selected_difficulty == 4:
                track_stats("impossible", game_attempts, "win")
            print("You guessed correctly!")
            print()
            print("Your attempt count was: " + str(game_attempts))
            print()
            try_again = input("Do you want to try again? (y/n): ")
            if try_again.lower() == "y":
                print()
                print("Restarting game...")
                time.sleep(2)
                start_game()
            if try_again.lower() == "n":
                print()
                print("Taking you back to the main menu...")
                time.sleep(2)
                main_menu()
        elif current_guess > random_num:
            print("Guess Lower!")
            print()
        elif current_guess < random_num:
            print("Guess Higher!")
            print()

        if selected_difficulty == 1:
            if game_attempts >= 15:
                track_stats("easy", game_attempts, "loss")
                print("Too many attempts, you lose!")
                print()
                try_again = input("Do you want to try again? (y/n): ")
                if try_again.lower() == "y":
                    print()
                    print("Restarting game...")
                    time.sleep(2)
                    start_game()
                if try_again.lower() == "n":
                    print()
                    print("Taking you back to the main menu...")
                    time.sleep(2)
                    main_menu()
        if selected_difficulty == 2:
            if game_attempts >= 10:
                track_stats("medium", game_attempts, "loss")
                print("Too many attempts, you lose!")
                print()
                try_again = input("Do you want to try again? (y/n): ")
                if try_again.lower() == "y":
                    print()
                    print("Restarting game...")
                    time.sleep(2)
                    start_game()
                if try_again.lower() == "n":
                    print()
                    print("Taking you back to the main menu...")
                    time.sleep(2)
                    main_menu()
        if selected_difficulty == 3:
            if game_attempts >= 5:
                track_stats("hard", game_attempts, "loss")
                print("Too many attempts, you lose!")
                print()
                try_again = input("Do you want to try again? (y/n): ")
                if try_again.lower() == "y":
                    print()
                    print("Restarting game...")
                    time.sleep(2)
                    start_game()
                if try_again.lower() == "n":
                    print()
                    print("Taking you back to the main menu...")
                    time.sleep(2)
                    main_menu()
        if selected_difficulty == 4:
            if game_attempts >= 1:
                track_stats("impossible", game_attempts, "loss")
                print("Too many attempts, you lose!")
                print()
                try_again = input("Do you want to try again? (y/n): ")
                if try_again.lower() == "y":
                    print()
                    print("Restarting game...")
                    time.sleep(2)
                    start_game()
                if try_again.lower() == "n":
                    print()
                    print("Taking you back to the main menu...")
                    time.sleep(2)
                    main_menu()


def main_menu():
    print("Welcome to the number guessing game!")
    time.sleep(2)
    print("1. Start Game")
    print("2. Instructions")
    print("3. Stats")
    print("4. Quit")
    selected_option = int(input("Select an option (1/2/3/4): "))

    if selected_option == 2:
        explain_rules()
    if selected_option == 1:
        start_game()
    if selected_option == 4:
        print()
        print("Exiting...")
        time.sleep(2)
        exit()
    if selected_option == 3:
        display_stats()


main_menu()