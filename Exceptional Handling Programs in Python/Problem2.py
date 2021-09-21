# Problem 2
# Write a program to print third,fifth,and seventh element from a list using enumerate function

a = [25, 45, 36, 98, 78, 4, 14]
index = 2
for index,item in enumerate(a):
    if index==2 or index==4 or index==6:
        print(item)

