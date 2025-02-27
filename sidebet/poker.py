import math
from cards import ranks, suits


def poker_sidebet(master_count_map):
    """
    Returns RTP for the poker (21+3) side bet
    Example return value: 99.1234
    Will print Calculated RTP vs Theoretical RTP (83.1803%)

    Payouts:
    Suited Three of a Kind: 100:1
    Straight Flush: 30:1
    Three of a Kind: 20:1
    Straight: 10:1
    Flush: 4:1

    combinatorics up the wazoo
    your mind will become mush reading this
    """

    total_cards = sum(master_count_map.values())
    total_three_card_combos = math.comb(total_cards, 3)
    straight_sequences = [ranks[i:i + 3] for i in range(len(ranks) - 2)] + [["A", "2", "3"]]

    suited_three_of_a_kind_probability = 0
    three_of_a_kind_probability = 0
    straight_flush_probability = 0
    straight_probability = 0
    flush_probability = 0

    # probability of drawing a suited three of a kind
    for rank in ranks:
        for suit in suits:
            suit_count = master_count_map.get(rank + suit, 0)
            if suit_count >= 3:
                suited_three_of_a_kind_probability += math.comb(suit_count, 3) / total_three_card_combos

    # probability of drawing a three of a kind
    for rank in ranks:
        count = 0
        for suit in suits:
            count += master_count_map.get(rank + suit, 0)
        if count >= 3:
            three_of_a_kind_probability += math.comb(count, 3) / total_three_card_combos
    three_of_a_kind_probability -= suited_three_of_a_kind_probability

    # probability of drawing a straight flush
    for suit in suits:
        for sequence in straight_sequences:
            count1 = master_count_map.get(sequence[0] + suit, 0)
            count2 = master_count_map.get(sequence[1] + suit, 0)
            count3 = master_count_map.get(sequence[2] + suit, 0)

            if count1 > 0 and count2 > 0 and count3 > 0:
                straight_flush_probability += (
                        (math.comb(count1, 1) * math.comb(count2, 1) *
                         math.comb(count3, 1)) / math.comb(total_cards, 3))

    # probability of drawing a straight
    for sequence in straight_sequences:
        counts = [sum(master_count_map.get(rank + suit, 0) for suit in suits) for rank in sequence]

        if all(counts):
            straight_probability += (
                    (math.comb(counts[0], 1) * math.comb(counts[1], 1) *
                     math.comb(counts[2], 1)) / math.comb(total_cards, 3))
    straight_probability -= straight_flush_probability

    # probability of drawing a flush
    for suit in suits:
        suit_count = 0
        for rank in ranks:
            suit_count += master_count_map.get(rank + suit, 0)
        if suit_count >= 3:
            flush_combination = math.comb(suit_count, 3)
            flush_probability += flush_combination / total_three_card_combos
    flush_probability -= straight_flush_probability + suited_three_of_a_kind_probability

    # no_hand_probability is compliment of probability of drawing any hand
    no_hand_probability = 1 - (flush_probability + straight_probability +
                               three_of_a_kind_probability + straight_flush_probability +
                               suited_three_of_a_kind_probability)

    calculated_rtp = 100 + (((flush_probability * 4) + (straight_probability * 10) +
                             (three_of_a_kind_probability * 20) + (straight_flush_probability * 30) +
                             (suited_three_of_a_kind_probability * 100) + (no_hand_probability * -1)) * 100)

    theoretical_rtp = 83.1803

    print("|====== poker.py ======|")
    print(f"Calculated RTP: {calculated_rtp:.4f}%")
    print(f"Theoretical RTP: {theoretical_rtp:.4f}%")
    if calculated_rtp > theoretical_rtp:
        print("Worth it")
    else:
        print("Not worth it")
    print("\n\n")

    return calculated_rtp
