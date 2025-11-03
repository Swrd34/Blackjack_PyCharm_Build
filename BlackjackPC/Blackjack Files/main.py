import deck_system
import utils
import globals


def main():
    """Main menu"""
    print("\033[97mWelcome to Swrd's BlackJack Sim! Have fun!\n\033[97m")
    print("Where would you like to go?")
    print(">Play Game\n"
          ">About\n"
          ">Exit\n")
    choice = (input().lower()).replace(" ", "")

    while choice not in ["playgame", "about", "exit"]:
        print("Invalid input. Try Again.")
        choice = input()

    if choice == "exit":
        quit()

    elif choice == "playgame":
        start_game()


    elif choice == "about":
        about()
        pass


def about():
    """About function"""
    print("This is a little blackjack game I made to get some experience with programming in python! I hope you enjoy playing it as much as I enjoyed making it!")

    main()


def start_game():
    print("Dealing cards", end="")

    utils.load()

    globals.cards = []
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
        choice = (input().lower()).replace(" ", "")
        while choice not in ["hit", "stand"]:
            print("Invalid input. Try Again.")
            choice = input()
        if choice == "hit":
            deck_system.hit()
        else:
            deck_system.stand()

    deck_system.deal_cards()
    deck_system.display_hand()


main()