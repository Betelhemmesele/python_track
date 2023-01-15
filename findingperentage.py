if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    mark=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    mark=sum(student_marks[query_name])
    avg=mark/3
    print("%.2f"%avg)
   
