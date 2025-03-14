descriptionList = ["""
The system functional requirements are as follows:
+ There are robots that have an id. Robots can be of type cleaning robot and transport robot. Each robot can perform multiple Task. Each task has an id.
+ When a robot performs a task, the robot must check if the location is valid (CORRIDOR or ROOM), and can throw an error for invalid locations. When the location is valid, the task execution is recorded. A task execution has an id, a start time and a location.
+ Each robot can retrieve the latest TaskExecution records for the robot.
+ Cleaning robots check battery levels before performing tasks and trigger low-battery notifications."""
                   ,
    """"There are robots that have an id. Robots can be of type cleaning robot and transport robot. Robots can perform tasks, which have an id. When a robot performs a task, the task execution is recorded. A task execution has an id, a start time and a location. The location can be either corridors or rooms."""
]


umlList = ["""
```plantuml
@startuml
enum Location {
  CORRIDOR
  ROOM
}
           
abstract class Robot {
  - string id
  + void performTask(Task,location)
  + void retrieveLatestExecution()
}
           
class CleaningRobot {
  - int batteryLevel
           
  + void performCleaningTask()
  + void checkBattery()
}
           
class TransportRobot {
}
           
class Task {
  - string id
  - void initiateTaskExecution(Robot, Location)
}

class TaskExecution {
  - string id
  - int startTime
  - Location location
  
}


Robot "*" -- "*" Task : performs

CleaningRobot --|> Robot
TransportRobot --|> Robot

(Robot, Task) .. TaskExecution

@enduml
```
"""]