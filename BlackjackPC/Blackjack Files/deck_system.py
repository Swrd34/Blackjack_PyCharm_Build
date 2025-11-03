import random
import globals

deck = {"Ace of Hearts": 1, "Ace of Spades": 1, "Ace of Clubs": 1, "Ace of Diamonds": 1,  #Full deck of cards
        "2 of Hearts": 2, "2 of Spades": 2, "2 of Clubs": 2, "2 of Diamonds": 2,
        "3 of Hearts": 3, "3 of Spades": 3, "3 of Clubs": 3, "3 of Diamonds": 3,
        "4 of Hearts": 4, "4 of Spades": 4, "4 of Clubs": 4, "4 of Diamonds": 4,
        "5 of Hearts": 5, "5 of Spades": 5, "5 of Clubs": 5, "5 of Diamonds": 5,
        "6 of Hearts": 6, "6 of Spades": 6, "6 of Clubs": 6, "6 of Diamonds": 6,
        "7 of Hearts": 7, "7 of Spades": 7, "7 of Clubs": 7, "7 of Diamonds": 7,
        "8 of Hearts": 8, "8 of Spades": 8, "8 of Clubs": 8, "8 of Diamonds": 8,
        "9 of Hearts": 9, "9 of Spades": 9, "9 of Clubs": 9, "9 of Diamonds": 9,
        "10 of Hearts": 10, "10 of Spades": 10, "10 of Clubs": 10, "10 of Diamonds": 10,
        "Jack of Hearts": 10, "Jack of Spades": 10, "Jack of Clubs": 10, "Jack of Diamonds": 10,
        "Queen of Hearts": 10, "Queen of Spades": 10, "Queen of Clubs": 10, "Queen of Diamonds": 10,
        "King of Hearts": 10, "King of Spades": 10, "King of Clubs": 10, "King of Diamonds": 10}


def pull_card():
    """Pulls a random card from the deck without changing the amount of values in deck. This returns a tuple"""
    deck_card_name = list(deck.keys()) # x Converts deck.keys to a list and assigns it to deckCardName
    deck_card_value = list(deck.values())  # Converts deck.values to a list and assigns it to deckCardValue
    x = random.randint(0,len(deck)-1) #Range between 0 and the amount of cards in deck
    deck.pop(deck_card_name[x], deck_card_value[x])
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
        globals.cardvals.extend(list((pulled_card_val1,pulled_card_val2))) #Same for card value
        return globals.cards, globals.cardvals

def hit():
    """Adds card to player hand"""
    card_draw_name, card_draw_val = pull_card() #Pulls card, unpacks tuple.
    print(f"You drew: {card_draw_name}")
    globals.cards.append(card_draw_name) #Appends a card to the global hand variable
    globals.cardvals.append(card_draw_val) #Appends a card value to the global hand vals variable
    return card_draw_name #No return yet

def stand():
    pass

def display_hand():
    print("You have the cards: ")
    for card in globals.cards_in_hand:
        print(card)
    print(f"Their values total to: {utils.calc_hand(globals.cardvals)}")


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












