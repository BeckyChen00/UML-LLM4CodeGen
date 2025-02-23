# version 1.1
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information many teacher teach, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram:

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // List of courses taught by the teacher
    private List<Course> taughtCourses = new ArrayList<>();

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get the billed hours based on course type
    public double getBilledHours() {
        switch (type) {
            case compulsory:
                return hours * 2; // 2 hours per class hour for compulsory courses
            case elective:
                return hours; // 1 hour per class hour for elective courses
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher1 = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);

        // Add courses to the teacher
        teacher1.addCourse(course1);
        teacher1.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher1.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details, methods to calculate salary, and to get the course fee per hour. It also maintains a list of courses taught by the teacher.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, method naming conventions, and proper use of collections.

--------------------------------------------------
# version 1.2
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information many teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary(Course[] courses) {
        double totalSalary = basicSalary;
        for (Course course : courses) {
            totalSalary += course.getBilledHours() * getCourseFeePerHour();
        }
        return totalSalary;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForAlice = {course1, course2};
        double salaryAlice = teacher1.calculateSalary(coursesForAlice);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salaryAlice);
        
        Course[] coursesForBob = {course1};
        double salaryBob = teacher2.calculateSalary(coursesForBob);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salaryBob);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate the salary based on the courses taught and to get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate the billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and comments for clarity.

