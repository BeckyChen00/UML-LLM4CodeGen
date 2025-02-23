"""
# 简易的教务系统，能够实现以下功能：
# 1）管理学生基本信息，学生信息包含学生编号、姓名等信息。
# 2）管理学生的课程信息，包括课程编号、课程名称、课程学分、课程简介等信息。
# 3）管理学生所选的每门课程的选课时间和成绩。同一门课程可以重复选修多次。记录最高成绩为该课程的成绩。
# 4）查询学生所修的所有课程。
# 5）查询学生所修的某一门课程的成绩。
# 4）计算学生已获得的总学分。每门课成绩大于等于60分，学分才能算入总学分。 
# 5）计算学生选修的每门课程的绩点。成绩在60分以下、60分-70分（含70分）、70分-80分（含80分）、80分以上，那对应的绩点就是0、2、3、4的标准。
# 6）计算学生所获得的平均绩点。平均绩点=（课程1绩点*课程1学分+课程2绩点*课程2学分+...）/（课程1学分+课程2学分+...）。
"""
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
1) Manage student information, including student ID, name.
2) Manage course information, including course ID, course name, course credits, and course description.
3) Manage students' course enroll time and grades. The student can take the same course multiple times.
4) Query all the unique courses taken by a student.
5) Calculate a course grade, which is the highest score the student have earned.
6) Calculate the credits earned by a student. The credit of a unique course is only counted toward the result if the course grade is 60 or above.
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