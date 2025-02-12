HRIS_description = """Human-Resources Information System(HRIS)

The Human-Resources Information System (HRIS) web-based, it is divided into four parts; they are User Login Management, Employee Information Management, Employee Leaves Management, and Employee Discipline Management.

In the User Login Management, it is divided into ordinary user login, and administrator user login. The ordinary user is the registered user, such as employees and so on. The administrators are responsible for maintaining and updating the entire system and have more rights on the system. This system includes employee information entry, employee information changes, employee information inquiry, and employee information deleted. The Employee Leaves Management includes: leave information input, leave information query and statistics leave information. Employee Discipline Management includes: input information punishment, query information punishment.
1. User login Management is divided into ordinary user login and administrator login. When ordinary users log on, the system will give him low authority to meet the basic needs of ordinary users. When the user is an administrator, the system will assign a higher authority in order to achieve the system's updates and maintenance by the administrator.
2. The Employee Information Management is mainly the basic information management for employees. Employees can view the personal information page their own such as (name, address, sex, minority status, etc.,) when they enter system and do not have any right to edit and manage of the information as defined by HR Policies of the organization. They can edit personal information only as defined by HR administrators of the organization and also uploads their personal photographs into the system. 
3. The Employee leaves Management is the assessment of the daily work of employees. The employee worth an annual leave when he has at least one year of continuous service to be eligible for this type of leave. The employee can request another leave (maternity, satisfactory, without pay, etc.,) as well as a local leave period of seven days for a while if an employee did not complete the year on his appointment and will be in cases necessary only. The employee can send request leave to the administrator after getting employee's to initial approval from the senior management for submission of the application. The administrator can approve or reject the approval.
4. The Employee Discipline Management is the It encourages harmony and cooperation among employees as well as acts as a morale booster for the employees. In the absence of discipline, there will be chaos, confusion, corruption and disobedience in an organization. If the employee has committed any breach, the senior management will determine the type of offense and the punishment necessary. After the notify system administrator, such as (dismissal, written reprimand, etc.) when the employee gets on three written reprimand the administrator will notify senior management to take appropriate procedures against the employee such as separating the employee or transmission in the same or the outside institution.
"""

HRIS_UML = """
Classes:
User()
Administrator()
Employee(string name,string adress,boolean sex,string minorityStatus,string photo,EmployeeRole role,int leaveBalance)
LeaveRequest(LeaveType leavetype,ApprovalStatus approvalStatus,date startDate,date endDate)
DisciplineRecord(string offenseType,PunishmentType punishmentType)

Relationships:
1 LeaveRequest associate 1 Employee
1 DisciplineRecord associate 1 Employee

Administrator inherit User
Employee inherit User

"""

Member_description = """
常见的用户权限管理的表结构设计，基本的关系如下：一个用户可以拥有多个角色，一个角色可能有多个用户；一个角色可以拥有多个权限。要求实现如下查询功能：1）以根据一个用户找到该用户对应的所有角色，以及每一个角色对应的所有权限信息；2）可以根据一个角色找到该角色下的所有权限，以及拥有此角色的全部用户信息；3）可以根据一个权限找到具备有此权限的所有用户信息。

"""
Member_UML = """
- 类：
Member(string mid,string name,Member(), setRoles(),getRoles(),getInfo())，
Role(long rid, string title, Role(), setMembers(), getmembers(), setPrivileges(), getPrivileges(),getInfo())
Privilege(long pid, string title,Privilege(),   setRole(), getRole(), getInfo()
- 关系：
1 Member associate * Role
1 Role associate * Member
1 Role associate * Privilege
1 Privilege associate * Role
"""

# 题库管理系统
# 线上考试管理系统
# 银行管理系统(存款取款，转账支付，储蓄账户/信用卡账户，利息计算)
# 物流管理系统

