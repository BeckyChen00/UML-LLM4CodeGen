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


University_description = """
高校教师课程教学管理系统，能够实现以下功能：
1）管理教师数据，教师数据包含教师编号、姓名、性别、职称（教授/副教授/讲师）、基本工资等信息。
2）管理教师的课程信息，包括课程编号、课程名称、学分、学时、课程类型（选修/必修）等信息。
3）计算教师的工资，工资计算规则为：工资=基本工资+课时费*计费学时。一个老师可以教多门课程。
4）课时费用根据教师的职称不同而不同，教授每学时100元，副教授每学时80元，讲师每学时50元。注意：
5）计费学时根据课程类型不同而不同，必修课每课时2学时，选修课每课时1学时。

"""

Uni_UML = """
@startuml
enum professionalTitle{
    professor
    associateProfessor
    lecturer
}

class Teacher {
    - string tid
    - string name
    - boolean sex
    - professionalTitle prof_Title
    - double basicSalary

    + double calculateSalary()
    + double getCourseFeePerHour()

    
}

enum CourseType{
    compulsory
    elective
}

class Course {
    - string cid
    - string name
    - double credit
    - double hours
    - CourseType type

    + double getPaidHours()
}

' Teacher associate Course
Teacher *-- "*" Course: teaches 
@enduml
"""