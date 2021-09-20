# Problem 1
''' WAP to create a dictionary of hindi words with values as 
 their english translation Provide user with an option to look it up'''


hintoeng={
    "Pankha" : "Fan",
    "Kitab" : "Book"
}
print("options are\n", hintoeng.keys())
a = input("Please enter any word from above options\n")
print("Meaning of your word is", hintoeng[a])
