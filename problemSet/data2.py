# 自创数据集

# 7) Calculate the grade point for each course taken by a student. The grade point is determined as follows:
#     - Below 60: Grade point = 0
#     - 60-70 (inclusive): Grade point = 2
#     - 70-80 (inclusive): Grade point = 3
#     - Above 80: Grade point = 4
# 8) Calculate the student's average grade point. The average grade point is calculated as:
# Average Grade Point= (Grade Point of Course 1 * Credit of Course 1 + Grade Point of Course 2 * Credit of Course 2 + ...) / (Credit of Course 1 + Credit of Course 2 + ...)  

# educational management system

descriptionList =[ """
A simple educational management system that can implement the following functions:
1) Record student details, encompassing student ID and name.
2) Handle course specifics, which include course ID, course name, course credits, and course overview.
3) Keep track of students' course enrollment times and grades, allowing students to retake the same course multiple times.
4) Retrieve all the distinct courses enrolled by a student.
5) Canculate a unique course grade as the highest mark obtained by the student.
6) Canculate the total credits accumulated by a student, where only the credit of a unique course counts if the course grade is 60 or more.
""",
"""
A simple educational management system that can implement the following functions:
1) Record student details, encompassing student ID and name.
2) Handle course specifics, which include course ID, course name, course credits, and course overview.
3) Keep track of students' course enrollment times and grades, allowing students to retake the same course multiple times.
4) Retrieve all the distinct courses enrolled by a student.
5) Canculate a unique course grade as the highest mark obtained by the student.
6) Canculate the total credits accumulated by a student, where only the credit of a unique course counts if the course grade is 60 or more.
7) Calculate the student's average grade point. The average grade point is calculated as: Average Grade Point= (Grade Point of Course 1 * Credit of Course 1 + Grade Point of Course 2 * Credit of Course 2 + ...) / (Credit of Course 1 + Credit of Course 2 + ...) 
""",

]



umlList = [
    """
```plantuml
@startuml
note:  class diagram

class Student {
    - string sid
    - string name

    + double calculateAccumulatedCredits()
    + List<Course> retrieveUniqueCoursesEnrolled()
    + double calculateCourseGrade(Course course)
}

class Course {
    - string cid
    - string name
    - double credit
    - string description

    + double getCredit()
}

class Enrollment {
    - double score    
}

Student "1" *-- "0..*" Enrollment : enrollment
Enrollment "*" --> "1" Course : enrolledCourse

@enduml
```
""",
"""
```plantuml
@startuml
note:  class diagram

class Student {
    - string sid
    - string name

    + double calculateEarnedCredits()
    + List<Course> queryUniqueCoursesEnrolled()
    + double calculateCourseGrade(Course course)
}

class Course {
    - string cid
    - string name
    - double credit
    - string description

    + double getCredit()
}

class Enrollment {
    - double score    
}

Student "1" *-- "0..*" Enrollment : enrollment
Enrollment "*" --> "1" Course : course

@enduml
```
""",
]