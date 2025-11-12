from time import sleep

def calc_hand(values):
    """Calculates the total value of a hand"""
    total = sum(values)
    if 1 in values and total + 10 <= 21: #An hour of insanity in just 4 lines of code. Sigh.
        total += 10
    return total

def load():
    """A function for slowing things down a bit"""
    for i in range(3):
        print(".", end="")
        sleep(0.8)
    print("\n")