--------------------------------------------------
# version 1.3
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information many teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary(Course[] courses) {
        double totalSalary = basicSalary;
        for (Course course : courses) {
            totalSalary += getCourseFeePerHour() * course.getBilledHours();
        }
        return totalSalary;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours * 1; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate the salary based on the courses taught and to get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate the billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation and method naming conventions.

--------------------------------------------------
# version 1.4
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information many teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taught
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram:

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary(Course[] courses) {
        double totalSalary = basicSalary;
        for (Course course : courses) {
            totalSalary += course.getBilledHours() * getCourseFeePerHour();
        }
        return totalSalary;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters for Teacher properties
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters for Course properties
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation and method naming conventions.

--------------------------------------------------
# version 1.5
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information many teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: courses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's list
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        return (type == CourseType.COMPULSORY) ? hours * 2 : hours;
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.FULL_PROFESSOR, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.ELECTIVE);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details, a list of courses, and methods to calculate salary and course fees.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on course type.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and proper use of collections.

--------------------------------------------------
# version 1.6
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information many teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: teaches
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary(Course[] courses) {
        double totalSalary = basicSalary;
        for (Course course : courses) {
            totalSalary += course.getBilledHours() * getCourseFeePerHour();
        }
        return totalSalary;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters for Teacher properties
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type (compulsory or elective)

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters for Course properties
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate the salary based on courses taught and to get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation and clear method definitions.

--------------------------------------------------
# version 1.7
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information many teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary(Course[] taughtCourses) {
        double totalSalary = basicSalary;
        for (Course course : taughtCourses) {
            totalSalary += getCourseFeePerHour() * course.getBilledHours();
        }
        return totalSalary;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Example usage
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] taughtCourses1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(taughtCourses1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] taughtCourses2 = {course1};
        double salary2 = teacher2.calculateSalary(taughtCourses2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate the salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates how to create instances of `Teacher` and `Course`, and how to calculate and display the salaries of teachers based on the courses they teach.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and proper use of enums.

--------------------------------------------------
# version 1.0
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information many teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Based on the provided functional requirements for the teaching management system, I will create a Java implementation that includes classes for managing teachers and courses, as well as methods for calculating salaries according to the specified rules. Below is the complete Java code:

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Title
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Class representing a Teacher
class Teacher {
    private String teacherNumber;
    private String name;
    private String gender;
    private ProfessionalTitle title;
    private double basicSalary;
    private List<Course> courses;

    public Teacher(String teacherNumber, String name, String gender, ProfessionalTitle title, double basicSalary) {
        this.teacherNumber = teacherNumber;
        this.name = name;
        this.gender = gender;
        this.title = title;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    // Method to add a course to the teacher
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.calculateCourseFee(this.title);
        }
        return basicSalary + totalCourseFee;
    }

    // Getters and Setters
    public String getTeacherNumber() {
        return teacherNumber;
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }

    public ProfessionalTitle getTitle() {
        return title;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Class representing a Course
class Course {
    private String courseNumber;
    private String courseName;
    private int credit;
    private int classHours;
    private boolean isCompulsory;

    public Course(String courseNumber, String courseName, int credit, int classHours, boolean isCompulsory) {
        this.courseNumber = courseNumber;
        this.courseName = courseName;
        this.credit = credit;
        this.classHours = classHours;
        this.isCompulsory = isCompulsory;
    }

    // Method to calculate the course fee based on teacher's title
    public double calculateCourseFee(ProfessionalTitle title) {
        double courseFeePerHour = 0.0;
        int billedHours = isCompulsory ? classHours * 2 : classHours;

        switch (title) {
            case FULL_PROFESSOR:
                courseFeePerHour = 100.0;
                break;
            case ASSOCIATE_PROFESSOR:
                courseFeePerHour = 80.0;
                break;
            case ASSISTANT_PROFESSOR:
                courseFeePerHour = 50.0;
                break;
        }
        return courseFeePerHour * billedHours;
    }

    // Getters and Setters
    public String getCourseNumber() {
        return courseNumber;
    }

    public String getCourseName() {
        return courseName;
    }

    public int getCredit() {
        return credit;
    }

    public int getClassHours() {
        return classHours;
    }

    public boolean isCompulsory() {
        return isCompulsory;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create teachers
        Teacher teacher1 = new Teacher("T001", "Alice", "Female", ProfessionalTitle.FULL_PROFESSOR, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", "Male", ProfessionalTitle.ASSOCIATE_PROFESSOR, 4000);
        
        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, true); // Compulsory
        Course course2 = new Course("C002", "History", 2, 5, false); // Elective
        
        // Assign courses to teachers
        teacher1.addCourse(course1);
        teacher1.addCourse(course2);
        teacher2.addCourse(course1);
        
        // Calculate and display salaries
        System.out.println("Salary of " + teacher1.getName() + ": $" + teacher1.calculateSalary());
        System.out.println("Salary of " + teacher2.getName() + ": $" + teacher2.calculateSalary());
    }
}
```

### Explanation of the Code:
1. **Enums**: `ProfessionalTitle` is an enumeration that defines the different professional titles a teacher can have.
2. **Teacher Class**: This class contains properties for teacher information and methods to add courses and calculate salary.
3. **Course Class**: This class contains properties for course information and a method to calculate the course fee based on the teacher's title and course type.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating instances of `Teacher` and `Course`, assigning courses to teachers, and calculating their salaries.

### Comments:
- The code is structured to follow Java best practices, including encapsulation and clear method definitions.
- Each class has appropriate getters and setters to access private fields.
- The salary calculation logic is implemented according to the specified rules.

--------------------------------------------------
# version 2.8
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type (compulsory/elective)

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details, a list of courses taught, and methods to calculate salary and course fees.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on course type.
4. **Main Class**: Demonstrates the creation of a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful method names, and comments for clarity.

--------------------------------------------------
# version 2.9
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalSalary = basicSalary;
        for (Course course : courses) {
            totalSalary += getCourseFeePerHour() * course.getBilledHours();
        }
        return totalSalary;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters for Teacher properties
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type (Compulsory or Elective)

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters for Course properties
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", false, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", true, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForAlice = {course1, course2};
        double salaryAlice = teacher1.calculateSalary(coursesForAlice);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salaryAlice);
        
        Course[] coursesForBob = {course1};
        double salaryBob = teacher2.calculateSalary(coursesForBob);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salaryBob);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation and method naming conventions.

--------------------------------------------------
# version 2.10
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;

        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }

        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and proper use of enums.

--------------------------------------------------
# version 2.11
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taught
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0; // Default case (should not occur)
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        switch (type) {
            case COMPULSORY:
                return hours * 2; // 2 hours per class hour for compulsory courses
            case ELECTIVE:
                return hours; // 1 hour per class hour for elective courses
            default:
                return 0.0; // Default case (should not occur)
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Example usage
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", false, ProfessionalTitle.FULL_PROFESSOR, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", true, ProfessionalTitle.ASSOCIATE_PROFESSOR, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.ELECTIVE);
        
        // Calculate salaries
        Course[] coursesForAlice = {course1, course2};
        double salaryAlice = teacher1.calculateSalary(coursesForAlice);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salaryAlice);
        
        Course[] coursesForBob = {course1};
        double salaryBob = teacher2.calculateSalary(coursesForBob);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salaryBob);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get course fees based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: An example usage of the `Teacher` and `Course` classes is provided in the `TeachingManagementSystem` class, demonstrating how to create instances and calculate salaries.

This code adheres to Java coding standards and best practices, including encapsulation and method naming conventions.

--------------------------------------------------
# version 2.12
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: courses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours * 1; // 1 hour per class hour for elective courses
        }
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Professional Title
    private double basicSalary; // Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>(); // Initialize the courses list
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee; // Total salary calculation
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0; // $100 per class hour for full professors
            case associateProfessor:
                return 80.0; // $80 per class hour for associate professors
            case assistantProfessor:
                return 50.0; // $50 per class hour for assistant professors
            default:
                return 0.0; // Default case
        }
    }

    // Method to add a course to the teacher's list of courses
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 2.13
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: teaches
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", false, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", true, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and proper use of enums.

--------------------------------------------------
# version 2.14
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram:

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details, methods to calculate salary, get course fee per hour, and manage courses taught by the teacher.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, method naming conventions, and proper use of collections.

--------------------------------------------------
# version 2.0
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Based on the provided functional requirements for the teaching management system, I will create a Java implementation that includes classes for managing teacher data and course information, as well as methods for calculating salaries according to the specified rules.

Here is the complete Java code:

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Title
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Class representing a Teacher
class Teacher {
    private String teacherNumber;
    private String name;
    private String gender;
    private ProfessionalTitle title;
    private double basicSalary;
    private List<Course> courses;

    public Teacher(String teacherNumber, String name, String gender, ProfessionalTitle title, double basicSalary) {
        this.teacherNumber = teacherNumber;
        this.name = name;
        this.gender = gender;
        this.title = title;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    // Method to add a course to the teacher's list
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.calculateCourseFee(title);
        }
        return basicSalary + totalCourseFee;
    }

    // Getters and Setters
    public String getTeacherNumber() {
        return teacherNumber;
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }

    public ProfessionalTitle getTitle() {
        return title;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Class representing a Course
class Course {
    private String courseNumber;
    private String courseName;
    private int credit;
    private int classHours;
    private boolean isCompulsory;

    public Course(String courseNumber, String courseName, int credit, int classHours, boolean isCompulsory) {
        this.courseNumber = courseNumber;
        this.courseName = courseName;
        this.credit = credit;
        this.classHours = classHours;
        this.isCompulsory = isCompulsory;
    }

    // Method to calculate the course fee based on the teacher's title
    public double calculateCourseFee(ProfessionalTitle title) {
        double courseFeePerHour;
        switch (title) {
            case FULL_PROFESSOR:
                courseFeePerHour = 100.0;
                break;
            case ASSOCIATE_PROFESSOR:
                courseFeePerHour = 80.0;
                break;
            case ASSISTANT_PROFESSOR:
                courseFeePerHour = 50.0;
                break;
            default:
                throw new IllegalArgumentException("Unknown professional title: " + title);
        }

        // Calculate billed hours based on course type
        int billedHours = isCompulsory ? classHours * 2 : classHours;
        return courseFeePerHour * billedHours;
    }

    // Getters and Setters
    public String getCourseNumber() {
        return courseNumber;
    }

    public String getCourseName() {
        return courseName;
    }

    public int getCredit() {
        return credit;
    }

    public int getClassHours() {
        return classHours;
    }

    public boolean isCompulsory() {
        return isCompulsory;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", "Male", ProfessionalTitle.FULL_PROFESSOR, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Data Structures", 3, 10, true); // Compulsory
        Course course2 = new Course("C002", "Algorithms", 3, 5, false); // Elective

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation of the Code:
1. **Enums**: `ProfessionalTitle` is an enumeration that defines the different professional titles a teacher can have.
2. **Teacher Class**: This class contains properties for teacher data and methods to manage courses and calculate salary.
   - `addCourse`: Adds a course to the teacher's list.
   - `calculateSalary`: Calculates the total salary based on the basic salary and course fees.
3. **Course Class**: This class contains properties for course information and a method to calculate the course fee based on the teacher's title and course type.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the salary.

This implementation adheres to Java coding standards and best practices, including proper encapsulation, use of enums, and clear method signatures.

--------------------------------------------------
# version 3.15
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information every teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours * 1; // 1 hour per class hour for elective courses
        }
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Professional Title
    private double basicSalary; // Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee; // Total salary calculation
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0; // $100 per class hour for full professors
            case associateProfessor:
                return 80.0; // $80 per class hour for associate professors
            case assistantProfessor:
                return 50.0; // $50 per class hour for assistant professors
            default:
                return 0.0; // Default case
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses taught. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 3.16
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information every teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.COMPULSORY) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee; // Total salary calculation
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0; // $100 per class hour for full professors
            case ASSOCIATE_PROFESSOR:
                return 80.0; // $80 per class hour for associate professors
            case ASSISTANT_PROFESSOR:
                return 50.0; // $50 per class hour for assistant professors
            default:
                return 0.0; // Default case
        }
    }

    // Method to add a course to the teacher's list of courses
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.FULL_PROFESSOR, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.ELECTIVE);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 3.17
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information every teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters for Teacher properties
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        switch (type) {
            case COMPULSORY:
                return hours * 2; // 2 hours per class hour for compulsory courses
            case ELECTIVE:
                return hours; // 1 hour per class hour for elective courses
            default:
                return 0.0;
        }
    }

    // Getters for Course properties
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Example usage
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.FULL_PROFESSOR, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.ASSOCIATE_PROFESSOR, 4000);

        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.ELECTIVE);

        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);

        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: An example usage of the `Teacher` and `Course` classes is provided in the `TeachingManagementSystem` class, demonstrating how to create instances and calculate salaries.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 3.18
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information every teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taught
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and comments for clarity.

--------------------------------------------------
# version 3.19
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information every teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: courses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.COMPULSORY) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Professional Title
    private double basicSalary; // Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>(); // Initialize the courses list
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee; // Total salary calculation
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0; // $100 per class hour for full professors
            case ASSOCIATE_PROFESSOR:
                return 80.0; // $80 per class hour for associate professors
            case ASSISTANT_PROFESSOR:
                return 50.0; // $50 per class hour for assistant professors
            default:
                return 0.0; // Default case
        }
    }

    // Method to add a course to the teacher's list of courses
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.FULL_PROFESSOR, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.ELECTIVE);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 3.20
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information every teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: teaches
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        return (type == CourseType.COMPULSORY) ? hours * 2 : hours;
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0;
        for (Course course : courses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's list of courses
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.FULL_PROFESSOR, 5000);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "Physics", 4, 5, CourseType.ELECTIVE);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 3.21
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information every teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        switch (type) {
            case compulsory:
                return hours * 2; // 2 hours per class hour for compulsory courses
            case elective:
                return hours; // 1 hour per class hour for elective courses
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details, a list of courses taught, and methods to calculate salary and course fees.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the creation of a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and comments for clarity.

--------------------------------------------------
# version 3.0
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information every teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Based on the provided functional requirements for the teaching management system, I will create a Java implementation that includes classes for managing teacher data and course information, as well as methods for calculating salaries according to the specified rules.

Here is the complete Java code:

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Title
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Class representing a Teacher
class Teacher {
    private String teacherNumber;
    private String name;
    private String gender;
    private ProfessionalTitle title;
    private double basicSalary;
    private List<Course> courses;

    public Teacher(String teacherNumber, String name, String gender, ProfessionalTitle title, double basicSalary) {
        this.teacherNumber = teacherNumber;
        this.name = name;
        this.gender = gender;
        this.title = title;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    public void addCourse(Course course) {
        courses.add(course);
    }

    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.calculateCourseFee(getCourseFeePerHour());
        }
        return basicSalary + totalCourseFee;
    }

    private double getCourseFeePerHour() {
        switch (title) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTeacherNumber() {
        return teacherNumber;
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }

    public ProfessionalTitle getTitle() {
        return title;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Class representing a Course
class Course {
    private String courseNumber;
    private String courseName;
    private int credit;
    private int classHours;
    private boolean isCompulsory;

    public Course(String courseNumber, String courseName, int credit, int classHours, boolean isCompulsory) {
        this.courseNumber = courseNumber;
        this.courseName = courseName;
        this.credit = credit;
        this.classHours = classHours;
        this.isCompulsory = isCompulsory;
    }

    public double calculateCourseFee(double courseFeePerHour) {
        int billedHours = isCompulsory ? classHours * 2 : classHours;
        return billedHours * courseFeePerHour;
    }

    // Getters and Setters
    public String getCourseNumber() {
        return courseNumber;
    }

    public String getCourseName() {
        return courseName;
    }

    public int getCredit() {
        return credit;
    }

    public int getClassHours() {
        return classHours;
    }

    public boolean isCompulsory() {
        return isCompulsory;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create teachers
        Teacher teacher1 = new Teacher("T001", "Alice", "Female", ProfessionalTitle.FULL_PROFESSOR, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", "Male", ProfessionalTitle.ASSOCIATE_PROFESSOR, 4000);
        
        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, true); // Compulsory
        Course course2 = new Course("C002", "History", 2, 5, false); // Elective
        
        // Assign courses to teachers
        teacher1.addCourse(course1);
        teacher1.addCourse(course2);
        teacher2.addCourse(course1);
        
        // Calculate and display salaries
        System.out.println("Salary of " + teacher1.getName() + ": $" + teacher1.calculateSalary());
        System.out.println("Salary of " + teacher2.getName() + ": $" + teacher2.calculateSalary());
    }
}
```

### Explanation of the Code:
1. **Enums**: `ProfessionalTitle` is an enumeration that defines the different professional titles a teacher can have.
2. **Teacher Class**: This class contains properties for teacher data, methods to add courses, and a method to calculate the salary based on the rules provided.
3. **Course Class**: This class contains properties for course data and a method to calculate the course fee based on whether the course is compulsory or elective.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating instances of `Teacher` and `Course`, assigning courses to teachers, and calculating their salaries.

This implementation adheres to Java coding standards and best practices, including encapsulation, use of collections, and clear method definitions.

--------------------------------------------------
# version 4.22
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information each teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details, a list of courses taught, and methods to calculate salary and course fees.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and comments for clarity.

--------------------------------------------------
# version 4.23
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information each teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForAlice = {course1, course2};
        double salaryAlice = teacher1.calculateSalary(coursesForAlice);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salaryAlice);
        
        Course[] coursesForBob = {course1};
        double salaryBob = teacher2.calculateSalary(coursesForBob);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salaryBob);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate the salary based on the courses taught and to get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate the billed hours based on the course type.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and proper use of enums.

--------------------------------------------------
# version 4.24
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information each teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate the salary based on the courses taught and to get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate the billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation and clear method definitions.

--------------------------------------------------
# version 4.25
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information each teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taught
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary(Course[] courses) {
        double totalSalary = basicSalary;
        for (Course course : courses) {
            totalSalary += course.getBilledHours() * getCourseFeePerHour();
        }
        return totalSalary;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        return (type == CourseType.COMPULSORY) ? hours * 2 : hours;
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.FULL_PROFESSOR, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.ASSOCIATE_PROFESSOR, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.ELECTIVE);
        
        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation and clear method definitions.

--------------------------------------------------
# version 4.26
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information each teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: courses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // List of courses taught by the teacher
    private List<Course> courses = new ArrayList<>();

    // Method to add a course to the teacher's list
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details, methods to calculate salary, and manage courses.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on course type.
4. **Main Class**: Demonstrates the creation of a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, proper naming conventions, and comments for clarity.

--------------------------------------------------
# version 4.27
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information each teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: teaches
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;

        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }

        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.COMPULSORY) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Example usage
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.FULL_PROFESSOR, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.ASSOCIATE_PROFESSOR, 4000);

        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.ELECTIVE);

        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);

        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate the salary based on the courses taught and to get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate the billed hours based on the course type.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates how to create instances of `Teacher` and `Course`, and how to calculate and display the salaries of the teachers based on the courses they teach.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 4.28
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information each teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000.0);
        
        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);
        
        // Add courses to the teacher
        teacher1.addCourse(course1);
        teacher1.addCourse(course2);
        
        // Calculate and display the teacher's salary
        double salary = teacher1.calculateSalary();
        System.out.println("Teacher: " + teacher1.getName() + ", Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details and methods to calculate salary and course fees. It also has a list to manage the courses taught by the teacher.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and proper use of collections.

--------------------------------------------------
# version 4.0
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information each teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Based on the provided functional requirements for the teaching management system, I will create a Java implementation that includes classes for managing teacher data and course information, as well as methods for calculating salaries according to the specified rules.

Here is the complete Java code:

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Title
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Class representing a Teacher
class Teacher {
    private String teacherNumber;
    private String name;
    private String gender;
    private ProfessionalTitle title;
    private double basicSalary;
    private List<Course> courses;

    public Teacher(String teacherNumber, String name, String gender, ProfessionalTitle title, double basicSalary) {
        this.teacherNumber = teacherNumber;
        this.name = name;
        this.gender = gender;
        this.title = title;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    // Method to add a course to the teacher
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.calculateCourseFee(getCourseFeePerHour());
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on the teacher's title
    private double getCourseFeePerHour() {
        switch (title) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters for teacher properties
    public String getTeacherNumber() {
        return teacherNumber;
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }

    public ProfessionalTitle getTitle() {
        return title;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Class representing a Course
class Course {
    private String courseNumber;
    private String courseName;
    private int credit;
    private int classHours;
    private boolean isCompulsory;

    public Course(String courseNumber, String courseName, int credit, int classHours, boolean isCompulsory) {
        this.courseNumber = courseNumber;
        this.courseName = courseName;
        this.credit = credit;
        this.classHours = classHours;
        this.isCompulsory = isCompulsory;
    }

    // Method to calculate the course fee based on the course type
    public double calculateCourseFee(double feePerHour) {
        int billedHours = isCompulsory ? classHours * 2 : classHours;
        return feePerHour * billedHours;
    }

    // Getters for course properties
    public String getCourseNumber() {
        return courseNumber;
    }

    public String getCourseName() {
        return courseName;
    }

    public int getCredit() {
        return credit;
    }

    public int getClassHours() {
        return classHours;
    }

    public boolean isCompulsory() {
        return isCompulsory;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", "Male", ProfessionalTitle.FULL_PROFESSOR, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, true); // Compulsory
        Course course2 = new Course("C002", "History", 2, 5, false); // Elective

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher: " + teacher.getName());
        System.out.println("Total Salary: $" + salary);
    }
}
```

### Explanation of the Code:
1. **Enums**: `ProfessionalTitle` is an enumeration that defines the different professional titles a teacher can have.

2. **Teacher Class**: 
   - Contains properties for teacher number, name, gender, title, basic salary, and a list of courses.
   - Includes methods to add courses and calculate the salary based on the rules provided.

3. **Course Class**: 
   - Contains properties for course number, name, credit, class hours, and whether the course is compulsory.
   - Includes a method to calculate the course fee based on the course type.

4. **Main Class**: 
   - Demonstrates the functionality by creating a teacher and adding courses, then calculating and displaying the teacher's salary.

This implementation adheres to Java coding standards and best practices, ensuring clarity and maintainability.

--------------------------------------------------
# version 5.29
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage what courses a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        switch (type) {
            case compulsory:
                return hours * 2; // 2 hours per class hour for compulsory courses
            case elective:
                return hours; // 1 hour per class hour for elective courses
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses taught. It includes methods to calculate salary and get the course fee per hour.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful method names, and comments for clarity.

--------------------------------------------------
# version 5.30
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage what courses a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", false, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", true, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForAlice = {course1, course2};
        double salaryAlice = teacher1.calculateSalary(coursesForAlice);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salaryAlice);
        
        Course[] coursesForBob = {course1};
        double salaryBob = teacher2.calculateSalary(coursesForBob);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salaryBob);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate the salary based on courses taught and to get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation and clear method definitions.

--------------------------------------------------
# version 5.31
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage what courses a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", false, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", true, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and proper use of enums.

--------------------------------------------------
# version 5.32
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage what courses a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taught
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", false, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", true, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForAlice = {course1, course2};
        double salaryAlice = teacher1.calculateSalary(coursesForAlice);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salaryAlice);
        
        Course[] coursesForBob = {course1};
        double salaryBob = teacher2.calculateSalary(coursesForBob);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salaryBob);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate the salary based on the courses taught and to get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate the billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and proper use of enums.

--------------------------------------------------
# version 5.33
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage what courses a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: courses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // List of courses taught by the teacher
    private List<Course> courses = new ArrayList<>();

    // Method to add a course to the teacher's list
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type (Compulsory or Elective)

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details, methods to calculate salary, and manage courses.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on course type.
4. **Main Class**: Demonstrates the creation of a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, method naming conventions, and proper use of collections.

--------------------------------------------------
# version 5.34
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage what courses a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: teaches
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the salary of the teacher
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForAlice = {course1, course2};
        double salaryAlice = teacher1.calculateSalary(coursesForAlice);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salaryAlice);
        
        Course[] coursesForBob = {course1};
        double salaryBob = teacher2.calculateSalary(coursesForBob);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salaryBob);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate the salary based on the courses taught and to get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate the billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation and clear method definitions.

--------------------------------------------------
# version 5.35
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage what courses a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type (compulsory or elective)

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details and methods to calculate salary and course fees. It also has a method to add courses.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation and clear method definitions.

--------------------------------------------------
# version 5.0
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage what courses a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Based on the provided functional requirements for the teaching management system, I will create a Java implementation that includes classes for managing teacher data and courses, as well as calculating salaries based on the specified rules. Below is the complete Java code:

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Title
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Class representing a Teacher
class Teacher {
    private String teacherNumber;
    private String name;
    private String gender;
    private ProfessionalTitle title;
    private double basicSalary;
    private List<Course> courses;

    public Teacher(String teacherNumber, String name, String gender, ProfessionalTitle title, double basicSalary) {
        this.teacherNumber = teacherNumber;
        this.name = name;
        this.gender = gender;
        this.title = title;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    public void addCourse(Course course) {
        courses.add(course);
    }

    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.calculateCourseFee(getCourseFeePerHour());
        }
        return basicSalary + totalCourseFee;
    }

    private double getCourseFeePerHour() {
        switch (title) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTeacherNumber() {
        return teacherNumber;
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }

    public ProfessionalTitle getTitle() {
        return title;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Class representing a Course
class Course {
    private String courseNumber;
    private String courseName;
    private int credit;
    private int classHours;
    private boolean isCompulsory;

    public Course(String courseNumber, String courseName, int credit, int classHours, boolean isCompulsory) {
        this.courseNumber = courseNumber;
        this.courseName = courseName;
        this.credit = credit;
        this.classHours = classHours;
        this.isCompulsory = isCompulsory;
    }

    public double calculateCourseFee(double courseFeePerHour) {
        int billedHours = isCompulsory ? classHours * 2 : classHours;
        return courseFeePerHour * billedHours;
    }

    // Getters and Setters
    public String getCourseNumber() {
        return courseNumber;
    }

    public String getCourseName() {
        return courseName;
    }

    public int getCredit() {
        return credit;
    }

    public int getClassHours() {
        return classHours;
    }

    public boolean isCompulsory() {
        return isCompulsory;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", "Male", ProfessionalTitle.FULL_PROFESSOR, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Data Structures", 3, 10, true); // Compulsory
        Course course2 = new Course("C002", "Algorithms", 3, 5, false); // Elective

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher: " + teacher.getName());
        System.out.println("Total Salary: $" + salary);
    }
}
```

### Explanation of the Code:
1. **Enums**: `ProfessionalTitle` is an enumeration that defines the different professional titles a teacher can have.

2. **Teacher Class**: 
   - Contains properties for teacher number, name, gender, title, basic salary, and a list of courses.
   - The `addCourse` method allows adding courses to the teacher.
   - The `calculateSalary` method computes the total salary based on the basic salary and the fees from the courses taught.

3. **Course Class**: 
   - Contains properties for course number, name, credit, class hours, and whether the course is compulsory.
   - The `calculateCourseFee` method calculates the fee based on the course type and the number of class hours.

4. **Main Class**: 
   - Demonstrates the functionality by creating a teacher and adding courses to them, then calculating and displaying the total salary.

This implementation adheres to Java coding standards and best practices, including encapsulation, use of enums, and clear method definitions.

--------------------------------------------------
# version 6.36
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Record courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram:

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details, methods to calculate salary, get course fee per hour, and add courses.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on course type.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful method names, and comments for clarity.

--------------------------------------------------
# version 6.37
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Record courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0; // Default case, should not occur
        }
    }

    // Getters for Teacher properties
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type (compulsory or elective)

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters for Course properties
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Example usage
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForAlice = {course1, course2};
        double salaryAlice = teacher1.calculateSalary(coursesForAlice);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salaryAlice);
        
        Course[] coursesForBob = {course1};
        double salaryBob = teacher2.calculateSalary(coursesForBob);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salaryBob);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: An example usage of the `Teacher` and `Course` classes is provided in the `TeachingManagementSystem` class, demonstrating how to create instances and calculate salaries.

This code adheres to Java coding standards and best practices, including encapsulation and clear method definitions.

--------------------------------------------------
# version 6.38
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Record courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.fullProfessor, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.associateProfessor, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.elective);
        
        // Calculate salaries
        Course[] coursesForAlice = {course1, course2};
        double salaryAlice = teacher1.calculateSalary(coursesForAlice);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salaryAlice);
        
        Course[] coursesForBob = {course1};
        double salaryBob = teacher2.calculateSalary(coursesForBob);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salaryBob);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, calculating their salaries, and printing the results.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful naming conventions, and proper use of enums.

