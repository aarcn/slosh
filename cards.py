# Define the Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

deck = [Card(suit, rank) for suit in suits for rank in ranks]

count_mapping = {
    '2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
    '7': 0, '8': 0, '9': 0,
    'T': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
}

running_count = 0

master_count = {
    # Spade cards
    'AS': 8, '2S': 8, '3S': 8, '4S': 8, '5S': 8,
    '6S': 8, '7S': 8, '8S': 8, '9S': 8, 'TS': 8,
    'JS': 8, 'QS': 8, 'KS': 8,

    # Club cards
    'AC': 8, '2C': 8, '3C': 8, '4C': 8, '5C': 8,
    '6C': 8, '7C': 8, '8C': 8, '9C': 8, 'TC': 8,
    'JC': 8, 'QC': 8, 'KC': 8,

    # Heart cards
    'AH': 8, '2H': 8, '3H': 8, '4H': 8, '5H': 8,
    '6H': 8, '7H': 8, '8H': 8, '9H': 8, 'TH': 8,
    'JH': 8, 'QH': 8, 'KH': 8,

    # Diamond cards
    'AD': 8, '2D': 8, '3D': 8, '4D': 8, '5D': 8,
    '6D': 8, '7D': 8, '8D': 8, '9D': 8, 'TD': 8,
    'JD': 8, 'QD': 8, 'KD': 8
}

dealer_hand = {

}

player_hand = {

}

split_hand = {

}