import time
import dealer_system
import utils
import deck_system
import globals
import colors as c

def main():
    """Handles all function calling"""
    while True:
        utils.clear_console()
        utils.main_menu()

        choice = utils.get_user_input(["exit", "start", "about", "howtoplay"])

        if choice == "start":
            while choice != "mainmenu" and choice != "exit":
                start_game()
                utils.end_game_menu()
                choice = utils.get_user_input(["replay", "mainmenu", "exit"])

            if choice == "exit":
                utils.clear_console()
                print("Thanks for playing!")
                time.sleep(2)
                quit()

        elif choice == "howtoplay":
            utils.htp()

        elif choice == "about":
            utils.about()

        elif choice == "exit":
            utils.clear_console()
            print("Thanks for playing!")
            time.sleep(2)
            quit()




def start_game():
    """Starts game"""
    utils.clear_console()
    print(f"Dealing cards", end="")
    utils.load(.5)

    # Setting globals and deck to their default vales
    deck_system.reset_deck()
    globals.player_card_names.clear()
    globals.player_card_vals.clear()
    globals.dealer_card_names.clear()
    globals.dealer_card_vals.clear()

    deck_system.deal_cards() # Deal first 2 cards to dealer and player


    globals.player_hand_val = utils.calc_hand(globals.player_card_vals) #Calculate initial hand values
    globals.dealer_hand_val = utils.calc_hand(globals.dealer_card_vals)

    dealer_system.display_hand_hidden()
    print("\n")
    utils.load(.5)
    print("\n")
    deck_system.display_hand()

    if globals.player_hand_val == 21 and globals.dealer_hand_val != 21: #Check if initial hand is already 21
        print(f"{c.B_YELLOW}\n\nBlackjack! You win!{c.B_WHITE}")
        globals.player_wins += 1
        return

    elif globals.player_hand_val == 21 and globals.dealer_hand_val == 21: #Check if initial hand is already 21 and dealer has 21
            print(f"{c.B_BLUE}\n\nPush. Both player and dealer have 21.{c.B_WHITE}")
            return



    game_state() # Starting gameplay loop

def game_state():
    """Gameplay loop"""
    while globals.player_hand_val < 21: #While player has not lost or won
        print("\n\nWould you like to hit or stand?")
        choice = utils.get_user_input(["hit", "stand"])
        if choice == "hit":
            utils.clear_console()
            deck_system.hit()
            if globals.player_hand_val > 21: #If after hitting the player busts
                print(f"{c.B_RED}Bust! You went over 21.{c.B_WHITE}")
                globals.dealer_wins += 1
                input()
                return
            elif globals.player_hand_val == 21:
                print(f"{c.B_YELLOW}Blackjack! You win!{c.B_WHITE}")
                globals.player_wins += 1
                input()
                return
        if choice == "stand":
            utils.clear_console()
            deck_system.stand()
            break

    dealer_system.display_hand_reveal()
    utils.load(1.5)
    if globals.dealer_hand_val == 21:
        print(f"{c.B_RED}Dealer has 21! Dealer wins!{c.B_WHITE}")
        globals.dealer_wins += 1
        return

    while globals.dealer_hand_val < 17:
        utils.clear_console()
        print("Dealer hits", end="")
        utils.load(0.5)
        dealer_system.hit()
        if globals.dealer_hand_val > 21:
            print(f"{c.B_YELLOW}Dealer busts! Player wins!{c.B_WHITE}")
            globals.player_wins += 1
            return
        elif globals.dealer_hand_val == 21:
            print(f"{c.B_YELLOW}Dealer has blackjack! Dealer wins!{c.B_WHITE}")
            globals.dealer_wins += 1
            return
        utils.load(1.5)


    if globals.player_hand_val > globals.dealer_hand_val:
        print(f"{c.B_YELLOW}Player is closer to 21. Player wins!{c.B_WHITE}")
        globals.player_wins += 1
    elif globals.player_hand_val < globals.dealer_hand_val:
        print(f"{c.B_RED}Dealer is closer to 21. Dealer wins!{c.B_WHITE}")
        globals.dealer_wins += 1
    else:
        print(f"{c.B_BLUE}Both player and dealer hands are equal. Push.{c.B_WHITE}")



main()