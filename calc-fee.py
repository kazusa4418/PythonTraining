# 子供の人数を入力させる
child_num = int(input("子供料金(13歳未満)は何人いますか > "))
normal_num = int(input("通常料金(13~64歳)は何人いますか > "))
old_num = int(input("年配者料金(65歳以上)は何人いますか > "))

# 各料金を計算
child_value = child_num * 500
normal_value = normal_num * 1000
old_value = old_num * 700

total_value = child_value + normal_value + old_value

# 団体割引が入るか確認
if (child_num + normal_num + old_num) >= 10:
    print("団体割引があります")
    total_value *= 0.8
else:
    print("割引はありません")

# 料金表を表示
print("子供料金\t:{child_num}人 × 500 = {child_value}円".format(child_num=child_num, child_value=child_value))
print("通常料金\t:{normal_num}人 × 1000 = {normal_value}円".format(normal_num=normal_num, normal_value=normal_value))
print("年配者料金\t:{old_num}人 × 700 = {old_value}円".format(old_num=old_num, old_value=old_value))
print("合計: {0}人 {1}円".format(child_num + normal_num + old_num, total_value))