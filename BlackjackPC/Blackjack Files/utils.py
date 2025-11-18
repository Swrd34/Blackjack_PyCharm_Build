from time import sleep

def calc_hand(values):
    """Calculates the total value of a hand"""
    total = sum(values)
    if 1 in values and total + 10 <= 21: #An hour of insanity in just 1 line of code. Sigh.
        total += 10
    return total

def load():
    """A function for slowing things down a bit"""
    for i in range(3):
        print(".", end="")
        sleep(0.8)
    print("\n")

def get_user_input(choice_list: list[str], dev_cmds=False):
    """Checks if user input matches given parameters and loops till it does"""
    user_choice = (input().lower()).replace(" ", "") #Keeps user input not case-sensitive and removes whitespace
    if user_choice == "dev_cmds":
        print("Dev cmds enabled.")
    while user_choice not in choice_list:
        print(f"Invalid input. Try Again. Your choice: {user_choice}")
        user_choice = (input().lower()).replace(" ", "")
    return user_choice

def main_menu():
    """Prints main menu"""
    print("\033[97mWelcome to Swrd's BlackJack Sim! Have fun!\n\033[97m")
    print("Where would you like to go?")
    print(">Play Game\n"
          ">About\n"
          
          ">Exit\n")

def about():
    """About section"""
    print("This is a little blackjack game I made to get some experience with programming in python! I hope you enjoy playing it as much as I enjoyed making it!")