The first line contains an integer, , the number of students who have subscribed to the English newspaper.
The second line contains space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains space separated roll numbers of those students. 

#program
def solve():
    # Read English subscribers
    n = int(input())
    english_set = set(map(int, input().split()))
    
    # Read French subscribers
    m = int(input())
    french_set = set(map(int, input().split()))
    
    # Union finds all unique elements in both sets
    at_least_one = english_set.union(french_set)
    
    # Output the total count
    print(len(at_least_one))

if __name__ == "__main__":
    solve()