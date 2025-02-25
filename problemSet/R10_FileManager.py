# A file system contains information from multiple documents.
#  The document can be added and removed from the file, and all the documents can be listed.
#  Each document uses an editor suitable for creation.
#  A document contains the document's name, creation date, author information, and size.
#  The user determines the assignment of the editor to the documents.
#  Each editor has a name and file management task.
#  The system has three editors that allow you to manage documents: Text Editor, Image Editor, and Video Editor.


descriptionList = [
# """文件系统，包括以下需求：
# 1）一个文件系统包含来自多个文档的信息。文档信息包含名称、创建日期、大小和作者姓名。
# 2）管理文档。允许用户在文件系统中添加和删除文档，并且可以列出所有文档。
# 3）管理编辑器。每个编辑器都有一个名称和一个文件管理任务。系统有三个编辑器允许用户管理文档：文本编辑器，图像编辑器和视频编辑器。每个文档都使用适合创建的编辑器。
# 4）指定/分配编辑器。用户可以指定/分配文档编辑器管理文档；也可以创建新的编辑器（例如音频编辑器、代码编辑器）添加到系统中。"""
# # 用户可以创建新的编辑器，指定编辑器管理。
# # 保证编辑器里文档列表和文档的一致性。
# ,
"""文件系统，包括以下需求：
1）一个文件系统包含来自多个文档的信息。文档信息包含名称、创建日期、大小和作者姓名。
2）用户可以从文件系统中添加和删除文档，并且可以列出所有文档。
3）每个文档都使用适合创建的编辑器。每个编辑器都有一个名称和一个文件管理任务。系统已有三个编辑器允许用户管理文档：文本编辑器，图像编辑器和视频编辑器。
4）用户可以决定文档编辑器的分配。
5）用户可以创建新的特定类型的编辑器，例如音频编辑器、代码编辑器，指定编辑器管理合适的文档。"""
,
"""A file system, with the following specific requirements:
1) A file system  contains information from multiple documents including the document's name, creation date, size and the author's name.
2) The user can add and delete documents from the file system, and list all the documents.
3) Each document uses an editor suitable for creation. Each editor has a name and a file management task. The system has three editors that allow you to manage documents: Text Editor, Image Editor, and Video Editor.
4) The user determines the assignment of the editor to the documents.
"""
# 5) The user can create new and specific types of editors, such as audio editors, code editors, and specify the editor to manage the documents."""
,
"""文件系统，包括以下需求：
1）一个文件系统包含来自多个文档的信息。文档信息包含名称、创建日期、大小和作者姓名。
2）用户可以从文件系统中添加和删除文档，并且可以列出所有文档。
3）每个文档都使用适合创建的编辑器。每个编辑器都有一个名称和一个文件管理任务。系统已有三个编辑器允许用户管理文档：文本编辑器，图像编辑器和视频编辑器。
4）用户可以决定文档编辑器的分配。
5）允许用户创建新类型的编辑器，例如音频编辑器、代码编辑器，指定编辑器管理合适的文档。"""
,
"""A file system, with the following specific requirements:
1) A file system  contains information from multiple documents, including the document's name, creation date, size and the author's name.
2) The user can add and delete documents from the file system, and list all the documents.
3) Each document uses an editor suitable for creation. Each editor has a name and a file management task. The system has three editors that allow you to manage documents: Text Editor, Image Editor, and Video Editor.
4) The user determines the assignment of the editor to the documents.
5) The user can create new editors, specify the editor to manage the documents."""
,
"""A file system, with the following specific requirements:
1) A file system stores multiple documents. Each document includes name, creation date, size, and the author's name.
2) The user can add and delete documents from the file system, and list all the documents.
3) Each document uses an editor suitable for creation. Each editor has a name and a file management task. The system has three editors that allow you to manage documents: Text Editor, Image Editor, and Video Editor.
4) The user determines the assignment of the editor to the documents.
5) The user can create new editors, specify the editor to manage the documents."""
]


umlList = ["""
```plantuml
@startuml
class User {
    + assignEditorToDocument()
    + createNewEditor(name, task)
}

class Document {
    - string name
    - date creationDate 
    - string authorName
    - long size
    
}

class FileSystem {
    + addDocument()
    + deleteDocument()
    + listDocuments()
}

abstract class Editor {
    - string name
    - string task
}

class TextEditor {
    + editText()
}

class VideoEditor {
    + editVideo()
}

class ImageEditor {
    + editImage()
}

FileSystem "1" -- "0..*" Document : contains
Document "1" -- "1" Editor : uses
User "1" -- "*" Editor : manages
@enduml
```"""]