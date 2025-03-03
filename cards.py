# Define the Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


suits = ['S', 'C', 'H', 'D']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
ten_value_ranks = ['T', 'J', 'Q', 'K']

deck = [Card(suit, rank) for suit in suits for rank in ranks]

count_mapping = {
    '2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
    '7': 0, '8': 0, '9': 0,
    'T': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
}

running_count = 0

deck_count = 6
master_count = {
    # Spade cards
    'AS': deck_count, '2S': deck_count, '3S': deck_count, '4S': deck_count, '5S': deck_count,
    '6S': deck_count, '7S': deck_count, '8S': deck_count, '9S': deck_count, 'TS': deck_count,
    'JS': deck_count, 'QS': deck_count, 'KS': deck_count,

    # Club cards
    'AC': deck_count, '2C': deck_count, '3C': deck_count, '4C': deck_count, '5C': deck_count,
    '6C': deck_count, '7C': deck_count, '8C': deck_count, '9C': deck_count, 'TC': deck_count,
    'JC': deck_count, 'QC': deck_count, 'KC': deck_count,

    # Heart cards
    'AH': deck_count, '2H': deck_count, '3H': deck_count, '4H': deck_count, '5H': deck_count,
    '6H': deck_count, '7H': deck_count, '8H': deck_count, '9H': deck_count, 'TH': deck_count,
    'JH': deck_count, 'QH': deck_count, 'KH': deck_count,

    # Diamond cards
    'AD': deck_count, '2D': deck_count, '3D': deck_count, '4D': deck_count, '5D': deck_count,
    '6D': deck_count, '7D': deck_count, '8D': deck_count, '9D': deck_count, 'TD': deck_count,
    'JD': deck_count, 'QD': deck_count, 'KD': deck_count
}


dealer_hand = {

}

player_hand = {

}

split_hand = {

}
