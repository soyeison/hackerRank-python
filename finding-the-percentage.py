def calculateAverage(scores):
    return round((sum(scores) / len(scores)), 2)
    

def findStudentScore(students, studentName):
    for i in students:
        if i == studentName:
            return students[i]

if __name__ == '__main__':
    """ n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input() """
    n = 3
    student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
    query_name = 'Malika'

    # Buscar las notas del estudiante
    scores = findStudentScore(student_marks, query_name)
    
    # Calcular el promedio
    print("{:.2F}".format(calculateAverage(scores)))
    