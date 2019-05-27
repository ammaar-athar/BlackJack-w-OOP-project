'''This is my first trial at coding a blackjack game'''
import random

print ("WELCOME to blackjack\n")


suits=['Spades','Clubs','Hearts','Diamonds']
numbers=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
value={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        
    def __str__(self):
        return self.rank+" of "+self.suit

class Deck:
    
    def __init__(self):
        self.deck=[]
        for s in suits:
            for r in numbers:
                self.deck.append(Card(s,r))
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        dealt=self.deck.pop()
        return dealt
    
    def __str__(self):
        string="The Deck Contains:\n"
        for card in self.deck:
            string+=card.__str__()+"\n"
        return string

    
d=Deck()
d.shuffle()
dealer_hand=[]
player_hand=[]

class player_hand:
    def __init__(self):
        self.hand=[]
        self.total=0
        
    def calctotal(self):
        
player_hand.append(d.deal())
player_hand.append(d.deal())
        
dealer_hand.append(d.deal())
dealer_hand.append(d.deal())

print("Dealers hand is:\n")
print(dealer_hand[0].__str__()+" {Face Down Card}")
print("\nPlayers hand is:\n")
print(player_hand[0].__str__()+" "+player_hand[1].__str__())

move=input("would you like to hit or stay?\n")

if move=='hit':
    player_hand.append(d.deal())
    print("Dealers hand is:\n")
    print(dealer_hand[0].__str__()+" {Face Down Card}")
    print("\nPlayers hand is:\n")
    print(player_hand[0].__str__()+" "+player_hand[1].__str__()+" "+player_hand[2].__str__())
else:
    dealer_hand.append(d.deal())
    print("Dealers hand is:\n")
    print(dealer_hand[0].__str__()+dealer_hand[1].__str__())
    print("\nPlayers hand is:\n")
    print(player_hand[0].__str__()+" "+player_hand[1].__str__()+" "+player_hand[2].__str__())
    
#starting the game here

while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100
    
    # Prompt the Player for their bet:
    take_bet(player_chips)
    
    # Show the cards:
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    # If Player hasn't busted, play Dealer's hand        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Test different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    # Inform Player of their chips total    
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