# sports game management system, # 体育比赛管理系统
# 电竞比赛管理系统 
# 直播售卖物品统计系统
educational_description = """ 
A simple educational management system that can implement the following functions:
1) Manage student information, including student ID, name.
2) Manage course information, including course ID, course name, course credits, and course description.
3) Manage students' course enroll time and grades. The student can take the same course multiple times.
4) Query all the unique courses taken by a student.
5) Calculate a course grade, which is the highest score the student have earned.
6) Calculate the credits earned by a student. The credit of a unique course is only counted toward the result if the course grade is 60 or above.
"""
# 5) Calculate the grade point for each course taken by a student. The grade point is determined as follows:
#     - Below 60: Grade point = 0
#     - 60-70 (inclusive): Grade point = 2
#     - 70-80 (inclusive): Grade point = 3
#     - Above 80: Grade point = 4
# 6) Calculate the student's average grade point. The average grade point is calculated as:
# Average Grade Point= (Grade Point of Course 1 * Credit of Course 1 + Grade Point of Course 2 * Credit of Course 2 + ...) / (Credit of Course 1 + Credit of Course 2 + ...)  

"""
简易的教务系统，能够实现以下功能：
1）管理学生基本信息，学生信息包含学生编号、姓名等信息。
2）管理学生的课程信息，包括课程编号、课程名称、课程学分、课程简介等信息。
3）管理学生所选的每门课程的选课时间和成绩。同一门课程可以重复选修多次。记录最高成绩为该课程的成绩。
4）查询学生所修的所有课程。
5）查询学生所修的某一门课程的成绩。
4）计算学生已获得的总学分。每门课成绩大于等于60分，学分才能算入总学分。 
5）计算学生选修的每门课程的绩点。成绩在60分以下、60分-70分（含70分）、70分-80分（含80分）、80分以上，那对应的绩点就是0、2、3、4的标准。
6）计算学生所获得的平均绩点。平均绩点=（课程1绩点*课程1学分+课程2绩点*课程2学分+...）/（课程1学分+课程2学分+...）。
"""
educational_uml = """
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
"""


System_description = """
考试管理系统，能够实现以下功能：
1）管理员创建和安排考试
2）学生参加考试，提交答卷
3）老师批阅考试，给出成绩
"""

University_description = """
The teaching management system for college teachers can realize the following functions:
1) Manage teacher data, which contains information such as teacher number, name, gender, professional title (full professor/associate professor/assistant professor), basic salary.
2) Manage courses information a teacher teaches, including course number, course name, credit, class hours, course type (elective/compulsory) and other information.
3) Calculate the teacher's salary. The salary calculation rule is as follows: salary = basic salary + course fee * billed hours.
4) The class fee varies according to the teacher's professional title. It is $100 per class hour for full professors, $80 per class hour for associate professors and $50 per class hour for assistant professors.
5) The charging hours are different according to the course type, 2 hours per class hour for compulsory courses and 1 hour per class hour for elective courses.
"""

"""
高校教师课程教学管理系统，能够实现以下功能：
1）管理教师数据，教师数据包含教师编号、姓名、性别、职称（教授/副教授/讲师）、基本工资等信息。
2）管理教师的课程信息，包括课程编号、课程名称、学分、学时、课程类型（选修/必修）等信息。
3）计算教师的工资，工资计算规则为：工资=基本工资+课时费*计费学时。注意：一个老师可以教多门课程。
4）课时费用根据教师的职称不同而不同，教授每学时100元，副教授每学时80元，讲师每学时50元。
5）计费学时根据课程类型不同而不同，必修课每课时2学时，选修课每课时1学时。

"""

