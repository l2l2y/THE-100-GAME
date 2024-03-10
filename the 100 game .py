player_scores = {'player_1': 0, 'player_2': 0}

# Main menu
while True:
    print(' THE 100 GAME ')
    print('MENU')
    print('1 - Start multiplayer game')
    print('2 - Quit game')
    choice = int(input('Ready or not ?!'))
    # Start multiplayer game
    if choice == 1:
        print('GMAE IS ON')
    # Quit game
    elif choice == 2:
        print('See you soon.')
        break
    # Invalid choice
    else:
        print('SORRY, invalid option')
# Game loop
    while True:
        # Get player names
        print('player 1, tell me your name:')
        player1 = input()
        print('player 2 , what about you ?')
        player2 = input()
        print('Well hey there, ' + player1 + ' and ' + player2 + ', and welcome to  (THE 100 GAME).')
        print('You will each take turns to choose a number between 1 and 10.')
        print('The first person to reach 100 is the winner.')
        print('GL,HF')

        # Game loop
        total_number = 0
        current_player = player1
        player_scores=0
        while total_number < 100:
         # Get number input from current player
           number_input = input(current_player + ', give me a number between 1 and 10.')
           number = int(number_input)
           # Check if number is valid
           if 1 <= number <= 10:
            # Update scores and display total
            total_number += number
            player_scores += number
            print("Got it, " + current_player + ' Here is the Total')
            print(total_number)

            # Check for winner
            if player_scores >= 100:
                print(current_player.capitalize() + " IS THE WINNER!!")
                break

            # Switch to other player
            current_player = player1 if current_player == player2 else player2
        # Invalid number
           else:
            print("Invalid number. Try again.")
            continue

    # Break game loop
        break