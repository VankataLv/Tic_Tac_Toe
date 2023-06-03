import functions
# ------------- TIC-TAC-TOE by Vankata_Lv -------------
user_wins = 0
computer_wins = 0
draws = 0
total_games_played = 0
board = [el for el in range(10)]
valid_choices = [str(el) for el in range(1, 10)]
win_lose_draw = False
user_choice_to_play = True
print("______________________________________________")
print("> Dear player, welcome to my Tic-Tac_Toe game!")
while True:
    user_name = input("> What is your name? \n> ")
    valid_name = functions.name_validity(user_name)             # to check if the name is real
    if valid_name:
        user_name = user_name.capitalize()
        break

print(f"> Hello {user_name}!\n> Let's play a game!, you will be with X symbol")
while user_choice_to_play:
    while not win_lose_draw:
        functions.current_board(board)
        print(f'> {user_name}, please make your move! Pick a number from 1 to 9 and then press "enter"!')
        functions.player_turn(user_name, board, valid_choices)
        functions.current_board(board)
        functions.board_full_check(board)
        win_lose_draw, user_wins, total_games_played, computer_wins = functions.is_winner(board, win_lose_draw, user_wins, computer_wins, total_games_played, user_name)
        if win_lose_draw:
            break
        functions.ai_turn(board)
        win_lose_draw, user_wins, total_games_played, computer_wins = functions.is_winner(board, win_lose_draw, user_wins, computer_wins, total_games_played, user_name)
        if win_lose_draw:
            break

    print('> Do you want to play again? Type "y" or "n".')
    user_choice_to_play = input("> ").lower()
    while True:
        if user_choice_to_play == "n":
            print('> Thank you for playing!')
            user_desire_to_play = False
            break
        elif user_choice_to_play == "y":
            print("> Excellent, let's play again!")
            break
        else:
            print('> Please try again! Do you want to play another game? Type "y" or "n".')
            continue

print(f"Goodbye {user_name}!")