Uni_UML = """
```plantuml
    @startuml
        note:  class diagram

        enum ProfessionalTitle{
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
"""
# 这个系统主要是测试 聚合和继承。
Bank_description = """
这是一个银行系统，具体要求如下 :
1) 管理储蓄账户：用户（包括姓名，账号，密码，联系电话）可以管理储蓄账户，包括存款和取款，查询余额。包括账户id, 余额balance, 年利率rate，日期等。注意：一个用户可以有多个储蓄账户。
2）计算储蓄账户的年利息：对于每个账户：年利 = 日均余额 * 年利率，日均余额 = 一年当中每天的余额累计起来/一年的总天数。

3）管理信用卡账户，包括余额（balance）：
- 当前账户内有多少钱（可正可负）
- 信用额度（credit）: 欠款 <= 信用额度
- 利率(rate)：存钱(正余额) 不会有利息。欠款（负余额）需要支付利息，且按日欠款计息，不考虑免息期。
- 每月结算（settle函数）：每月1日结算利息。
- 年费（fee）：每年需要交一次年费（每年1月1日扣年费）。
4）计算信用卡账户的年利息：年利息 = 累加每月的月利息， 月利息 = 累加（每日欠款 *利率）。 
5）计算所有账户的总金额：所有账户的总金额 = 所有账户的余额之和 + 所有账户的年利。
6）完成日期类的设计，包括年、月、日、总天数等属性，实现日期间的距离计算。
"""


Bank_uml = """
@startuml
class Date {
    - year: int
    - month: int
    - day: int
    - totalDays: int
    + Date(year: int, month: int, day: int)
    + {const} distance(date: Date): int
}

class Accumulator {
    - lastDate: Date
    - value: double
    - sum: double
    + Accumulator(date: Date, value: double)
    + {const} getSum(date: Date): double)
}

abstract class Account {
    # id: int
    # balance: double
    # record(date: Date, amount: double, desc: string)
    + {const} getBalance(): double
    + {static} getTotal(): double

}

class SavingsAccount {
    - rate: double
    - lastDate: Date
    - value: double
    
    
    + withdraw(date: Date, amount: double, desc: string)
    + deposit(date: Date, amount: double, desc: string)
    + calculate_interest(date: Date): double
}

class CreditAccount {
    - credit: double
    - rate: double
    - fee: double
    + CreditAccount(date: Date, id: int, credit: double, rate: double, fee: double)
    + withdraw(date: Date, amount: double, desc: string)
    + deposit(date: Date, amount: double, desc: string)
    + calculate_interest(date: Date): double
}
' This is an inheritance relationship: SavingsAccount and CreditAccount inherit/extend Account
Account <|-- SavingsAccount
Account <|-- CreditAccount
 
SavingsAccount *-- Accumulator
CreditAccount *-- Accumulator

' This is an association relationship: SavingsAccount and CreditAccount have Date
SavingsAccount ..> Date
CreditAccount ..> Date
@enduml

"""

xlsx2csv_description = """
这个系统目的是将XLSX文件转化为CSV的软件工具，具体要求如下：
1）读取和写入XLSX文件：能够读取用户指定的输入输出文件路径，能够读取XLSX文件中的数据，并将其转换为CSV文件并保存。注意：一个XLSX文件路径可能包含多个XLSX文件。
2）多工作表支持：能够监测并且转换XLSX文件中的每个工作表，并输出以相应工作表命名的单独 CSV 文件。注意：一个XLSX文件可能包含多个工作表。
3）一致的数据转换：确保输出的 CSV 文件与相应 XLSX 文件的内容匹配。

"""
xlsx2csv_uml = """ 
@startuml
class workbook {
-sheet_relations : std::vector
-shared_string : std::vector
-my_archive : std::shared_ptr
-all_cells : std::unordered_map>
-string_idx : std::unordered_map
+workbook(const std::string&)
+write_to_csv(std::string)
}

class worksheet {
worksheet
-_name : const std::string
-_sheet_id : const std::uint32_t

-_cells : const std::vector
-row_num : std::uint32_t
-column_num : std::uint32_t
-row_info : std::vector>
+get_name() : const : std::string
+to_csv() : const : std::string
}

class archive {
-archive_content : std::unordered_map
-xml_content : std::unordered_map>
-archive_files : std::vector
+archive(const std::string&)
+get_sheet_relations() : : std::vector
+get_sheet_xml(const std::string&) : : std::shared_ptr
}

class global_functions_and_types {
sheet_desc : std::tuple
cell : std::tuple
string_to_idx(const std::string&) : : std::uint32_t
string_to_row_column(const std::string&) : : std::pair
strip(std::string) : : std::string
}

' This is a contain relationship: workbook contains worksheet
worksheet o-- workbook

' This is a usdependency relationship: workbook uses archive
workbook --> archive :uses


@enduml
"""

