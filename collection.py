Perform append, pop, popleft and appendleft methods on an empty deque a.

#program

from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    # Read the command (e.g., "append 5" or "pop")
    command = input().split()
    method = command[0]
    
    if len(command) > 1:
        # Call methods with arguments like append(5)
        getattr(d, method)(command[1])
    else:
        # Call methods without arguments like pop()
        getattr(d, method)()

print(*(d))
