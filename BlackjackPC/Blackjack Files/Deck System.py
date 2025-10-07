import random
"""
Leftovers
Aces = {"Ace of Hearts": 1, "Ace of Spades": 1, "Ace of Clubs": 1, "Ace of Diamonds": 1}
Twos = {"2 of Hearts" : 2, "2 of Spades": 2, "2 of Clubs": 2, "2 of Diamonds": 2}
Threes = {"3 of Hearts": 3, "3 of Spades":3, "3 of Clubs": 3, "3 of Diamonds": 3}
Fours = {"4 of Hearts": 4, "4 of Spades": 4, "4 of Clubs": 4, "4 of Diamonds": 4}
Fives = {"5 of Hearts": 5, "5 of Spades": 5, "5 of Clubs": 5, "5 of Diamonds": 5}
Sixes = {"6 of Hearts": 6, "6 of Spades": 6, "6 of Clubs": 6, "6 of Diamonds": 6}
Sevens = {"7 of Hearts": 7, "7 of Spades": 7, "7 of Clubs": 7, "7 of Diamonds": 7}
Eights = {"8 of Hearts": 8, "8 of Spades": 8, "8 of Clubs": 8, "8 of Diamonds": 8}
Nines = {"9 of Hearts": 9, "9 of Spades": 9, "9 of Clubs": 9, "9 of Diamonds": 9}
Tens = {"10 of Hearts": 10, "10 of Spades": 10, "10 of Clubs": 10, "10 of Diamonds": 10}
Jacks = {"Jack of Hearts": 10, "Jack of Spades": 10, "Jack of Clubs": 10, "Jack of Diamonds": 10}
Queens = {"Queen of Hearts": 10, "Queen of Spades": 10, "Queen of Clubs": 10, "Queen of Diamonds": 10}
Kings = {"King of Hearts": 10, "King of Spades": 10, "King of Clubs": 10, "King of Diamonds": 10}
Maybe This can be used elsewhere??
"""




deck = {"Ace of Hearts": 1, "Ace of Spades": 1, "Ace of Clubs": 1, "Ace of Diamonds": 1,
        "2 of Hearts" : 2, "2 of Spades": 2, "2 of Clubs": 2, "2 of Diamonds": 2,
        "3 of Hearts": 3, "3 of Spades":3, "3 of Clubs": 3, "3 of Diamonds": 3,
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

x = random.randint(0,51)
deckCardNumber = list(deck.values())
deckCardName = list(deck.keys())

print(deckCardNumber[x])
print(deckCardName[x])












