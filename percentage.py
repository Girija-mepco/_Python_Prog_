The first line contains the integer n , the number of students' records. The next lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
#program
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        marks = student_marks[query_name]
        average = sum(marks) / len(marks)
        print(f"{average:.2f}")