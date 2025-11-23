import time
import dealer_system
import utils
import deck_system
import globals

def main():
    """Handles all function calling"""
    while True:
        utils.clear_console()
        utils.main_menu()

        choice = utils.get_user_input(["exit", "playgame", "about"])

        if choice == "playgame":
            start_game()
            utils.end_game_menu()
            choice = utils.get_user_input(["replay", "mainmenu", "exit"])

            if choice == "replay":
                start_game()
            elif choice == "mainmenu":
                break
            else:
                utils.clear_console()
                print("Thanks for playing!")
                time.sleep(2)
                quit()


        elif choice == "about":
            utils.about()

        elif choice == "exit":
            break
    utils.clear_console()
    print("Thanks for playing!")
    time.sleep(2)
    input() # wait
    quit()




def start_game():
    """Starts game"""
    utils.clear_console()
    print("Dealing cards", end="")
    utils.load(.5)

    # Setting all the globals to their default vales
    globals.player_card_names.clear()
    globals.player_card_vals.clear()
    globals.dealer_card_names.clear()
    globals.dealer_card_vals.clear()

    deck_system.deal_cards() # Deal first 2 cards to dealer and player


    globals.player_hand_val = utils.calc_hand(globals.player_card_vals) #Calc Hand Value
    globals.dealer_hand_val = utils.calc_hand(globals.dealer_card_vals)

    dealer_system.display_hand_hidden()
    print("\n")
    utils.load(.5)
    print("\n")
    deck_system.display_hand()

    if globals.player_hand_val == 21 and globals.dealer_hand_val != 21: #Check if initial hand is already 21
        print("\n\nBlackjack! You win!")
        return

    elif globals.player_hand_val == 21 and globals.dealer_hand_val == 21: #Check if initial hand is already 21 and dealer has 21
            print("\n\nPush. Both player and dealer have 21.")
            return



    game_state() # Starting gameplay loop

def game_state():
    """."""
    while globals.player_hand_val < 21 and globals.player_hand_val != 21: #While player has not lost or won
        print("\n\nWould you like to hit or stand?")
        choice = utils.get_user_input(["hit", "stand"])
        if choice == "hit":
            utils.clear_console()
            deck_system.hit()
            if globals.player_hand_val > 21: #If after hitting the player busts
                print("Bust! You went over 21.")
                input()
                return
            elif globals.player_hand_val == 21:
                print("Blackjack! You win!")
                input()
                return
        if choice == "stand":
            pass







main()