--------------------------------------------------
# version 6.39
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Record courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taught
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0; // Should not reach here
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        return (type == CourseType.COMPULSORY) ? hours * 2 : hours;
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.FULL_PROFESSOR, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.ASSOCIATE_PROFESSOR, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.ELECTIVE);
        
        // Calculate salaries
        Course[] coursesForAlice = {course1, course2};
        double salaryAlice = teacher1.calculateSalary(coursesForAlice);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salaryAlice);
        
        Course[] coursesForBob = {course1};
        double salaryBob = teacher2.calculateSalary(coursesForBob);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salaryBob);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: Demonstrates the functionality by creating instances of `Teacher` and `Course`, and calculating their salaries based on the courses they teach.

This code adheres to Java coding standards and best practices, including encapsulation and clear method definitions.

--------------------------------------------------
# version 6.40
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Record courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: courses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's list of courses
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type (compulsory or elective)

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher details, a list of courses, and methods to calculate salary and course fees.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on course type.
4. **Main Class**: Demonstrates the creation of a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful method names, and comments for clarity.

--------------------------------------------------
# version 6.41
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Record courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: teaches
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Method to calculate the teacher's salary
    public double calculateSalary(Course[] courses) {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0; // Default case (should not occur)
        }
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.COMPULSORY) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Example usage
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create some teachers
        Teacher teacher1 = new Teacher("T001", "Alice", true, ProfessionalTitle.FULL_PROFESSOR, 5000);
        Teacher teacher2 = new Teacher("T002", "Bob", false, ProfessionalTitle.ASSOCIATE_PROFESSOR, 4000);
        
        // Create some courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "History", 2, 5, CourseType.ELECTIVE);
        
        // Calculate salaries
        Course[] coursesForTeacher1 = {course1, course2};
        double salary1 = teacher1.calculateSalary(coursesForTeacher1);
        System.out.println("Salary of " + teacher1.getName() + ": $" + salary1);
        
        Course[] coursesForTeacher2 = {course1};
        double salary2 = teacher2.calculateSalary(coursesForTeacher2);
        System.out.println("Salary of " + teacher2.getName() + ": $" + salary2);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined to represent the professional titles of teachers and types of courses, respectively.
2. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, and basic salary. It includes methods to calculate salary and get the course fee per hour based on the professional title.
3. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
4. **Main Class**: An example usage of the `Teacher` and `Course` classes is provided in the `TeachingManagementSystem` class, demonstrating how to create instances and calculate salaries.

This code adheres to Java coding standards and best practices, including encapsulation and method naming conventions.

--------------------------------------------------
# version 6.42
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Record courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary methods and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender (true for male, false for female)
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += course.getBilledHours() * getCourseFeePerHour();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0;
            case associateProfessor:
                return 80.0;
            case assistantProfessor:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters and Setters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type (compulsory or elective)

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters and Setters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Example usage
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and print the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses.
2. **Teacher Class**: Contains properties for teacher details, a list of courses taught, and methods to calculate salary and course fees.
3. **Course Class**: Contains properties for course details and a method to calculate billed hours based on course type.
4. **Main Class**: An example usage of the `Teacher` and `Course` classes is provided in the `TeachingManagementSystem` class, demonstrating how to create a teacher, add courses, and calculate the salary.

This code adheres to Java coding standards and best practices, including encapsulation, meaningful method names, and comments for clarity.

--------------------------------------------------
# version 6.0
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Record courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Based on the provided functional requirements for the teaching management system, I will create a Java implementation that includes classes for managing teacher data, course information, and salary calculations. Below is the complete Java code:

