a = input("Type a word: ")
a = a.lower()
if a[0] == 'a' or a[0] == 'e' or a[0] == 'i' or a[0] == 'o' or a[0] == 'u':
    print((a+"way").lower())
else:
    print(((a[1:]+a[0]+"ay").lower()))
