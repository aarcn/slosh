from cards import ranks, master_count
import math


# logic to determine if pairs side bet is worth it
def pairs_side_bet(master_count_map):
    """
    calculate RTP for pairs side bet
    will display Calculated RTP vs Theoretical RTP (95.90%)
    Suited 20:1
    Colored: 10:1
    Mixed: 5:1
    """
    total_cards = sum(master_count_map.values())
    suited_probability = 0
    colored_probability = 0
    mixed_probability = 0
    total_pairs = math.comb(total_cards, 2)

    # probability of drawing suited pairs
    for card, count in master_count_map.items():
        if count > 1:
            suited_probability += (count / total_cards) * ((count - 1) / (total_cards - 1))

    # probability of drawing colored pairs
    red_probability = 0
    black_probability = 0

    for rank in ranks:
        red_count = master_count_map.get(rank + 'H', 0) + master_count_map.get(rank + 'D', 0)
        black_count = master_count_map.get(rank + 'S', 0) + master_count_map.get(rank + 'C', 0)

        if red_count > 1:
            red_probability += (red_count / total_cards) * ((red_count - 1) / (total_cards - 1))

        if black_count > 1:
            black_probability += (black_count / total_cards) * ((black_count - 1) / (total_cards - 1))

    print(red_probability, black_probability)
    colored_probability = red_probability + black_probability - suited_probability

    # probability of drawing mixed pairs
    for rank in ranks:
        count = (master_count_map.get(rank + 'H', 0) + master_count_map.get(rank + 'D', 0) +
                 master_count_map.get(rank + 'S', 0) + master_count_map.get(rank + 'C', 0))
        if count > 1:
            mixed_probability += (count / total_cards) * ((count - 1) / (total_cards - 1))

    mixed_probability -= colored_probability + suited_probability

    # no pair probability is calculated by subtracting every special combination of hands from 1
    no_pair_probability = 1 - (suited_probability + colored_probability + mixed_probability)

    calculated_rtp = 100 + (((suited_probability * 25) + (colored_probability * 12) +
                             (mixed_probability * 5) + (no_pair_probability * -1)) * 100)

    theoretical_rtp = 92.0482

    print(f"Calculated RTP: {calculated_rtp:.4f}%")
    print(f"Theoretical RTP: {theoretical_rtp:.4f}%")

    if calculated_rtp > theoretical_rtp:
        print("Worth it")
    else:
        print("Not worth it")



pairs_side_bet(master_count)

# logic to determine if poker (21 + 3) side bet is worth it
# logic to determine if lucky ladies (any 20 queens) side bet is worth it
