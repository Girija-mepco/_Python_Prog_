from collections import defaultdict

# Read n and m
n, m = map(int, input().split())

# Initialize defaultdict with a list as the default factory
d = defaultdict(list)

# Read Group A words and store their 1-based indices
for i in range(1, n + 1):
    word = input().strip()
    d[word].append(i)

# Read Group B words and check against the dictionary
for _ in range(m):
    word_b = input().strip()
    if word_b in d:
        # Print all indices joined by a space
        print(*(d[word_b]))
    else:
        # Word not found in Group A
        print(-1)
