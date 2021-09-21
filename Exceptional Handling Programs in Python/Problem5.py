# Problem 5
# Store the multiplication tables generated in Problem 3 in a file named TAbles.txt

num = int(input("Enter number"))
table=[num*i for i in range(1,11)]
print(table)
with open("tables.txt","a") as f:
    f.write(str(table))
    f.write('\n')