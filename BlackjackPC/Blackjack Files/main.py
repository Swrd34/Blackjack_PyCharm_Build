import utils
import deck_system
import globals


def main():
    utils.main_menu()

    choice = utils.get_user_input(["exit", "playgame", "about"])

    while choice != "playgame" or choice != "exit":
        if choice == "exit":
            quit()

        elif choice == "playgame":
            start_game()


        elif choice == "about":
            utils.about()
            pass

        choice = utils.get_user_input(["exit", "playgame", "about"])
    print("End of main")
    quit()




def start_game():
    """Starts game"""
    print("Dealing cards", end="")

    utils.load()

    globals.cards = [] #Setting all the globals to their default vales
    globals.card_vals = []
    globals.win_flag = False
    globals.lose_flag = False

    deck_system.deal_cards() # Deal first 2 cards
    deck_system.display_hand()

    game_state() # Starting gameplay loop

def game_state():
    """Function that handles the loop of gameplay until a lose or a win condition is hit."""
    utils.load()
    while globals.win_flag != True and globals.lose_flag != True:
        print("Would you like to hit or stand?")
        choice = utils.get_user_input(["hit", "stand"])
        if choice == "hit":
            deck_system.hit()
        else:
            deck_system.stand()

    deck_system.deal_cards()
    deck_system.display_hand()

start_game()