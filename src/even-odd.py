# 偶数か奇数か判定する数を入力する
num = int(input("奇数か偶数か判定する数を入力してください > "))

# 入力された値をもとに奇数か偶数か判定する
if num % 2 == 0:
    print("偶数です")
else:
    print("奇数です")
