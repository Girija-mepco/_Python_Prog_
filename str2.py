from itertools import combinations

# Input handling
n = int(input())
s = input().split()
k = int(input())

# Generate all possible combinations
all_combinations = list(combinations(s, k))

# Filter combinations that contain the character 'a'
containing_a = [c for c in all_combinations if 'a' in c]

# Calculate probability: favorable / total
probability = len(containing_a) / len(all_combinations)

# Output result formatted to 3 decimal places
print(f"{probability:.4f}")
