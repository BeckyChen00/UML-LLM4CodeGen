# Version 1.1
## Description:

A simple educational management system that can implement the following functions:
1) Record student details, encompassing student ID and name.
2) Handle course specifics, which include course ID, course name, course credits, and course overview.
3) Keep track of students' course enrollment times and grades, allowing students to retake the same course multiple times.
4) Retrieve all the distinct courses enrolled by a student.
5) Canculate a unique course grade as the highest mark obtained by the student.
6) Canculate the total credits accumulated by a student, where only the credit of a unique course counts if the course grade is 60 or more.

## UML:

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

## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Below is the complete Java code for the educational management system based on the provided functional requirements and UML class diagram. The code includes the `Student`, `Course`, and `Enrollment` classes, along with the necessary methods and business logic implementations.

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credits
    private String description; // Course Overview

    // Constructor
    public Course(String cid, String name, double credit, String description) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.description = description;
    }

    // Getter for credit
    public double getCredit() {
        return credit;
    }

    // Getter for course ID
    public String getCid() {
        return cid;
    }

    // Getter for course name
    public String getName() {
        return name;
    }
}

class Enrollment {
    private double score; // Score obtained in the course
    private Course enrolledCourse; // The course the student is enrolled in

    // Constructor
    public Enrollment(double score, Course enrolledCourse) {
        this.score = score;
        this.enrolledCourse = enrolledCourse;
    }

    // Getter for score
    public double getScore() {
        return score;
    }

    // Getter for enrolled course
    public Course getEnrolledCourse() {
        return enrolledCourse;
    }
}

class Student {
    private String sid; // Student ID
    private String name; // Student Name
    private List<Enrollment> enrollments; // List of enrollments

    // Constructor
    public Student(String sid, String name) {
        this.sid = sid;
        this.name = name;
        this.enrollments = new ArrayList<>();
    }

    // Method to calculate accumulated credits
    public double calculateAccumulatedCredits() {
        Map<String, Double> uniqueCourses = new HashMap<>();
        
        for (Enrollment enrollment : enrollments) {
            Course course = enrollment.getEnrolledCourse();
            double score = enrollment.getScore();
            if (score >= 60) {
                uniqueCourses.put(course.getCid(), course.getCredit());
            }
        }
        
        double totalCredits = 0;
        for (double credit : uniqueCourses.values()) {
            totalCredits += credit;
        }
        
        return totalCredits;
    }

    // Method to retrieve unique courses enrolled
    public List<Course> retrieveUniqueCoursesEnrolled() {
        List<Course> uniqueCourses = new ArrayList<>();
        Map<String, Course> courseMap = new HashMap<>();
        
        for (Enrollment enrollment : enrollments) {
            Course course = enrollment.getEnrolledCourse();
            if (!courseMap.containsKey(course.getCid())) {
                courseMap.put(course.getCid(), course);
                uniqueCourses.add(course);
            }
        }
        
        return uniqueCourses;
    }

    // Method to calculate the highest course grade for a specific course
    public double calculateCourseGrade(Course course) {
        double highestScore = 0;
        
        for (Enrollment enrollment : enrollments) {
            if (enrollment.getEnrolledCourse().getCid().equals(course.getCid())) {
                double score = enrollment.getScore();
                if (score > highestScore) {
                    highestScore = score;
                }
            }
        }
        
        return highestScore;
    }

    // Method to add enrollment
    public void enrollInCourse(double score, Course course) {
        enrollments.add(new Enrollment(score, course));
    }

    // Getters for student details
    public String getSid() {
        return sid;
    }

    public String getName() {
        return name;
    }
}

