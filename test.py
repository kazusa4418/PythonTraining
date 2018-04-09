num = int(input("整数を入力してください > "))

nums = []

for i in range(2, num):
    if num % i == 0:
        nums.append(str(i))

nums = ",".join(nums)

print(nums)

