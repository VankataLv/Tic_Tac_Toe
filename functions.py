import random


def name_validity(name) -> bool:
    """This function will check if the user has typed a valid name. If not, it will ask the user again until he gives a valid name."""
    validity = name.isalpha()
    if not validity:
        print(f"> Your name probably contains ONLY letters.")
    if len(name) < 2:
        print(f"> Your name is probably longer than 1 letter.")
        validity = False
    if not validity:
        print("> You can try again.")
    return validity


def current_board(board) -> None:
    """Prints the current state of the board"""
    print("> Here is the current state of the board.")
    print(f'|---|---|---|\n'
          f'| {board[1]} | {board[2]} | {board[3]} |\n'
          f'|---|---|---|\n'
          f'| {board[4]} | {board[5]} | {board[6]} |\n'
          f'|---|---|---|\n'
          f'| {board[7]} | {board[8]} | {board[9]} |\n'
          f'|---|---|---|')


def player_turn(user: str, board: list, valid_choices: list):
    """Check's if the user has made a valid turn and returns the new board situation."""
    player_choice = input("> ")  # get player input/choice
    while True:
        if player_choice in valid_choices:  # check is it in range 1-9 string!!!
            player_choice = int(player_choice)
            if board[player_choice] == "X" or board[player_choice] == "O":  # is the player choice already taken
                print(f'> Position {player_choice} is already taken! Please pick again!')
                continue
            else:  # VALID choice
                board[player_choice] = "X"
                break
        else:
            print(f'> {user}, please pick a number from 1 to 9, only!')
            player_choice = input("> ")
            continue


def board_full_check(board: list) -> bool:
    """Check if all position in the board are full"""
    full_board = True
    for index in range(1, 10):
        if board[index] == "O" or board[index] == "X":
            continue
        else:
            full_board = False
            break
    return full_board


def is_winner(board: list, win_lose_draw: bool, user_wins: int, computer_wins: int, total_games_played: int, user: str):
    if (board[1] == board[2] == board[3] == "X") or \
            (board[4] == board[5] == board[6] == "X") or \
            (board[7] == board[8] == board[9] == "X") or \
            (board[1] == board[4] == board[7] == "X") or \
            (board[2] == board[5] == board[8] == "X") or \
            (board[3] == board[6] == board[9] == "X") or \
            (board[1] == board[5] == board[9] == "X") or \
            (board[3] == board[5] == board[7] == "X"):
        win_lose_draw = True
        user_wins += 1
        total_games_played += 1
        print(f"> ----- Congratulations, {user}, you WIN! -----")
    elif (board[1] == board[2] == board[3] == "O") or \
            (board[4] == board[5] == board[6] == "O") or \
            (board[7] == board[8] == board[9] == "O") or \
            (board[1] == board[4] == board[7] == "O") or \
            (board[2] == board[5] == board[8] == "O") or \
            (board[3] == board[6] == board[9] == "O") or \
            (board[1] == board[5] == board[9] == "O") or \
            (board[3] == board[5] == board[7] == "O"):
        win_lose_draw = True
        computer_wins += 1
        total_games_played += 1
        print(f"> ----- Sorry, {user}, computer wins this one! -----")
    return win_lose_draw, user_wins, total_games_played, computer_wins


def ai_turn(board: list):
    while True:
        ai_pick = random.randint(1, 9)
        if board[ai_pick] == "X" or board[ai_pick] == "O":
            continue
        else:
            board[ai_pick] = "O"
            print(f"> Computer picks: {ai_pick}")
            break
