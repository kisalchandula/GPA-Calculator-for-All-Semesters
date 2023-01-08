#  16GES900 - K.C Wijeyesekera  GPA with grades

finalGpa = 0
gpa = 0
grades = []
semesterGpa = []
semesterCredits = []

s = int(input("Enter number of semesters to calculate GPA: "))
for i in range(0, s):
    n = int(input("\nEnter number of subjects for" + " semester-" + str(i + 1) + ": "))
    print("\n*** Enter semester-" + str(i + 1) + " marks ***")

    gradePoints = 0.0  # (credits*points)
    totalGP = 0.0  # Total grade points
    totalCredit = 0.0
    totalGpa = 0.0
    for j in range(0, n):
        marks = int(input("\nPlease enter the marks for subject-" + str(j + 1) + ": "))
        credit = int(input("Please enter the subject credits: "))
        if 90 <= marks:
            gradePoints = float(credit) * 4.0
            grades.append('A+')
        elif 80 <= marks < 90:
            gradePoints = float(credit) * 4.0
            grades.append('A')
        elif 75 <= marks < 80:
            gradePoints = float(credit) * 3.7
            grades.append('A-')
        elif 70 <= marks < 75:
            gradePoints = float(credit) * 3.3
            grades.append('B+')
        elif 65 <= marks < 70:
            gradePoints = float(credit) * 3.0
            grades.append('B')
        elif 60 <= marks < 65:
            gradePoints = float(credit) * 2.7
            grades.append('B-')
        elif 55 <= marks < 60:
            gradePoints = float(credit) * 2.3
            grades.append('C+')
        elif 50 <= marks < 55:
            gradePoints = float(credit) * 2.0
            grades.append('C')
        elif 45 <= marks < 50:
            gradePoints = float(credit) * 1.7
            grades.append('C-')
        elif 40 <= marks < 45:
            gradePoints = float(credit) * 1.3
            grades.append('D+')
        elif 30 <= marks < 40:
            gradePoints = float(credit) * 1.0
            grades.append('D')
        elif marks < 30:
            gradePoints = 0.0
            grades.append('E')

        totalCredit = totalCredit + float(credit)
        totalGP += gradePoints
        totalGpa = totalGP / totalCredit  # semester gpa

    semesterGpa.append(totalGpa)
    semesterCredits.append(totalCredit)

# final gpa
for i in range(len(semesterGpa)):
    gpa = float(semesterGpa[i] * semesterCredits[i])
    finalGpa += gpa
finalGpa = finalGpa / sum(semesterCredits)
print("\nFinal GPA is " + str(format(round(finalGpa, 2), '.2f')))

# grades
for i in range(len(grades)):
    print(str(i + 1) + "- subject grade: " + grades[i])
