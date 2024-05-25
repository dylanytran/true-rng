from backend import rand_gen
import numpy as np
from scipy.stats import chisquare

# Generate random numbers using the custom generator
def generate_random_numbers(n, low=0, high=100):
    return [rand_gen(low, high) for _ in range(n)]

# Perform Chi-square test
def chi_square_test(data, num_bins=10):
    # Create histogram
    hist, bin_edges = np.histogram(data, bins=num_bins, range=(min(data), max(data)))
    
    # Expected counts (uniform distribution)
    expected_counts = [len(data) / num_bins] * num_bins
    
    # Chi-square test
    chi2, p_value = chisquare(hist, expected_counts)
    return chi2, p_value

# Example usage
random_numbers = generate_random_numbers(1000, 1, 10)
chi2, p_value = chi_square_test(random_numbers)
print(f"Chi-square statistic: {chi2}, p-value: {p_value}")