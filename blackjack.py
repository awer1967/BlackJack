"""The Black Jack game - a simple educational version"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:
    """A card class definition, returns with a standard method a rank and a suit """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    """A desk of card definition, initializes it and  shuffles it"""
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # build Card objects and add them to the list

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.deck)

    def deal(self):
        """Deal with the deck"""
        single_card = self.deck.pop()
        return single_card


class Hand:
    """Defines a player hand"""
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        """Add a card for the hand"""
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        """Aces adjustment"""
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    """Chips assigned to the hand"""
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        """Win the chips"""
        self.total += self.bet

    def lose_bet(self):
        """Loose the chips"""
        self.total -= self.bet

# Functions section


def take_bet(chips):
    """Taking the bet with a chips"""
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def hit(deck, hand):
    """Make a hit from the hand"""
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """Should the player hit or stand"""
    global playing  # to control an upcoming while loop
    while True:
        x_mas = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x_mas[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above

        elif x_mas[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    """Show some card from both sides"""
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    """Show all the card from both sides"""
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    """Player busts"""
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    """Player wins"""
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    """Dealer busts"""
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    """Dealer wins"""
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    """The Push"""
    print("Dealer and Player tie! It's a push.")