```java
// Teacher.java
public class Teacher {
    private String teacherNumber;
    private String name;
    private String gender;
    private String professionalTitle; // "Full Professor", "Associate Professor", "Assistant Professor"
    private double basicSalary;

    public Teacher(String teacherNumber, String name, String gender, String professionalTitle, double basicSalary) {
        this.teacherNumber = teacherNumber;
        this.name = name;
        this.gender = gender;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
    }

    // Getters and Setters
    public String getTeacherNumber() {
        return teacherNumber;
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }

    public String getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    // Method to calculate course fee per hour based on professional title
    public double getCourseFee() {
        switch (professionalTitle) {
            case "Full Professor":
                return 100.0;
            case "Associate Professor":
                return 80.0;
            case "Assistant Professor":
                return 50.0;
            default:
                throw new IllegalArgumentException("Invalid professional title");
        }
    }
}

// Course.java
public class Course {
    private String courseNumber;
    private String courseName;
    private int credit;
    private int classHours;
    private String courseType; // "Elective" or "Compulsory"

    public Course(String courseNumber, String courseName, int credit, int classHours, String courseType) {
        this.courseNumber = courseNumber;
        this.courseName = courseName;
        this.credit = credit;
        this.classHours = classHours;
        this.courseType = courseType;
    }

    // Getters and Setters
    public String getCourseNumber() {
        return courseNumber;
    }

    public String getCourseName() {
        return courseName;
    }

    public int getCredit() {
        return credit;
    }

    public int getClassHours() {
        return classHours;
    }

    public String getCourseType() {
        return courseType;
    }

    // Method to calculate billed hours based on course type
    public int getBilledHours() {
        return courseType.equals("Compulsory") ? classHours * 2 : classHours;
    }
}

// SalaryCalculator.java
public class SalaryCalculator {
    public static double calculateSalary(Teacher teacher, Course course) {
        double courseFee = teacher.getCourseFee();
        int billedHours = course.getBilledHours();
        return teacher.getBasicSalary() + (courseFee * billedHours);
    }
}

// Main.java
public class Main {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", "Male", "Full Professor", 5000.0);
        
        // Create a course
        Course course = new Course("C001", "Data Structures", 3, 10, "Compulsory");
        
        // Calculate salary
        double salary = SalaryCalculator.calculateSalary(teacher, course);
        
        // Output the result
        System.out.printf("Teacher: %s, Salary: $%.2f%n", teacher.getName(), salary);
    }
}
```

