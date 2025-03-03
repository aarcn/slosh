import math
from cards import suits, ten_value_ranks


def luckyladies_sidebet(master_count_map):
    """
    Returns RTP for the lucky ladies side bet
    Example return value: 99.1234
    Prints the Calculated RTP vs Theoretical RTP (81.1272%)

    Payouts:
    Queen of Hearts Pair: 100:1
    Matched 20: 20:1
    Suited 20: 10:1
    Any 20: 2:1
    Any queen: 1:1
    """

    total_cards = sum(master_count_map.values())
    total_pairs = math.comb(total_cards, 2)

    qh_pair_probability = 0
    matched_twenty_probability = 0
    suited_twenty_probability = 0
    any_twenty_probability = 0
    queen_probability = 0

    # probability of drawing queen of hearts pair
    qh_count = master_count_map.get("QH", 0)
    if qh_count >= 2:
        qh_pair_probability = (qh_count / total_cards) * ((qh_count - 1) / (total_cards - 1))

    # probability of drawing matched twenty
    for rank in ten_value_ranks:
        for suit in suits:
            count = master_count_map.get(rank + suit, 0)
            if count >= 2:
                matched_twenty_probability += (count / total_cards) * ((count - 1) / (total_cards - 1))
    matched_twenty_probability -= qh_pair_probability

    # probability of drawing suited twenty
    suited_twenty_ten_value_prob = 0
    suited_twenty_a_nine_value_prob = 0
    for suit in suits:
        count = sum(master_count_map.get(rank + suit, 0) for rank in ten_value_ranks)
        if count >= 2:
            suited_twenty_ten_value_prob += (count / total_cards) * ((count - 1) / (total_cards - 1))
    for suit in suits:
        ace_count = master_count_map.get("A" + suit, 0)
        nine_count = master_count_map.get("9" + suit, 0)
        if ace_count >= 1 and nine_count >= 1:
            suited_twenty_a_nine_value_prob += (((ace_count / total_cards) * (nine_count / (total_cards - 1))) +
                                          ((nine_count / total_cards) * (ace_count / (total_cards - 1))))
    suited_twenty_probability = suited_twenty_ten_value_prob + suited_twenty_a_nine_value_prob
    suited_twenty_probability -= matched_twenty_probability + qh_pair_probability

    # probability of drawing any twenty
    any_twenty_ten_value_prob = 0
    any_twenty_a_nine_value_prob = 0
    ten_value_count = sum(master_count_map.get(rank + suit, 0) for rank in ten_value_ranks for suit in suits)
    if ten_value_count >= 2:
        any_twenty_ten_value_prob += (ten_value_count / total_cards) * ((ten_value_count - 1) / (total_cards - 1))
    any_ace_count = sum(master_count_map.get("A" + suit, 0) for suit in suits)
    any_nine_count = sum(master_count_map.get("9" + suit, 0) for suit in suits)
    if any_ace_count >= 1 and any_nine_count >= 1:
        any_twenty_a_nine_value_prob += (((any_ace_count / total_cards) * (any_nine_count / (total_cards - 1))) +
                                   ((any_nine_count / total_cards) * (any_ace_count / (total_cards - 1))))
    any_twenty_probability = any_twenty_ten_value_prob + any_twenty_a_nine_value_prob
    any_twenty_probability -= suited_twenty_probability + matched_twenty_probability + qh_pair_probability

    # probability of drawing any queen
    queen_count = sum(master_count_map.get("Q" + suit, 0) for suit in suits)
    if queen_count >= 1:
        queen_probability = (1 - ((total_cards - queen_count) / total_cards) *
                             ((total_cards - queen_count - 1) / (total_cards - 1)))
    queen_probability -= (any_twenty_ten_value_prob + suited_twenty_ten_value_prob +
                          matched_twenty_probability + qh_pair_probability)

    # no_luckyladies_probability is compliment of probability of drawing any pair
    no_luckyladies_probability = 1 - (qh_pair_probability + matched_twenty_probability +
                                      suited_twenty_probability + any_twenty_probability +
                                      queen_probability)

    calculated_rtp = 100 + (((qh_pair_probability * 100) + (matched_twenty_probability * 20) +
                             (suited_twenty_probability * 10) + (any_twenty_probability * 2) +
                             (queen_probability * 1) + (no_luckyladies_probability * -1)) * 100)

    theoretical_rtp = 81.1272

    print("|=== luckyladies.py ===|")
    print(f"qh_pair (0.000309): {qh_pair_probability:.8f}")
    print(f"matched twenty (0.004638): {matched_twenty_probability:.8f}")
    print(f"suited twenty (0.020777): {suited_twenty_probability:.8f}")
    print(f"any twenty (0.080139): {any_twenty_probability:.8f}")
    print(f"queen (0.106851): {queen_probability:.8f}")
    print(f"loser (0.787287): {no_luckyladies_probability:.8f}")
    print("\n\n")
    print(f"Calculated RTP: {calculated_rtp:.4f}%")
    print(f"Theoretical RTP: {theoretical_rtp:.4f}%")
    if calculated_rtp > theoretical_rtp:
        print("Worth it")
    else:
        print("Not worth it")
    print("\n\n")

    return calculated_rtp