graph_traversal_software_tool_description = """This document outlines the requirements for a graph traversal software tool. The project aims to implement two graph traversals, including non-recursive depth-first and breadth-first for connected undirected and directed graphs. The software will use adjacency multilist and adjacency matrix structures for storing graph data and output the node visit sequence and the edge sets of the generated trees.

Goals: The primary goal is to develop a reliable and efficient graph traversal tool that supports multiple traversal algorithms and storage structures. It aims to accurately output traversal sequences and associated generated tree edge sets for both directed and undirected graphs.

Features and Functionalities: 
- Graph Traversal Algorithms: Implementation of non-recursive depth-first, and breadth-first traversals.
- Graph Storage Structures: Utilize adjacency multilist and adjacency matrix structures for graph data storage.
- Traversal Output: Output the node visit sequence and the edge sets of the generated trees for each traversal.}
- Input Flexibility: Accept graph data through specific input file formats.
- Support for Directed and Undirected Graphs: Handle both directed and undirected graphs efficiently.

Data input should be flexible, allowing users to input graphs via specific file formats. The specific format of the input file is as follows: the first line indicates whether it is a directed graph or not, with 0 representing an undirected graph and 1 representing a directed graph; each subsequent line contains the start end point and weight of an edge, separated using spaces.

The output file is formatted to print the adjacency matrix, then the adjacency table, and finally the results of the non-recursive dfs and bfs in that order.For example, the following example:
Adjacency Matrix：
0 0 0 0 0 
0 0 1 0 4 
0 0 0 9 2 
0 3 5 0 8 
0 0 0 6 0 
Adjacency Table：
0 1 -> 1 1 -> 2 4 -> ^ 
1 2 -> 2 2 -> 3 9 -> ^ 
2 4 -> 3 6 -> ^ 
3 3 -> 0 3 -> 1 5 -> 2 8 -> ^ 
Depth-first search (no recursion) 
1 2 4 3 
BFS: 
1 2 4 3 """

graph_traversal_software_tool_UML = """
@startuml
class AdjacencyListGraph {
        -bool _isDirected
        -int _vexNum
        -int _arcNum
        +vector~VertexType~ dfs_noRes()
        +vector~VertexType~ bfs()
        +vector~VertexType~ bfs(VertexType)
        +int locateVex(VertexType)
        +bool setVexer(vector~VertexType~)
        +bool setArcs(vector~tuple~~VertexType VertexType int~)
        +friend operator<< (ostream&, const AdjacencyListGraph&)
    }

    class ArcNode {
        -int adjVex
        -int weight
        -ArcNode* next
    }
    class _vNode{
        -VertexType v
        -ArcNode* next
    }

    class AdjacencyMatrixGraph {
        -bool _isDirected
        -int _vexNum
        -int _arcNum
        -int** arcMatrix
        -VertexType* vexList
        +int locateVex(VertexType)
        +bool setVexer(vector~VertexType~)
        +bool setArcs(vector~tuple~~int int int~)
        +friend operator<< (ostream&, const AdjacencyMatrixGraph&)
    }

    class Queue~T~ {
        -Node* _rear
        -Node* _front
        +void push(const T& data)
        +T pop()
        +T front()
        +bool empty()
    }

    class Node~T~{
        +Node* next
        +T data
    }

    class Stack~T~ {
        -const int DEFAULT_SIZE
        -T* _array
        -int size
        -int capacity
        +void push(const T& data)
        +T top()
        +void pop()
        +bool empty()
    }
@enduml
"""


