# 価格表のデータを変数priceに代入
prices = {"バナナ": 300, "リンゴ": 200, "マンゴー": 400}

# リンゴがあるか確認
exist = "リンゴ" in prices

if exist:
    print(prices["リンゴ"])
else:
    print("リンゴは存在しません")

exist = "マンゴー" in prices

if exist:
    print(prices["マンゴー"])
else:
    print("マンゴーは存在しません")