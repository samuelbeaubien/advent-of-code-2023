from enum import Enum
from functools import total_ordering

@total_ordering
class HandType(Enum):
    FiveOfAKind = 7
    FourOfAKind = 6
    FullHouse = 5
    ThreeOfAKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1

    def __lt__(self, other):
        if self.__class__ is other.__class__:
           return self.value < other.value
        return NotImplemented

@total_ordering
class Card(Enum):
    A = 'A'
    K = 'K'
    Q = 'Q'
    J = 'J'
    T = 'T'
    Nine = '9'
    Eight = '8'
    Seven = '7'
    Six = '6'
    Five = '5'
    Four = '4'
    Three = '3'
    Two = '2'

    def __lt__(self, other):
        if self.__class__ is other.__class__:
           return Card.transform_value(self.value) < Card.transform_value(other.value)
        return NotImplemented
    
    @classmethod
    def transform_value(cls, value):
        if value == 'A':
            return 14
        elif value == 'K':
            return 13
        elif value == 'Q':
            return 12
        elif value == 'J':
            return 1
        elif value == 'T':
            return 10
        else:
            return int(value)

@total_ordering
class HandBid:
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self.type = self.get_type()
        self.cards = []
        for card_str in hand:
            self.cards.append(Card(card_str))

    def get_card(self):
        card_str = self.hand[0]
        return Card(card_str)

    def get_type(self):
        map_dict = {}
        for card in hand:
            if card in map_dict:
                map_dict[card] +=1
            else:
                map_dict[card] = 1
        num_unique = 0
        num_pairs = 0
        num_three = 0
        num_four = 0
        num_five = 0

        if self.hand == 'QQQJA':
            pass

        if 'J' in map_dict:
            num_jokers = map_dict['J']
            map_dict.pop('J')
            key_max = None
            val_max = 0
            for key, val in map_dict.items():
                if val > val_max:
                    key_max = key
                    val_max = val
            if key_max is not None:
                map_dict[key_max] += num_jokers
            else:
                map_dict['J'] = num_jokers
            
        for key, val in map_dict.items():
            if val == 1:
                num_unique += 1
            elif val == 2:
                num_pairs += 1
            elif val == 3:
                num_three += 1
            elif val == 4:
                num_four += 1
            elif val == 5:
                num_five += 1
        # Return the type
        if num_five == 1:
            return HandType.FiveOfAKind
        elif num_four == 1:
            return HandType.FourOfAKind
        elif num_three == 1 and num_pairs == 1:
            return HandType.FullHouse
        elif num_three == 1:
            return HandType.ThreeOfAKind
        elif num_pairs == 2:
            return HandType.TwoPair
        elif num_pairs == 1:
            return HandType.OnePair
        else:
            return HandType.HighCard
        
    def get_winning(self, rank):
        return self.bid*rank

    def __lt__(self, other):
        if self.__class__ is other.__class__:
           if self.type == other.type:
                self_cards = self.cards
                other_cards = other.cards
                for self_card, other_card in zip(self_cards, other_cards):
                    if self_card == other_card:
                        continue
                    else:
                        return self_card < other_card
                return False
           else:
               return self.type < other.type
        return NotImplemented
        
file = open("src/day-7/input.txt")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
hand_bids = []
for line in lines:
    [hand, bid] = line.split(' ')
    hand_bids.append(HandBid(hand, int(bid)))
x = hand_bids[2] < hand_bids[3] 
hand_bids.sort()
total = 0
for hand_bid, rank in zip(hand_bids, range(1, len(hand_bids)+1)):
    winning = hand_bid.get_winning(rank)
    total += winning

print("hello")
