import deck_system
import utils
import globals

def display_hand_hidden():
    """Initial dealer hand hidden"""
    globals.player_hand_val = utils.calc_hand(globals.player_card_vals)  # Calc Hand Value
    print("Dealer is showing: ")
    print(f"{globals.dealer_card_names[0]} and ?")
    print(f"Their values' total to: ?")

def display_hand_reveal():
    """Reveals dealer cards"""
    globals.player_hand_val = utils.calc_hand(globals.player_card_vals)  # Calc Hand Value
    print("Dealer cards are: ")
    print(f"{globals.dealer_card_names[0]} and {globals.dealer_card_names[1]}")
    print(f"Their values' total to: {globals.dealer_hand_val}")

def hit():
    """Adds card to dealer hand"""
    card_draw_name, card_draw_val = deck_system.pull_card()  # Pulls card, unpacks tuple.
    globals.dealer_card_names.append(card_draw_name)  # Appends a card to the global hand variable
    globals.dealer_card_vals.append(card_draw_val)  # Appends a card value to the global hand vals variable

    globals.dealer_hand_val = utils.calc_hand(globals.dealer_card_vals)

    print(f"Dealer drew: {card_draw_name}")
    print(f"Dealer's new total value is: {globals.dealer_hand_val}")
    return card_draw_name

