# Sichuan University 2016-2017, BeWell App
# Purpose 
# This document outlines the usage and implementation of the Bewell app. 
# Scope
# The Bewell app is mainly for those who plan to lose or gain weight and require a planned medium. 

# Requirement
# The application will be able to record exercises, repetitions, and the diet followed. The app will have a calendar layout where the user can click on a specific day to find all the events and diets scheduled for the day. Further, the activities will be monitored and recorded for the same date.

# The application can suggest videos and diets and schedule them on the calendar. The app will take the inputs from the user and suggest videos, diets, and schedules for the user. A database of the videos (can be from youtube) is created. The videos will be mapped based on user inputs, like what part of the body the user is focussed on. For a low-data device case, thumbnails from the video at regular intervals can be mapped instead of the videos. Further, diet is also planned similarly.

# The application will track the user's running activity and convert them into calories burnt. Running speed, calories burnt, the track ran, etc., will be monitored and recorded for the day in the calendar. The app will take the device's GPS location and track the user's running activity. This will work only with the user's internet, and the location is "ON." This helps in calculating the calories burnt by the user. For calculation, the time taken by the user and the distance traveled by the user will be considered.

# The application will track the user's running activity and convert them into calories burnt. Running speed, calories burnt, the track ran, etc., will be monitored and recorded 
# for the day in the calendar. The app will take the device's GPS location and track the user's running activity. This will work only with the user's internet, and the location is "ON." This helps in calculating the calories burnt by the user. For calculation, the time taken by the user and the distance traveled by the user will be considered.

# The application will be able to work offline/in low-data mode. Since network availability is not available in many scenarios, the app will be working during offline and low data mode. For a low data mode, pictures from the videos at regular intervals will be provided instead of videos. Thus the information is conveyed with very less data consumption. Further, the app will store the data during offline mode and upload the same to the server whenever the device goes online.

# 四川大学2016-2017，BeWell App
# 目的
# 本文档概述了Bewell应用程序的使用和实现。

# 范围
# Bewell应用程序主要是为那些计划减肥或增重，需要计划好的介质的人设计的。


# 要求
# 该应用程序将能够记录锻炼、重复和随之而来的饮食。该应用程序将有一个日历布局，用户可以点击特定的一天，以找到当天的所有活动和饮食计划。此外，这些活动将在同一天进行监测和记录。


# 该应用程序可以推荐视频和饮食，并将它们安排在日历上。
# 该应用程序将接收用户的输入，并为用户推荐视频、饮食和日程安排。
# 创建一个视频数据库（可以来自youtube）。
# 视频将根据用户的输入进行映射，比如用户关注的身体部位。
# 对于低数据量的设备，可以按固定时间间隔映射视频的缩略图，而不是视频。
# 此外，饮食计划也类似。


# 该应用程序将跟踪用户的跑步活动，并将它们转换为消耗的卡路里。
# 跑步速度，燃烧的卡路里，跑步的轨道等，将被监测和记录在日历中的一天。
# 该应用程序将获取设备的GPS位置，并跟踪用户的运行活动。
# 这只适用于用户的互联网，并且位置是“ON”。
# 这有助于计算用户消耗的卡路里。
# 在计算时，将考虑用户所花费的时间和用户所行驶的距离。

