import random
from collections import defaultdict


class CardDeck:
    def __init__(self, ranks):
        self.suits = ['H', 'D', 'C', 'S']
        self.ranks = ranks
        self.deck = [{'rank': rank, 'suit': suit} for rank in self.ranks for suit in self.suits]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, num_cards):
        return [self.deck.pop() for _ in range(num_cards)]

    @staticmethod
    def evaluate_hand(player_hand, community_cards, ranks):
        all_cards = player_hand + community_cards
        all_cards.sort(key=lambda x: ranks.index(x['rank']))

        def is_flush(cards):
            suits_count = defaultdict(int)
            for card in cards:
                suits_count[card['suit']] += 1
                if suits_count[card['suit']] >= 5:
                    return True, card['suit']
            return False, None

        def is_straight(cards):
            unique_ranks = list(set(card['rank'] for card in cards))
            unique_ranks.sort(key=lambda x: ranks.index(x))

            for i in range(len(unique_ranks) - 4):
                if unique_ranks[i:i+5] == list(range(ranks.index(unique_ranks[i]), ranks.index(unique_ranks[i])+5)):
                    return True, unique_ranks[i:i+5]
            return False, None

        def rank_count(cards):
            rank_counts = defaultdict(int)
            for card in cards:
                rank_counts[card['rank']] += 1
            return rank_counts

        def get_rank_of_a_kind(cards, n):
            rank_counts = rank_count(cards)
            for rank, count in rank_counts.items():
                if count == n:
                    return rank
            return None

        flush, flush_suit = is_flush(all_cards)
        straight, straight_ranks = is_straight(all_cards)
        rank_counts = rank_count(all_cards)

        if flush and straight:
            if straight_ranks[-1] == ranks[-1]:
                return 'Royal Flush', None
            return 'Straight Flush', straight_ranks[-1]

        four_of_a_kind_rank = get_rank_of_a_kind(all_cards, 4)
        if four_of_a_kind_rank:
            return 'Four of a Kind', four_of_a_kind_rank

        three_of_a_kind_rank = get_rank_of_a_kind(all_cards, 3)
        pair_rank = get_rank_of_a_kind(all_cards, 2)

        if three_of_a_kind_rank and pair_rank:
            return 'Full House', (three_of_a_kind_rank, pair_rank)

        if flush:
            return 'Flush', flush_suit

        if straight:
            return 'Straight', straight_ranks[-1]

        if three_of_a_kind_rank:
            return 'Three of a Kind', three_of_a_kind_rank

        if pair_rank:
            if len(rank_counts) == 3:
                return 'Two Pair', pair_rank
            return 'One Pair', pair_rank

        high_card = max(all_cards, key=lambda x: ranks.index(x['rank']))['rank']
        return 'High Card', high_card