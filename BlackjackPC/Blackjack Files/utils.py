from time import sleep
import os


def calc_hand(values):
    """Calculates the total value of a hand"""
    total = sum(values)
    if 1 in values and total + 10 <= 21: #An hour of insanity in just 1 line of code. Sigh.
        total += 10
    return total

def load(time_to_wait):
    """A function for slowing things down a bit"""
    for i in range(3):
        print(".", end="")
        sleep(time_to_wait)
    print("\n")

def get_user_input(choice_list: list[str], dev_cmds=False):
    """Checks if user input matches given parameters and loops till it does"""
    user_choice = (input().lower()).replace(" ", "") #Keeps user input not case-sensitive and removes whitespace
    if user_choice == "devcmds":
        print("Dev cmds enabled.")
    while user_choice not in choice_list:
        print(f"Invalid input. Try Again. Your choice: {user_choice}")
        user_choice = (input().lower()).replace(" ", "")
    return user_choice

def main_menu():
    """Prints main menu"""
    clear_console()
    print("\033[97mWelcome to Swrd's BlackJack Sim! Have fun!\n\033[97m")
    print("Where would you like to go?")
    print(">Play Game\n"
          ">About\n"
          ">Exit\n")


def about():
    """About section"""
    clear_console()
    print("American blackjack made with <3 by Swrd34")
    input("\n\n\nPress enter to return.")


def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')

def end_game_menu():
    """Ask player if they would like to exit, replay, or go back to main menu"""
    print(">Replay\n"
          ">Main Menu\n"
          ">Exit\n")