descriptionList = [
"""系统需求：
1）管理用户信息（姓名、性别）。
2）用户记录跑步活动数据（日期、跑步速度、消耗卡路里和跑步距离）。
3）用户记录每日饮食信息（日期、食物名称、摄入重量（kg））。
4）用户查询某种食物单位重量（0.1kg）的卡路里，可以使用标准接口 calculateFoodCaloriesPerUnit(foodName)。
5）用户计算日净摄入卡路里量 = 每日摄入食物卡路里和 - 每日跑步消耗卡路里。 每日摄入食物卡路里和 = Σ（每日摄入的食物量 / 单位重量 * 单位重量的卡路里）。"""
,
"""The system requirements are as follows:
1) Manage the user's information including name and sex.
2) The user can record running activities including date, speed, calories burnt, and distance.
3) The user can record daily diets including date, food name and weight (kg). 
4) The user can query the calories of a unit weight (0.1kg) of a certain food. The system provide a standard interface calculateFoodCaloriesPerUnit(foodName) to query the calories of a unit weight (0.1kg) of a certain food.
5) The user can calculate the net daily calorie intake = daily calorie intake from food - daily calorie burnt from running. Daily calorie intake from food = Σ (daily intake weight of food / a unit weight * calories of a unit weight)."""
,
"""系统需求：
1）管理用户信息（姓名、性别）。
2）记录用户的跑步活动数据（跑步速度、消耗卡路里和跑步距离）。
3）记录用户每日饮食信息（食物名称、摄入重量（kg））。
4）查询某种食物单位重量（0.1kg）的卡路里。提供标准接口 calculateFoodCaloriesPerUnit(foodName)。
5）计算用户某一天的日净摄入卡路里量 = 当日摄入食物卡路里和 - 当日跑步消耗卡路里。 当日摄入食物卡路里和 = Σ（当日摄入的食物量 / 单位重量 * 单位重量的卡路里）。"""
,
"""Here’s an English variation of the functional requirements:
- User Information Management: The system should handle user details, including name and gender.
- Running Activity Management: The system should manage user’s running records, including date, speed, calories burned, and distance covered.
- Daily Diet Tracking: The system should allow users to log their daily food intake, including date, food item, and consumed weight (in kilograms).
- Food Calorie Query: The system must provide a standard interface, calculateFoodCaloriesPerUnit(foodName), to retrieve the calorie value for a unit weight (0.1 kg) of a specific food item.
- Net Daily Calorie Calculation: The system should compute the user’s net daily calorie intake for a specific date. Net daily calorie intake is calculated as:
Daily calorie intake from food - Daily calorie expenditure from running.
Where:
Daily calorie intake from food = Σ (daily consumed weight of food / unit weight * calories per unit weight)."""
,
"""The system requirements are as follows:
1) Manage the user's information, including name and sex.
2) Manage the user's running activities, including date, speed, calories burnt, and distance.
3) Record the user's daily diet, including date, food name, and weight (kg). 
4) Query the calories of a unit weight (0.1kg) of a certain food. The system provide a standard interface calculateFoodCaloriesPerUnit(foodName) to query the calories of a unit weight (0.1kg) of a certain food.
5) Calculate the user's net daily calorie intake by subtracting the calories burned through running from the total calories consumed from food. Daily calorie intake from food = Σ (daily intake weight of food / a unit weight * calories of a unit weight)."""


,
"""The system requirements are as follows:
1) Manage the user's information, including name and sex.
2) Manage the user's running activities, including date, speed, calories burnt, and distance.
3) Record the user's daily diet, including date, food name, and weight (kg). 
4) Query the calories of a unit weight (0.1kg) of a certain food. The system provide a standard interface calculateFoodCaloriesPerUnit(foodName) to query the calories of a unit weight (0.1kg) of a certain food.
5) Calculate the user's net daily calorie intake, which is the total calories ingested from food minus the calories burned from running. Daily calorie intake from food = Σ (daily intake weight of food / a unit weight * calories of a unit weight)."""
,
"""The system requirements are as follows:
1) Manage the user's information, including name and sex.
2) Manage the user's running activities, including date, speed, calories burnt, and distance.
3) Record the user's daily diet, including date, food name, and weight (kg). 
4) Query the calories of a unit weight (0.1kg) of a certain food. The system provide a standard interface calculateFoodCaloriesPerUnit(foodName) to query the calories of a unit weight (0.1kg) of a certain food.
5) Calculate the user's net daily calorie intake. The net daily calorie intake = daily calorie intake from food - daily calorie burnt from running. Daily calorie intake from food = Σ (daily intake weight of food / a unit weight * calories of a unit weight)."""

]

umlList = [
"""
```plantuml
@startuml
class User {
    - string name
    - string sex

    + double calculateNetDailyCalories(date)
    }

class RunningActivity {
    - date date
    - float speed
    - float caloriesBurnt
    - float distance
    }

class Diet {
    - date date
    - string foodName
    - float weight
    }

User "1" -- "0..*" RunningActivity
User "1" -- "0..*" Diet
@enduml
"""
]










