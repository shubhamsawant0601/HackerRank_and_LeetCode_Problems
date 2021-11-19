"""
Sample Input 0

4
73
67
38
33
Sample Output 0

75
67
40
33

Student 1 received a 73, and the next multiple of 5 from  73 is 75. Since 75-73<3 , the student's grade is rounded to 75.
Student 2 received a 67, and the next multiple of 5 from 67 is 70. Since 70-67=3, the grade will not be modified and the student's final grade is 67.
Student 3 received a 38, and the next multiple of 5 from 38 is 40. Since 40-38<3, the student's grade will be rounded to 40.
Student 4 received a grade below 33, so the grade will not be modified and the student's final grade is 33.
"""

def gradingStudents(grades):
    result = []
    
    for grade in grades:
        if grade<38:
            result.append(grade)
        elif (grade+1)%5==0 :
            result.append(grade+1)
        elif (grade+2)%5==0:
            result.append(grade+2)
        else:
            result.append(grade)
            
    return result