### Explanation of the Code:
1. **Teacher Class**: This class holds the teacher's information and includes methods to get the course fee based on the professional title.
2. **Course Class**: This class holds the course information and includes a method to calculate the billed hours based on the course type.
3. **SalaryCalculator Class**: This class contains a static method to calculate the teacher's salary based on their basic salary and the fees from the courses they teach.
4. **Main Class**: This is the entry point of the program where we create instances of `Teacher` and `Course`, calculate the salary, and print the result.

### Comments:
- The code is structured to follow Java best practices, including encapsulation and clear method naming.
- Error handling is included for invalid professional titles.
- The program is designed to be easily extendable for future requirements.

--------------------------------------------------
# version 7.43
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information. Note that a teacher can teach multiple courses.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours * 1; // 1 hour per class hour for elective courses
        }
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Professional Title
    private double basicSalary; // Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee; // Total salary calculation
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0; // $100 per class hour for full professors
            case associateProfessor:
                return 80.0; // $80 per class hour for associate professors
            case assistantProfessor:
                return 50.0; // $50 per class hour for assistant professors
            default:
                return 0.0; // Default case
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Example usage
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and print the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses taught. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Business Logic**: The salary calculation considers the basic salary and the total course fees based on the courses taught.
5. **Example Usage**: The `TeachingManagementSystem` class demonstrates how to create a teacher, add courses, and calculate the salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 7.44
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information. Note that a teacher can teach multiple courses.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>(); // Initialize the list of courses
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee; // Total salary calculation
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0; // $100 per class hour for full professors
            case associateProfessor:
                return 80.0; // $80 per class hour for associate professors
            case assistantProfessor:
                return 50.0; // $50 per class hour for assistant professors
            default:
                return 0.0; // Default case
        }
    }

    // Method to add a course to the teacher's list of courses
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 7.45
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information. Note that a teacher can teach multiple courses.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Enum for Course Types
enum CourseType {
    COMPULSORY,
    ELECTIVE
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        return (type == CourseType.COMPULSORY) ? hours * 2 : hours;
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Professional Title
    private double basicSalary; // Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0;
        for (Course course : courses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee;
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0;
        }
    }

    // Method to add a course to the teacher's list
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.FULL_PROFESSOR, 5000);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, CourseType.COMPULSORY);
        Course course2 = new Course("C002", "Physics", 4, 5, CourseType.ELECTIVE);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including encapsulation, proper naming conventions, and comments for clarity.

