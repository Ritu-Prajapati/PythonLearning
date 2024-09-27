import os

#specific directory you want to list
directory_path = '/'

#list all directories and files in the specified path
contents = os.listdir(directory_path)

# print each file in directory name 
print(contents)

# getcwd = get current working directory

'''
# Get the current working directory
current_directory = os.getcwd() 

# List the contents of the directory
directory_contents = os.listdir(current_directory)

# Print the contents of the directory
for item in directory_contents:
    print(item)'''
