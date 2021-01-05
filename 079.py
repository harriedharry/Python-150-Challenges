nums = []

print("Enter 3 nums: ")
for i in range(3):
    nums.append(int(input()))

print(nums)

dec = input("Do you still want last num: ")

if dec == "no":
    del nums[2]

print(nums)