--------------------------------------------------
# version 7.46
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information. Note that a teacher can teach multiple courses.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: taught
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Professional Title
    private double basicSalary; // Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>(); // Initialize the list of courses
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee; // Total salary calculation
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0; // $100 per class hour for full professors
            case associateProfessor:
                return 80.0; // $80 per class hour for associate professors
            case assistantProfessor:
                return 50.0; // $50 per class hour for assistant professors
            default:
                return 0.0; // Default case
        }
    }

    // Method to add a course to the teacher's list of courses
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 7.47
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information. Note that a teacher can teach multiple courses.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: courses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Professional Title
    private double basicSalary; // Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>(); // Initialize the courses list
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee; // Total salary calculation
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0; // $100 per class hour for full professors
            case associateProfessor:
                return 80.0; // $80 per class hour for associate professors
            case assistantProfessor:
                return 50.0; // $50 per class hour for assistant professors
            default:
                return 0.0; // Default case
        }
    }

    // Method to add a course to the teacher's list of courses
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Example usage
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);
        
        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);
        
        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);
        
        // Calculate and print the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Business Logic**: The `calculateSalary` method computes the total salary based on the basic salary and the fees from the courses taught.
5. **Example Usage**: The `TeachingManagementSystem` class demonstrates how to create a teacher, add courses, and calculate the salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 7.48
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information. Note that a teacher can teach multiple courses.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" *-- "0..*" Course: teaches
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram:

```java
// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours * 1; // 1 hour per class hour for elective courses
        }
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Teacher's Professional Title
    private double basicSalary; // Teacher's Basic Salary
    private List<Course> courses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>(); // Initialize the list of courses
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : courses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee; // Total salary calculation
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0; // $100 per class hour for full professors
            case associateProfessor:
                return 80.0; // $80 per class hour for associate professors
            case assistantProfessor:
                return 50.0; // $50 per class hour for assistant professors
            default:
                return 0.0; // Default case
        }
    }

    // Method to add a course to the teacher's list of courses
    public void addCourse(Course course) {
        courses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Main Class**: Demonstrates the functionality by creating a teacher and courses, adding courses to the teacher, and calculating the teacher's salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 7.49
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information. Note that a teacher can teach multiple courses.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:

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

        Teacher "1" --> "0..*" Course: taughtCourses
    @enduml
```
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Here is the complete Java code based on the provided system functional requirements and UML class diagram. The code includes the `Teacher` and `Course` classes, along with the necessary properties, methods, and business logic implementations.

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Titles
enum ProfessionalTitle {
    fullProfessor,
    associateProfessor,
    assistantProfessor
}

// Enum for Course Types
enum CourseType {
    compulsory,
    elective
}

// Class representing a Course
class Course {
    private String cid; // Course ID
    private String name; // Course Name
    private double credit; // Course Credit
    private double hours; // Class Hours
    private CourseType type; // Course Type

    // Constructor
    public Course(String cid, String name, double credit, double hours, CourseType type) {
        this.cid = cid;
        this.name = name;
        this.credit = credit;
        this.hours = hours;
        this.type = type;
    }

    // Method to get billed hours based on course type
    public double getBilledHours() {
        if (type == CourseType.compulsory) {
            return hours * 2; // 2 hours per class hour for compulsory courses
        } else {
            return hours; // 1 hour per class hour for elective courses
        }
    }

    // Getters
    public String getCid() {
        return cid;
    }

    public String getName() {
        return name;
    }

    public double getCredit() {
        return credit;
    }

    public double getHours() {
        return hours;
    }

    public CourseType getType() {
        return type;
    }
}

// Class representing a Teacher
class Teacher {
    private String tid; // Teacher ID
    private String name; // Teacher Name
    private boolean sex; // Teacher Gender
    private ProfessionalTitle professionalTitle; // Professional Title
    private double basicSalary; // Basic Salary
    private List<Course> taughtCourses; // List of courses taught by the teacher

    // Constructor
    public Teacher(String tid, String name, boolean sex, ProfessionalTitle professionalTitle, double basicSalary) {
        this.tid = tid;
        this.name = name;
        this.sex = sex;
        this.professionalTitle = professionalTitle;
        this.basicSalary = basicSalary;
        this.taughtCourses = new ArrayList<>();
    }

    // Method to calculate the teacher's salary
    public double calculateSalary() {
        double totalCourseFee = 0.0;
        for (Course course : taughtCourses) {
            totalCourseFee += getCourseFeePerHour() * course.getBilledHours();
        }
        return basicSalary + totalCourseFee; // Total salary calculation
    }

