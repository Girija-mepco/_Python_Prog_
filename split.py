Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen. 
#PROGRAM
def split_and_join(line):
    # Split the string into a list using the space delimiter
    words = line.split(" ")
    
    # Join the list elements into a single string with hyphens
    result = "-".join(words)
    
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
