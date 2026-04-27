def solve_division():
    # Read number of test cases
    try:
        t = int(input())
    except ValueError:
        return

    for _ in range(t):
        try:
            # Read a and b
            a, b = input().split()
            # Perform integer division
            print(int(a) // int(b))
            
        except ZeroDivisionError as e:
            print("Error Code:", e)
            
        except ValueError as e:
            print("Error Code:", e)

if __name__ == "__main__":
    solve_division()