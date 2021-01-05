x = []

print("Who are the 3 people,do you want to invite in the party?: ")

for i in range(3):
    x.append(input())

more = input("Do you want more?")
more = more.lower()

while more != "no":
    x.append(input("What's the name? "))
    more = input("Do you want more? ")

print(x)
