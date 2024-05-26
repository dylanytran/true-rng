from collections import Counter
from backend import rand_gen

# Generate random numbers as 5-digit sequences using the custom generator
def generate_poker_hands(n):
    return [f"{rand_gen(0, 99999):05}" for _ in range(n)]

# Classify poker hands
def classify_poker_hands(hands):
    classifications = {
        'all_different': 0,
        'one_pair': 0,
        'two_pairs': 0,
        'three_of_a_kind': 0,
        'full_house': 0,
        'four_of_a_kind': 0,
        'five_of_a_kind': 0
    }
    
    for hand in hands:
        counts = Counter(hand).values()
        counts = sorted(counts, reverse=True)
        
        if counts == [5]:
            classifications['five_of_a_kind'] += 1
        elif counts == [4, 1]:
            classifications['four_of_a_kind'] += 1
        elif counts == [3, 2]:
            classifications['full_house'] += 1
        elif counts == [3, 1, 1]:
            classifications['three_of_a_kind'] += 1
        elif counts == [2, 2, 1]:
            classifications['two_pairs'] += 1
        elif counts == [2, 1, 1, 1]:
            classifications['one_pair'] += 1
        else:
            classifications['all_different'] += 1
            
    return classifications

# Example usage
poker_hands = generate_poker_hands(300)
classification_results = classify_poker_hands(poker_hands)
print("Poker hand classification results:")
for hand_type, count in classification_results.items():
    print(f"{hand_type}: {count}")
