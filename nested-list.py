def returnScore(element):
    return element[1]

def printStudentsByValue(records):
    # Find second lowest grade
    secondLowestScore = sorted(set(student[1] for student in records))[1]

    # Extracting names of students by second lowest grade
    secondLowestStudents = [student[0] for student in records if student[1] == secondLowestScore]
    
    # Sorting the names alphabetically
    secondLowestStudents.sort()

    # Print the names of students with second lowest grade
    for student in secondLowestStudents:
        print(student)

if __name__ == '__main__':
    arrResp = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arrResp.append([name, score])
    printStudentsByValue(arrResp)