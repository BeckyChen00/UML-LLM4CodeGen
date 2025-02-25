"""
高校教师课程教学管理系统，能够实现以下功能：
1）管理教师数据，教师数据包含教师编号、姓名、性别、职称（教授/副教授/讲师）、基本工资等信息。
2）管理教师的课程信息，包括课程编号、课程名称、学分、学时、课程类型（选修/必修）等信息。
3）计算教师的工资，工资计算规则为：工资=基本工资+课时费*计费学时。注意：一个老师可以教多门课程。
4）课时费用根据教师的职称不同而不同，教授每学时100元，副教授每学时80元，讲师每学时50元。
5）计费学时根据课程类型不同而不同，必修课每课时2学时，选修课每课时1学时。

"""
# University_description

description = """
The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information many teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.
"""

version1List = [
    "2) Manage courses information many teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.",
    "2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.",
    "2) Manage courses information every teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.",
    "2) Manage courses information each teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.",
    "2) Manage what courses a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.",
    "2) Record courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.",
    "2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information. Note that a teacher can teach multiple courses.",
]

uml = """
```plantuml
    @startuml
        note:  class diagram

        enum ProfessionalTitle {
            fullProfessor
            associateProfessor
            assistantProfessor
        }

        enum CourseType{
            compulsory
            elective
        }

        class Teacher {
            - string tid
            - string name
            - boolean sex
            - ProfessionalTitle professionalTitle
            - double basicSalary

            + double calculateSalary()
            + double getCourseFeePerHour()
        }

        class Course {
            - string cid
            - string name
            - double credit
            - double hours
            - CourseType type

            + double getBilledHours()
        }

        {version2}
    @enduml
```"""

version2List = [
    f"Teacher \"1\" *-- \"0..*\" Course: taughtCourses",
    f"Teacher \"1\" *-- \"0..*\" Course",
    f"Teacher \"1\" --> \"0..*\" Course",
    f"Teacher \"1\" *-- \"0..*\" Course: taught",
    f"Teacher \"1\" *-- \"0..*\" Course: courses",
    f"Teacher \"1\" *-- \"0..*\" Course: teaches",
    f"Teacher \"1\" --> \"0..*\" Course: taughtCourses",
]
