def calculateAverage(scores):
    return round((sum(scores) / len(scores)), 2)
    

def findStudentScore(students, studentName):
    for i in students:
        if i == studentName:
            return students[i]

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Buscar las notas del estudiante
    scores = findStudentScore(student_marks, query_name)
    
    # Calcular el promedio
    print("{:.2F}".format(calculateAverage(scores)))
    