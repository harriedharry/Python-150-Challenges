s = '''There are 40 green bottles hanging on the wall, 
40 green bottles hanging on the wall, 
and if 1 green bottle should accidentally fall”.
“How many green bottles will be hanging on the wall?" '''

print(s)
i = 40
a = int(input("How many: "))
while i != 0:
    if a != i-1:
        while a != i-1:
            print("No,Try Again: ")
            a = int(input())
    print("There will be ",a," bottles will be hanging in the wall")
    i -= 1

    a = int(input("How many now: "))

print("There are no bottles hanging in the wall.")
