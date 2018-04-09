# coding=utf-8
# 素数を返すイテレータ
def prime(max):
    num = 2

    while num <= max:
        flag = True
        for value in range(2, num):
            if num % value == 0:
                flag = False
                break

        if flag:
            yield num

        num += 1


# イテレータを得る
it = prime(50)

# 画面に出力
for i in it:
    print(i, end=",")
