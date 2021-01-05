print('''1)Create a new file
2)Display a new file
3)Add a new item in the file.
Select 1,2 or 3:''')

ch = int(input())

if ch == 1:
    file = open("subject.txt","w")
    file.write(input("Subject:"))
    file.write("\n")
    file.close()

elif ch == 2:
    file = open("subject.txt","r")
    print(file.read())
    file.close()

elif ch == 3:
    file = open("subject.txt","a")
    file.write(input("Subject:"))
    file.write("\n")
    file.close()

else:
    print("Incorrect choice!!")








