# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N=int(input())
namec=input().split()
avg=0
for _ in range(N):
    students=namedtuple('student',namec)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    avg+=int(student.MARKS)
print('{:.2f}'.format(avg / N))
