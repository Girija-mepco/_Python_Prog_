You are the manager of a supermarket.
You have a list of items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

#program

from collections import OrderedDict

# Input the number of items
try:
    N = int(input())
except EOFError:
    N = 0

# Use OrderedDict to maintain the order of first occurrence
item_prices = OrderedDict()

for _ in range(N):
    line = input().split()
    # Item name can have multiple words, price is the last element
    price = int(line[-1])
    item_name = " ".join(line[:-1])
    
    # Update net price
    if item_name in item_prices:
        item_prices[item_name] += price
    else:
        item_prices[item_name] = price
