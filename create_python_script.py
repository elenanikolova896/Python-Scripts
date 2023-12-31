#The create_python_script function creates a new python script in the current working directory, 
#adds the line of comments to it declared by the "comments" variable, and returns the size of the new file.

def create_python_script(filename):
    comments = "#Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
        filesize = file.tell()
    return filesize

print(create_python_script("program.py"))
