import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + 'of' + self.suit



class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):

        finished_deck = ''
        for card in self.deck:
            finished_deck += card.__str__()
        return finished_deck
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10 
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet



def take_bet(chips):
    while True: 
        try: 
            chips.bet = int(input('How many chips would you like to bet?'))
        except:
            print('Sorry, you must enter a vaild number to bet')
        else:
            if chips.bet > chips.total:
                print('You are betting more than your total amount of chips! Total Chips: ' + chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        
        x = input('Would you like to Hit or Stand? Enter "h" or "s')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('You stand. It is now the dealers turn!')
            playing = False
        else:
            print('Please play again')
            continue
        break 

def show_some(player, dealer):
    print("/n Dealer's Hand ")
    print("HIDDEN CARD")
    print('', dealer.cards[1])
    print("/n Player's Hand: ", *player.cards, sep='/n ')

def show_all(player, dealer):
    print("/n Dealer's Hand ", *dealer.cards, sep='/n ')
    print("Dealer's Hand = " , dealer.value)
    print("/n Player's Hand: ", *player.cards, sep='/n ')
    print("Player's Hand = ", player.value)


def player_busts(player,dealer,chips):
    print('You Busted!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('You Win!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer Bust!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer Wins!')
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player tie! It's a push.") 

###TIE THE GAME TOGETHER###
while True:
    print('Welcome to Blackjack! Get ready to play to win!!!')

    deck = Deck()
    deck.shuffle
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing: 
        




    