from collections import namedtuple

if __name__ == '__main__':
    N = int(input())
    Student = namedtuple('Student', input().split())
    for i in range(0, N):
        std = Student(ID=)