// Example usage
public class EducationalManagementSystem {
    public static void main(String[] args) {
        // Create courses
        Course math = new Course("C001", "Mathematics", 3.0, "Basic Mathematics Course");
        Course science = new Course("C002", "Science", 4.0, "Basic Science Course");

        // Create a student
        Student student = new Student("S001", "John Doe");

        // Enroll student in courses with scores
        student.enrollInCourse(75, math); // First attempt in Mathematics
        student.enrollInCourse(85, math); // Retake in Mathematics
        student.enrollInCourse(55, science); // Attempt in Science

        // Calculate accumulated credits
        double accumulatedCredits = student.calculateAccumulatedCredits();
        System.out.println("Accumulated Credits: " + accumulatedCredits);

        // Retrieve unique courses enrolled
        List<Course> uniqueCourses = student.retrieveUniqueCoursesEnrolled();
        System.out.println("Unique Courses Enrolled:");
        for (Course course : uniqueCourses) {
            System.out.println(course.getName());
        }

        // Calculate highest grade for Mathematics
        double highestMathGrade = student.calculateCourseGrade(math);
        System.out.println("Highest Grade in Mathematics: " + highestMathGrade);
    }
}
```

### Explanation:
1. **Classes**: The code defines three classes: `Course`, `Enrollment`, and `Student`.
2. **Properties**: Each class has private properties as per the UML diagram.
3. **Methods**: The methods are implemented according to the functional requirements:
   - `calculateAccumulatedCredits()` calculates the total credits for courses where the student scored 60 or more.
   - `retrieveUniqueCoursesEnrolled()` retrieves a list of unique courses the student has enrolled in.
   - `calculateCourseGrade(Course course)` calculates the highest score obtained by the student in a specific course.
4. **Enrollment**: The `enrollInCourse(double score, Course course)` method allows adding enrollments for a student.
5. **Example Usage**: The `main` method demonstrates how to create courses, enroll a student, and use the methods to calculate credits and retrieve courses.

This code is structured, follows Java best practices, and is ready for further enhancements or integration into a larger system.

--------------------------------------------------
# Version 1.0
## Description:

A simple educational management system that can implement the following functions:
1) Record student details, encompassing student ID and name.
2) Handle course specifics, which include course ID, course name, course credits, and course overview.
3) Keep track of students' course enrollment times and grades, allowing students to retake the same course multiple times.
4) Retrieve all the distinct courses enrolled by a student.
5) Canculate a unique course grade as the highest mark obtained by the student.
6) Canculate the total credits accumulated by a student, where only the credit of a unique course counts if the course grade is 60 or more.

## UML:
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Based on the provided functional requirements for the educational management system, I will create a Java implementation that includes classes for `Student`, `Course`, and `Enrollment`. The code will encapsulate the required functionalities as described.

Here is the complete Java code:

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// Class representing a Course
class Course {
    private String courseId;
    private String courseName;
    private int courseCredits;
    private String courseOverview;

    public Course(String courseId, String courseName, int courseCredits, String courseOverview) {
        this.courseId = courseId;
        this.courseName = courseName;
        this.courseCredits = courseCredits;
        this.courseOverview = courseOverview;
    }

    public String getCourseId() {
        return courseId;
    }

    public String getCourseName() {
        return courseName;
    }

    public int getCourseCredits() {
        return courseCredits;
    }

    public String getCourseOverview() {
        return courseOverview;
    }
}

// Class representing a Student
class Student {
    private String studentId;
    private String name;
    private List<Enrollment> enrollments;

    public Student(String studentId, String name) {
        this.studentId = studentId;
        this.name = name;
        this.enrollments = new ArrayList<>();
    }

    public String getStudentId() {
        return studentId;
    }

    public String getName() {
        return name;
    }

    public void enrollInCourse(Course course, int grade) {
        enrollments.add(new Enrollment(this, course, grade));
    }

    public List<Course> getDistinctCourses() {
        Map<String, Course> distinctCourses = new HashMap<>();
        for (Enrollment enrollment : enrollments) {
            distinctCourses.put(enrollment.getCourse().getCourseId(), enrollment.getCourse());
        }
        return new ArrayList<>(distinctCourses.values());
    }

    public int calculateUniqueCourseGrade() {
        Map<String, Integer> highestGrades = new HashMap<>();
        for (Enrollment enrollment : enrollments) {
            String courseId = enrollment.getCourse().getCourseId();
            int grade = enrollment.getGrade();
            highestGrades.put(courseId, Math.max(highestGrades.getOrDefault(courseId, 0), grade));
        }
        return highestGrades.values().stream().mapToInt(Integer::intValue).max().orElse(0);
    }

    public int calculateTotalCredits() {
        int totalCredits = 0;
        Map<String, Integer> uniqueCourses = new HashMap<>();
        for (Enrollment enrollment : enrollments) {
            String courseId = enrollment.getCourse().getCourseId();
            int grade = enrollment.getGrade();
            if (grade >= 60 && !uniqueCourses.containsKey(courseId)) {
                uniqueCourses.put(courseId, enrollment.getCourse().getCourseCredits());
                totalCredits += enrollment.getCourse().getCourseCredits();
            }
        }
        return totalCredits;
    }
}

// Class representing an Enrollment
class Enrollment {
    private Student student;
    private Course course;
    private int grade;

    public Enrollment(Student student, Course course, int grade) {
        this.student = student;
        this.course = course;
        this.grade = grade;
    }

    public Student getStudent() {
        return student;
    }

    public Course getCourse() {
        return course;
    }

    public int getGrade() {
        return grade;
    }
}

// Main class to demonstrate the functionality
public class EducationalManagementSystem {
    public static void main(String[] args) {
        // Create courses
        Course math = new Course("C001", "Mathematics", 3, "An introduction to Mathematics.");
        Course science = new Course("C002", "Science", 4, "An introduction to Science.");
        Course history = new Course("C003", "History", 2, "An overview of world history.");

        // Create a student
        Student student1 = new Student("S001", "John Doe");

        // Enroll student in courses with grades
        student1.enrollInCourse(math, 75);
        student1.enrollInCourse(science, 85);
        student1.enrollInCourse(math, 90); // Retake
        student1.enrollInCourse(history, 55); // Below passing grade

        // Retrieve distinct courses
        List<Course> distinctCourses = student1.getDistinctCourses();
        System.out.println("Distinct Courses Enrolled by " + student1.getName() + ":");
        for (Course course : distinctCourses) {
            System.out.println(course.getCourseName());
        }

        // Calculate unique course grade
        int uniqueCourseGrade = student1.calculateUniqueCourseGrade();
        System.out.println("Highest Grade Obtained: " + uniqueCourseGrade);

        // Calculate total credits
        int totalCredits = student1.calculateTotalCredits();
        System.out.println("Total Credits Accumulated: " + totalCredits);
    }
}
```

### Explanation of the Code:
1. **Course Class**: Represents a course with properties like `courseId`, `courseName`, `courseCredits`, and `courseOverview`.
2. **Student Class**: Represents a student with properties like `studentId`, `name`, and a list of `enrollments`. It includes methods to enroll in courses, retrieve distinct courses, calculate the highest grade, and calculate total credits.
3. **Enrollment Class**: Represents the relationship between a student and a course, including the grade received.
4. **EducationalManagementSystem Class**: Contains the `main` method to demonstrate the functionality of the system by creating courses, enrolling a student, and displaying results.

This implementation adheres to the functional requirements and provides a clear structure for the educational management system.

--------------------------------------------------
