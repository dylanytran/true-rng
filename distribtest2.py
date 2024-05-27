from backend import rand_gen
import numpy as np
from scipy.stats import chisquare

# Generate random numbers using the custom generator
def generate_random_numbers(n, low=0, high=100):
    return [rand_gen(low, high) for _ in range(n)]

min_val = 1
max_val = 10
num_samples = 500
num_bins = max_val - min_val + 1

# Generate random numbers and count occurrences
counts = [0] * num_bins

for _ in range(num_samples):
    rand_num = rand_gen(min_val, max_val)
    counts[rand_num - min_val] += 1

# Print results
print(f"Observed counts: {counts}")