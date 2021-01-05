x = ['a','e','i','o','u']

c = input("What's your name: ")

count = 0
for i in c:
    for j in range(len(x)):
        if i == x[j]:
            count += 1

print("count =",count)
