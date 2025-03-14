descriptionList=["""The system functional requirements are as follows:
1) Student Management. A student is identified by a student ID and can enroll in multiple courses.
2) Teaching Assistant Management. The TA has the first name and last name. A TA has a first name and last name and can assist in multiple courses. 
3) TAs can review in the system the assignment details and assignment responsibilities. 
4) Course Management. Each course has a unique course id. A course can have many teaching assistants.  A TA can assist in multiple courses.
5) Lab Section Management. Each lab section has specific start time, end time, and locations. Each course has multiple lab sections.
                 
6) A student can enroll in a Lab section of a course if it does not overlap with another lab section they are already enrolled in.
7) A student can view all courses their enrolled, including the lab sections and teaching assitants information. 
8) A course can add a new LabSection if the new LabSection does not overlap with other existing lab sections.
9) A course can assign a TA to an existed lab section if the TA assigned courses have overlapping times.
10) TAs can view all courses they are assigned to, including lab sections, student lists, assignment details, and assignment responsibilities.
11) Students can view their course schedule, including all courses informtion they are enrolled in.""",
 ]

umlList = ["""
```plantuml
@startuml

class Student {
    - string ID
    
  + void enrollInCourse(course: Course)
  + void getEnrolledCourses()
}

class Course {
    - string id

    + addLabSection(lab: LabSection)
    + assignTAToLabSection(ta: TeachingAssistant, lab: LabSection)       
}

class TeachingAssistant {
    - string FirstName
    - string LastName
           
    + viewAllLabSection()
    + viewAssignmentDetails(): List<Assignment>
    + assignToLabSection(lab: LabSection)
}

class LabSection {
    - int StartTime
    - int EndTime
    - string Location
           
    + addStudent(student: Student)
    + addTA(ta: TA)
    + getEnrolledStudents(): List<Student>
    + getAssignedTAs(): List<TeachingAssistant>
}


class Assignment {
    - string details
    - string responsibilities
}
           
 
Student "*" -- "*" Course
           
TeachingAssistant "*" -- "*" Course
Course "1" *-- "1..*" LabSection

(Course, TeachingAssistant) .. Assignment

@enduml
```
"""]