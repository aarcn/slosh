from cards import ranks
import math


def pairs_sidebet(master_count_map):
    """
    Returns RTP for pairs side bet
    Example return value: 99.1234
    Will print Calculated RTP vs Theoretical RTP (92.0482%)

    Payouts:
    Suited Pairs: 20:1
    Colored Pairs: 10:1
    Mixed Pairs: 5:1

    baby combinatorics compared to poker.py
    """
    total_cards = sum(master_count_map.values())
    total_pairs = math.comb(total_cards, 2)

    suited_probability = 0
    colored_probability = 0
    mixed_probability = 0

    # probability of drawing a suited pair
    for card, count in master_count_map.items():
        if count > 1:
            suited_probability += (count / total_cards) * ((count - 1) / (total_cards - 1))

    # probability of drawing a colored pair
    red_probability = 0
    black_probability = 0

    for rank in ranks:
        red_count = master_count_map.get(rank + 'H', 0) + master_count_map.get(rank + 'D', 0)
        black_count = master_count_map.get(rank + 'S', 0) + master_count_map.get(rank + 'C', 0)

        if red_count > 1:
            red_probability += (red_count / total_cards) * ((red_count - 1) / (total_cards - 1))

        if black_count > 1:
            black_probability += (black_count / total_cards) * ((black_count - 1) / (total_cards - 1))

    colored_probability = red_probability + black_probability - suited_probability

    # probability of drawing a mixed pair
    for rank in ranks:
        count = (master_count_map.get(rank + 'H', 0) + master_count_map.get(rank + 'D', 0) +
                 master_count_map.get(rank + 'S', 0) + master_count_map.get(rank + 'C', 0))
        if count > 1:
            mixed_probability += (count / total_cards) * ((count - 1) / (total_cards - 1))

    mixed_probability -= colored_probability + suited_probability

    # no_pair_probability is compliment of probability of drawing any pair
    no_pair_probability = 1 - (suited_probability + colored_probability + mixed_probability)

    calculated_rtp = 100 + (((suited_probability * 25) + (colored_probability * 12) +
                             (mixed_probability * 5) + (no_pair_probability * -1)) * 100)

    theoretical_rtp = 92.0482

    print("|====== pairs.py ======|")
    print(f"Calculated RTP: {calculated_rtp:.4f}%")
    print(f"Theoretical RTP: {theoretical_rtp:.4f}%")
    if calculated_rtp > theoretical_rtp:
        print("Worth it")
    else:
        print("Not worth it")
    print("\n\n")

    return calculated_rtp
