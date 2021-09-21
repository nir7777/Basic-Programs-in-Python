# Problem 1
# Write a program to open 3 files 1.txt,2.txt,3.txt. If any of these files are not present, a message without
#  exiting the program must be printed prompting the same.

def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"File {filename} is not available")


readFile("t1.txt")
readFile("t2.txt")
readFile("t3.txt")
