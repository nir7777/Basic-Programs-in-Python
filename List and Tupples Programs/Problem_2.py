#  Problem 2
# WAP to accept marks of 6 students and display them in a sorted manner
s1 = int(input("Enter  marks of student   number 1\n") );
s2 = int(input("Enter   marks of student   number 2\n") );
s3 = int(input("Enter  marks of student   number 3\n") );
s4 = int(input("Enter  marks of student   number 4\n") );
s5 = int(input("Enter  marks of student   number 5\n") );
s6 = int(input("Enter  marks of student   number 6\n") );
studmarks = [s1,s2,s3,s4,s5,s6];
studmarks.sort();

print(studmarks);