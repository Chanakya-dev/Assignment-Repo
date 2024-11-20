# Python Assignment: Student Grades and Overall Performance

## Problem Statement

Write a Python program to calculate the grades and overall performance of a student based on the scores obtained in individual subjects.

### Input
1. **Student Name**: A string representing the student's name.
2. **Number of Subjects**: An integer representing the number of subjects.
3. **Subject Names and Scores**: For each subject, the program will take two inputs: the subject name and the score obtained in that subject.

### Output
1. Individual grades for each subject based on the following grading criteria:
   - **90-100**: A+
   - **80-89**: A
   - **70-79**: B
   - **60-69**: C
   - **50-59**: D
   - **Below 50**: Fail
2. Total marks obtained by the student.
3. Percentage of marks.
4. Final grade based on the percentage:
   - **90-100**: Outstanding
   - **80-89**: Excellent
   - **70-79**: Good
   - **60-69**: Average
   - **50-59**: Pass
   - **Below 50**: Fail

### Example Input
```python
Enter the student's name: Alice
Enter the number of subjects: 5
Enter the subject name: Mathematics
Enter the score for Mathematics: 85

Enter the subject name: Physics
Enter the score for Physics: 78

Enter the subject name: Chemistry
Enter the score for Chemistry: 92

Enter the subject name: Biology
Enter the score for Biology: 67

Enter the subject name: English
Enter the score for English: 73
```
Output

- Student Name: Alice

Subject-wise Grades:
- Mathematics: A
- Physics: B
- Chemistry: A+
- Biology: C
- English: B

Total Marks: 395
Percentage: 79.0%
Final Grade: Good
