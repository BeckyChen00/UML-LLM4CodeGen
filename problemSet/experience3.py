descriptionList = ["""The system functional requirements are as follows:
1) Theater Management. A theater has a location, and can play multiple plays.
2) Play Management. A play has a name and can be played either at day or night. The play can be musicals or operas. 
3) Person Manage. A person has a name. There are two types of persons: authors and participants.
4) Session Management. A particular participant acts in a particular session of a play. Each session has a start time and an end time. 
5) A Play can have multiple sessions. A new session can be added to a play only if there is no time conflict between the new session and the existing sessions of the play.
6) A session can add a new participant only if the time slot of the new session does not overlap with any of the sessions in which the participant is already involved.
7) Plays are written by one or more authors. 
8) Plays involve multiple participants who act in them.
9) The participant can view all involved sessions of all plays.
""",
"""Theaters have a location, and they can play any play, which can be musicals or operas. Plays have a name and can be played either at day or night. Plays are written by one or more authors, who have a name. There are many participants who act in a play, participants also have a name. 
A particular participant acts in a particular session of a play, where each session begins and ends at a specific time. Both authors and participants are persons."""]

umlList = ["""
```plantuml
@startuml
Enum Time{
  Day
  Night
}
           
abstract class Person {
  - string name
}
           
class Author {
}
           
class Participant {
  + void viewSessions()
}

class Session {
  - int startTime
  - int endTime
           
  + void addParticipant(Participant)
}
           
class Theater {
  - string Location
}
           
abstract class Play {
  - string name
  - Time time
  
  + void addNewSession(Session)

}
           
class Musical {
}
           
class Opera {
}


' This is a bidirectional association between Session and Participant 
Session "*" -- "*" Participant : participants

Play  *-- "*" Session         
Play "*" -- "*" Theater : plays
Author "1..*"  -- "*" Play : writes


Person <|-- Author
Person <|-- Participant
Play <|-- Musical
Play <|-- Opera

@enduml
```
"""]