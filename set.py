Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of country stamps.

Find the total number of distinct country stamps.

#program

def count_stamps():
    # Read the number of stamps
    n = int(input())
    
    # Initialize an empty set
    stamps = set()
    
    # Add each country to the set
    for _ in range(n):
        stamps.add(input().strip())
    
    # Print the total number of unique items
    print(len(stamps))

if __name__ == "__main__":
    count_stamps()