    // Method to get the course fee per hour based on professional title
    public double getCourseFeePerHour() {
        switch (professionalTitle) {
            case fullProfessor:
                return 100.0; // $100 per class hour for full professors
            case associateProfessor:
                return 80.0; // $80 per class hour for associate professors
            case assistantProfessor:
                return 50.0; // $50 per class hour for assistant professors
            default:
                return 0.0; // Default case
        }
    }

    // Method to add a course to the teacher's taught courses
    public void addCourse(Course course) {
        taughtCourses.add(course);
    }

    // Getters
    public String getTid() {
        return tid;
    }

    public String getName() {
        return name;
    }

    public boolean isSex() {
        return sex;
    }

    public ProfessionalTitle getProfessionalTitle() {
        return professionalTitle;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getTaughtCourses() {
        return taughtCourses;
    }
}

// Example usage
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", true, ProfessionalTitle.fullProfessor, 5000.0);

        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3.0, 10, CourseType.compulsory);
        Course course2 = new Course("C002", "Physics", 4.0, 5, CourseType.elective);

        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);

        // Calculate and print the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher's Salary: $" + salary);
    }
}
```

### Explanation:
1. **Enums**: `ProfessionalTitle` and `CourseType` are defined as enums to represent the professional titles of teachers and types of courses, respectively.
2. **Course Class**: Contains properties for course ID, name, credit, hours, and type. It includes a method to calculate billed hours based on the course type.
3. **Teacher Class**: Contains properties for teacher ID, name, gender, professional title, basic salary, and a list of courses taught. It includes methods to calculate salary and get the course fee per hour based on the professional title.
4. **Main Class**: An example usage of the `Teacher` and `Course` classes is provided in the `TeachingManagementSystem` class, demonstrating how to create a teacher, add courses, and calculate the salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, method naming conventions, and comments for clarity.

--------------------------------------------------
# version 7.0
## Description:

The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information. Note that a teacher can teach multiple courses.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.

## UML:
## Model:
gpt-3.5-turbo-0125
## Temperature:
0
## Result:
Based on the provided functional requirements for the teaching management system, I will create a Java implementation that includes classes for managing teacher data and course information, as well as methods for calculating salaries according to the specified rules.

Here is the complete Java code:

```java
import java.util.ArrayList;
import java.util.List;

// Enum for Professional Title
enum ProfessionalTitle {
    FULL_PROFESSOR,
    ASSOCIATE_PROFESSOR,
    ASSISTANT_PROFESSOR
}

// Class representing a Course
class Course {
    private String courseNumber;
    private String courseName;
    private int credit;
    private int classHours;
    private boolean isCompulsory; // true for compulsory, false for elective

    public Course(String courseNumber, String courseName, int credit, int classHours, boolean isCompulsory) {
        this.courseNumber = courseNumber;
        this.courseName = courseName;
        this.credit = credit;
        this.classHours = classHours;
        this.isCompulsory = isCompulsory;
    }

    public int getClassHours() {
        return classHours;
    }

    public boolean isCompulsory() {
        return isCompulsory;
    }
}

// Class representing a Teacher
class Teacher {
    private String teacherNumber;
    private String name;
    private String gender;
    private ProfessionalTitle title;
    private double basicSalary;
    private List<Course> courses;

    public Teacher(String teacherNumber, String name, String gender, ProfessionalTitle title, double basicSalary) {
        this.teacherNumber = teacherNumber;
        this.name = name;
        this.gender = gender;
        this.title = title;
        this.basicSalary = basicSalary;
        this.courses = new ArrayList<>();
    }

    public void addCourse(Course course) {
        courses.add(course);
    }

    public double calculateSalary() {
        double courseFee = getCourseFee();
        int totalBilledHours = calculateTotalBilledHours();
        return basicSalary + (courseFee * totalBilledHours);
    }

    private double getCourseFee() {
        switch (title) {
            case FULL_PROFESSOR:
                return 100.0;
            case ASSOCIATE_PROFESSOR:
                return 80.0;
            case ASSISTANT_PROFESSOR:
                return 50.0;
            default:
                return 0.0;
        }
    }

    private int calculateTotalBilledHours() {
        int totalHours = 0;
        for (Course course : courses) {
            if (course.isCompulsory()) {
                totalHours += course.getClassHours() * 2; // 2 hours per class hour for compulsory courses
            } else {
                totalHours += course.getClassHours(); // 1 hour per class hour for elective courses
            }
        }
        return totalHours;
    }

    // Getters for teacher information
    public String getTeacherNumber() {
        return teacherNumber;
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }

    public ProfessionalTitle getTitle() {
        return title;
    }

    public double getBasicSalary() {
        return basicSalary;
    }

    public List<Course> getCourses() {
        return courses;
    }
}

// Main class to demonstrate the functionality
public class TeachingManagementSystem {
    public static void main(String[] args) {
        // Create a teacher
        Teacher teacher = new Teacher("T001", "John Doe", "Male", ProfessionalTitle.FULL_PROFESSOR, 5000.0);
        
        // Create courses
        Course course1 = new Course("C001", "Mathematics", 3, 10, true); // Compulsory
        Course course2 = new Course("C002", "History", 2, 5, false); // Elective
        
        // Add courses to the teacher
        teacher.addCourse(course1);
        teacher.addCourse(course2);
        
        // Calculate and display the teacher's salary
        double salary = teacher.calculateSalary();
        System.out.println("Teacher: " + teacher.getName());
        System.out.println("Salary: $" + salary);
    }
}
```

### Explanation of the Code:
1. **Enums**: `ProfessionalTitle` is an enumeration that defines the different professional titles a teacher can have.
2. **Course Class**: Represents a course with properties such as course number, name, credit, class hours, and whether it is compulsory or elective.
3. **Teacher Class**: Represents a teacher with properties such as teacher number, name, gender, title, basic salary, and a list of courses they teach. It includes methods to add courses and calculate the salary based on the rules provided.
4. **Salary Calculation**: The `calculateSalary` method computes the total salary based on the basic salary and the fees for the courses taught, considering the type of courses.
5. **Main Class**: The `TeachingManagementSystem` class demonstrates the functionality by creating a teacher, adding courses, and calculating the salary.

This code adheres to Java coding standards and best practices, including proper encapsulation, use of collections, and clear method definitions.

--------------------------------------------------
