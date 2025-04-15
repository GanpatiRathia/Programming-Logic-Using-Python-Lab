"""
What is File Handling in Python?
File handling is the process of performing operations like create, open, read, write, and close on files stored on your computer.

Python provides built-in functions and methods to work with both text and binary files easily.

Used for data storage, logging, configuration files, saving user data, etc.

Key Steps in File Handling
Open the file – using open()

Perform operations – like read(), write(), or append()

Close the file – using close()

pen() Function Syntax

file = open("filename", "mode")

"filename": name of the file (can include path)

"mode": defines what you want to do with the file

File Modes in Python
Mode	Name	Description
'r'	Read	Default mode; opens file for reading only
'w'	Write	Overwrites file; creates if not exists
'a'	Append	Adds content to end; creates if not exists
'x'	Create	Creates file; error if file exists
'b'	Binary	Use for binary files like images/videos
't'	Text	Default mode; use for text files
'+'	Read and Write	Combines read and write modes
"""
