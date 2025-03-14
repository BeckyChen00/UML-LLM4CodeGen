# 目前的问题是 生成的方法没有实际内容。

descriptionList=[
"""The system functional requirements are as follows:
1) Manage person information, including name and identifier. 
+ Track parent-child relationships between persons. Every Person is the child of another person (except for one root Person who has no parent). Every Person can have an indeterminate number of children.
+ Track ancestors of a Person. A person has an indeterminate number of ancestors (e.g., father, grandfather, etc.). The ancestors of a Person are their father and the ancestors of their father.
+ Search the degree of each ancestor of a Person. The degree is 1 for the father, 2 for the grandfather.

2) Manage resource information. Each resouce has a name. 
+ There are two types of resources: Files and Folders. Each Folder can contain an indeterminate number of Resources (both Files and Folders).
+ Each resource belongs to a Folder and cannot exist outside of a Folder. However, there will be one root Folder that does not belong to any other Folder.

3) Manage user information. The user is a specialized type of person, in addition to a name and an identifier, also has a password to access resources. 
+ A user can access an indeterminate number of resources. Each resource can be accessed by an indeterminate number of Users. 
+ A user can search all accesible resources.
+ A user can edit the file content only if the user has editing access.

4) Manage access control. 
+ Grant/Revoke users access to specified resources, including viewing and editing permissions.
+ Check whether the user has permission to view/edit the specified resource.

""",

"""A Person has a name and an identifier. Every Person is the child of another Person and can have an indeterminate number of children (however, there will be one Person who is not the child of any other Person). A Person has an indeterminate number of ancestors (the ancestors of a Person are their father and the ancestors of their father). We will be interested in knowing the degree of each ancestor of a Person (1 for the father, 2 for the father's father, etc.).
A Resource has a name. There are two types of Resources: Files and Folders. 
Every resource belongs to a Folder and cannot exist outside of a Folder (however, there will be one Folder that does not follow that rule: the root Folder does not belong to any other Folder). Each Folder contains an indeterminate number of Resources.
A User is a Person who, in addition to a name and an identifier, also has a password to access an indeterminate number of Resources, and each Resource can be accessed by an indeterminate number of Users. When a User can access a resource, we will be interested in knowing if they can view it and if they can edit it."""
]

umlList=["""
```plantuml
@startuml
class Person {
  - string name
  - string identifier
  
  + int searchDegreeofAncestor(Ancestor)
}

class Ancestor {
  - int degree
}

class User {
  - string password
         
  + List<Resource> searchAccesibleResources()
  + void changeFileContent(File)
}

class Resource {
  - string name
}

class File {
}

class Folder {
}

class Access {
  - boolean canEdit
  - boolean canView
         
  + void grantAccess(User, Resource, canEdit, canView)
  + void revokeAccess(User, Resource)
  + boolean hasPermission(User, Resource)
}


Person "0..1" -- "*" Person : isChildOf
Person "*" -- "*" Person : ancestor
Person <|-- User 
User "*" *-- "*" Resource 
Folder "0..1" *-- "*" Resource: belongsTo
Resource <|-- File
Resource <|-- Folder

(User, Resource) .. Access
(Person, Person) .. Ancestor
@enduml
```
"""]