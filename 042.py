t = 0
for i in range(5):
    a = int(input("Num: "))
    b = input("Do you want to include? y/n: ")
    b = b.lower()
    if b == "y":
        t += a;


print("Total is ",t)
