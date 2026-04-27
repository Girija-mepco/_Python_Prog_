from itertools import groupby

# Read the input string
S = input()

# Group consecutive characters and format as (count, character)
# Use * to unpack the list and print elements separated by spaces
print(*(f"({len(list(group))}, {key})" for key, group in groupby(S)))
