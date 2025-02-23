"""This text was used in a software engineering exam at our chair.
A timbered house consists of 5–10 logs, 200–400 mud bricks, and 1,000 to 2,000 nails.
Each building material, whether log, brick, or nail, is a component in exactly one timbered house.
Each timbered house has a certain number of rooms and floors.
For the construction of a timbered house is at least one carpenter in charge, which has a name and an individual hourly wage.
To construct a timbered house, each carpenter uses tools consisting of one hammer and one saw.
Any carpenter can work on up to one timbered house at the same time.
"""
descriptionList = ["""
木屋建造订单管理系统，具体包含以下需求：
1）管理客户：包括姓名、地址。
2）管理木匠：包括名字、日薪。
3）管理订单：每个订单包括编号、建筑材料清单（原木数量、泥砖数量、钉子数量）、建设起止时间、是否已付款。
4）一个客户可以创建多个订单。
5）一个订单可以被分配给多位木匠完成；每位木匠可以参与多个订单。订单可以被分配给一位木匠，当且仅当订单建设起止时间与木匠已参与的订单时间没有重叠。
6）每个订单应付费用包含建筑材料费和人工费。建筑材料费 = 原木数量 * $10 + 泥砖数量 * $10 + 钉子数量 * $1。人工费 = 木匠日薪 * 订单时长。订单时长可以使用已知函数 calculateDuration(startTime, endTime)。
7）每位客户计算未付的订单费用之和。
""",
"""
Wooden House Construction Order Management System, with the following specific requirements:
1) Manage customers information (name and address).
2) Manage carpenters information (name and daily wage).
3) Manage orders. Each order includes an order number, a list of building materials (amount of logs, amount of mud bricks, amount of nails), construction start and end times, and payment status.
4) A customer can create/have/own multiple orders.
5) An order can be assigned to multiple carpenters to complete; each carpenter can participate in multiple orders. An order can be assigned to a carpenter only if there is no overlap in the construction start and end times with the orders the carpenter is already involved in.
6) The payable fee for each order includes the cost of building materials and labor. The cost of building materials = amount of logs * $10 + amount of mud bricks * $10 + amount of nails * $1. Labor cost = carpenter's daily wage * order duration. The order duration can be calculated using the known function calculateDuration(startTime, endTime).
7) Each customer can calculate the total unpaid order costs.
"""]

umlList = ["""
```plantUML
@startuml
class Customer {
    - string name
    - string address

    + double calculateTotalUnpaidOrderFee()
}

class Order {
    - string oid
    - int amountOfLogs
    - int amountOfMudBricksNumber
    - int amountOfNailsNumber
    - boolean paymentStatus
    - date startTime
    - date endTime
    
    + double calculateOrderFee()
}

class Carpenter {
    - string name
    - double dailyWage
}

Customer "1" -- "0..*" Order: createdOrders
Order "0..*" -- "1..*" Carpenter: assignedCarpenters
@enduml
"""]


