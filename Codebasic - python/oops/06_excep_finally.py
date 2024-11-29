file = None

try:
    file = open("example.txt", "r")  # r = read mode 
    content = file.read()
    print(content)
except FileNotFoundError as fe:
    print("Error: The file was not found.")
finally:
    if file:
        file.close()
    print("File closed.")
