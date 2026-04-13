Print an array of the elements that do not sum to n=3 . 
#program

if __name__ == "__main__":
    # Remove the prompt strings inside the brackets
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [[i, j, k] for i in range(x + 1) 
                        for j in range(y + 1) 
                        for k in range(z + 1) 
                        if i + j + k != n]
    
    print(result)