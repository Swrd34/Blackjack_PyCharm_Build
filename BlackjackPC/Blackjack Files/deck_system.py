import random


import globals
import utils

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
        pulled_card_name1, pulled_card_val1 = pull_card()# Pulls first card. Unpacks the tuple made in pull_Card so that the name/value can be outputted independently
        pulled_card_name2, pulled_card_val2 = pull_card() #Pulls second card

        globals.cards.extend(list((pulled_card_name1, pulled_card_name2))) #Extend here to add one element at a time so that we don't have any nested lists
        globals.card_vals.extend(list((pulled_card_val1,pulled_card_val2))) #Same for card value
        return globals.cards, globals.card_vals

def hit():
    """Adds card to player hand"""
    card_draw_name, card_draw_val = pull_card() #Pulls card, unpacks tuple.
    print(f"You drew: {card_draw_name}")
    globals.cards.append(card_draw_name) #Appends a card to the global hand variable
    globals.card_vals.append(card_draw_val) #Appends a card value to the global hand vals variable
    return card_draw_name

def stand():
    pass

def display_hand():
    print("You have the cards: ")
    globals.hand_val = utils.calc_hand(globals.card_vals)
    for card in globals.cards:
        print(card)
    print(f"Their values' total to: {globals.hand_val}")


"""
-------------------------------------------------Debug Functions:-------------------------------------------------------
"""

def deck_count():
    """Count Cards in the deck"""
    print("Cards left: ", len(deck))

def clear_deck():
    """Clears all elements in deck"""
    deck.clear()
    return 0

def deal_all_cards():
    """Deals all cards in the deck"""
    while len(deck) != 0 :
        deal_cards()

def give_card(x):
    """Gives card by dict value"""
    if x > (len(deck)-1):
            print("Out of range")
    else:
        deck_card_name = list(deck.keys())
        deck_card_value = list(deck.values())
        deck.pop(deck_card_name[x])
        globals.cards.append(deck_card_name[x])
        globals.card_vals.append(deck_card_value[x])
        return deck_card_name[x], deck_card_value[x]

#








