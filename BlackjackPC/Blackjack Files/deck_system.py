import random
import globals
import utils
import colors as c
deck = {"♥A": 1, "♦A": 1, "♣A": 1, "♠A": 1,  #Full deck of cards
        "♥2": 2, "♦2": 2, "♣2": 2, "♠2": 2,
        "♥3": 3, "♦3": 3, "♣3": 3, "♠3": 3,
        "♥4": 4, "♦4": 4, "♣4": 4, "♠4": 4,
        "♥5": 5, "♦5": 5, "♣5": 5, "♠5": 5,
        "♥6": 6, "♦6": 6, "♣6": 6, "♠6": 6,
        "♥7": 7, "♦7": 7, "♣7": 7, "♠7": 7,
        "♥8": 8, "♦8": 8, "♣8": 8, "♠8": 8,
        "♥9": 9, "♦9": 9, "♣9": 9, "♠9": 9,
        "♥10": 10, "♦10": 10, "♣10": 10, "♠10": 10,
        "♥J": 10, "♦J": 10, "♣J": 10, "♠J": 10,
        "♥Q": 10, "♦Q": 10, "♣Q": 10, "♠Q": 10,
        "♥K": 10, "♦K": 10, "♣K": 10, "♠K": 10}


def pull_card():
    """Pulls a random card from the deck without changing the amount of values in deck. This returns a tuple"""
    deck_card_name = list(deck.keys()) # x Converts deck.keys to a list and assigns it to deckCardName
    deck_card_value = list(deck.values())  # Converts deck.values to a list and assigns it to deckCardValue
    x = random.randint(0,len(deck)-1) #Range between 0 and the amount of cards in deck
    deck.pop(deck_card_name[x])
    return deck_card_name[x], deck_card_value[x] #Return the card name and card value (Key and value pair)

def deal_cards():
    """Prints card to player screen and removes the card from the deck"""
    if len(deck) == 0 : # Check if deck is empty
        print("All cards gone.")
        return None
    else:
        #For player
        pulled_card_name1, pulled_card_val1 = pull_card()# Pulls first card. Unpacks the tuple made in pull_Card so that the name/value can be outputted independently
        pulled_card_name2, pulled_card_val2 = pull_card() #Pulls second card

        #For dealer
        pulled_card_name3, pulled_card_val3 = pull_card()
        pulled_card_name4, pulled_card_val4 = pull_card()

        globals.player_card_names.extend(list((pulled_card_name1, pulled_card_name2))) #Extend here to add one element at a time so that we don't have any nested lists
        globals.player_card_vals.extend(list((pulled_card_val1,pulled_card_val2))) #Same for card value

        globals.dealer_card_names.extend(list((pulled_card_name3,pulled_card_name4)))
        globals.dealer_card_vals.extend(list((pulled_card_val3, pulled_card_val4)))  # Same for card value


        return globals.player_card_names, globals.player_card_vals

def hit():
    """Adds card to player hand"""
    print("Hitting", end="")
    utils.load(0.5)
    card_draw_name, card_draw_val = pull_card() #Pulls card, unpacks tuple.
    globals.player_card_names.append(card_draw_name)  # Appends a card to the global hand variable
    globals.player_card_vals.append(card_draw_val)  # Appends a card value to the global hand vals variable

    globals.player_hand_val = utils.calc_hand(globals.player_card_vals)

    print(f"You drew: {card_draw_name}")
    print(f"Your new total value is: {globals.player_hand_val}")
    return card_draw_name

def stand():
    """Player stands"""
    print("Standing", end="")
    utils.load(0.5)
    utils.clear_console()

def display_hand():
    """Displays player hand"""
    globals.player_hand_val = utils.calc_hand(globals.player_card_vals) #Calc Hand Value
    print(f"You have the cards: ")
    print(f"{globals.player_card_names[0]} and {globals.player_card_names[1]}")
    print(f"Their values' total to: {globals.player_hand_val}")

def reset_deck():
    """Resets the deck back to its original state"""
    global deck
    deck = {"♥A": 1, "♦A": 1, "♣A": 1, "♠A": 1,  #Full deck of cards
        "♥2": 2, "♦2": 2, "♣2": 2, "♠2": 2,
        "♥3": 3, "♦3": 3, "♣3": 3, "♠3": 3,
        "♥4": 4, "♦4": 4, "♣4": 4, "♠4": 4,
        "♥5": 5, "♦5": 5, "♣5": 5, "♠5": 5,
        "♥6": 6, "♦6": 6, "♣6": 6, "♠6": 6,
        "♥7": 7, "♦7": 7, "♣7": 7, "♠7": 7,
        "♥8": 8, "♦8": 8, "♣8": 8, "♠8": 8,
        "♥9": 9, "♦9": 9, "♣9": 9, "♠9": 9,
        "♥10": 10, "♦10": 10, "♣10": 10, "♠10": 10,
        "♥J": 10, "♦J": 10, "♣J": 10, "♠J": 10,
        "♥Q": 10, "♦Q": 10, "♣Q": 10, "♠Q": 10,
        "♥K": 10, "♦K": 10, "♣K": 10, "♠K": 10}
