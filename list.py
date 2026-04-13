Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#program

if __name__ == '__main__':
    # 1. Store data in a nested list
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # 2. Find the second lowest grade
    # Get unique scores, sort them, and pick the second one
    scores = sorted(list(set([s[1] for s in students])))
    second_lowest = scores[1]
    
    # 3. Find names with the second lowest grade
    names = [s[0] for s in students if s[1] == second_lowest]
    
    # 4. Sort alphabetically and print
    for name in sorted(names):
        print(name)
