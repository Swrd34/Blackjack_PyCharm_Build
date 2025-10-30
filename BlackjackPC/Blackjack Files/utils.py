import globals

def calc_hand(hand: list[int]):
    """Calculates the total value of a hand"""
    sum = 0
    for card in hand:
        sum = card + sum
    print(f"Your cards are worth {sum}")
    return sum
