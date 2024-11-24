# <!-- # Python Assignment: Student Grades and Overall Performance

# ## Problem Statement

# Write a Python program to calculate the grades and overall performance of a student based on the scores obtained in individual subjects.

# ### Input
# 1. **Student Name**: A string representing the student's name.
# 2. **Number of Subjects**: An integer representing the number of subjects.
# 3. **Subject Names and Scores**: For each subject, the program will take two inputs: the subject name and the score obtained in that subject.

# ### Output
# 1. Individual grades for each subject based on the following grading criteria:
#    - **90-100**: A+
#    - **80-89**: A
#    - **70-79**: B
#    - **60-69**: C
#    - **50-59**: D
#    - **Below 50**: Fail
# 2. Total marks obtained by the student.
# 3. Percentage of marks.
# 4. Final grade based on the percentage:
#    - **90-100**: Outstanding
#    - **80-89**: Excellent
#    - **70-79**: Good
#    - **60-69**: Average
#    - **50-59**: Pass
#    - **Below 50**: Fail

# ### Example Input
# ```python
# Enter the student's name: Alice
# Enter the number of subjects: 5
# Enter the subject name: Mathematics
# Enter the score for Mathematics: 85

# Enter the subject name: Physics
# Enter the score for Physics: 78

# Enter the subject name: Chemistry
# Enter the score for Chemistry: 92

# Enter the subject name: Biology
# Enter the score for Biology: 67

# Enter the subject name: English
# Enter the score for English: 73
# ```
# Output

# - Student Name: Alice

# Subject-wise Grades:
# - Mathematics: A
# - Physics: B
# - Chemistry: A+
# - Biology: C
# - English: B

# Total Marks: 395
# Percentage: 79.0%
# Final Grade: Good -->



Name = input("Enter your name: ")
Student_ID = input("Enter your ID: ")
print(Name)
print(Student_ID)

print("NOW KNOW YOUR GRADES")


def grade(n):

    if n <= 100 and n > 90:
        return "A"
    elif n <= 90 and n > 80:
        return "B"
    elif n <= 80 and n > 70:
        return "C"
    elif n <= 70 and n > 60:
        return "D"
    elif n <= 60 and n > 50:
        return "E"
    elif n <= 50 and n > 0:
       return "F"
    else:
        return "INVALID"
def overall(n) :
    if n<=500 and n>400:
        return 'A'
    elif n<=400 and n>300:
        return 'B'
    elif n<=300 and n>200:
        return 'c'
    elif n<=200 and n>100:
        return 'D'
    elif n <= 100 and n > 0:
       return "F"
    else :
        print("Invalid")
    
 


print("The overall garde and the average of all the subjects are: ")

MATH = int(input("Enter marks for MATH (out of 100): "))
print("the grade of MATHS is ",grade(MATH))
PHY = int(input("Enter marks for PHY (out of 100): "))
print("the grade of PHY is ",grade(PHY))
CHEM = int(input("Enter marks for CHEM (out of 100): "))
print("the grade of CHEM is ",grade(CHEM))
ENG = int(input("Enter marks for ENG (out of 100): "))
print("the grade of ENG is ",grade(ENG))
BIO = int(input("Enter marks for BIO (out of 100): "))
print("the grade of BIO is ",grade(BIO))

total_marks = MATH + PHY + CHEM + ENG + BIO
print("The total marks are : ",total_marks)

print("THE AVERAGE")
average_marks = total_marks / 5
print("Average marks:", average_marks)

print("Overall grade based on average marks:", grade(average_marks))

print("THE OVERALL GARDE: ")


print("Overall grade based on total marks:", overall(total_marks))



