import DeckSystem

def start_game():
    DeckSystem.deal_card() #amount of cards left in deck should be 50

    DeckSystem.deck_count()

i = 0
while i > 52:
    DeckSystem.deal_card()
    i += 1

