# Write a python program to print the contents of a directory using the os module.

# module import
import os

# specify the directory path
directory_path ='/' 

# list all the directory
contents = os.listdir(directory_path)

# print each file and directory namer
for i in contents:
          print(i)