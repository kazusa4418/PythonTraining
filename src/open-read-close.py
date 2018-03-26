# coding=utf-8
# ファイルを開く
a_file = open("ReadTester.java", encoding="utf-8")

# テキストを読む
s = a_file.read()

# ファイルを閉じる
a_file.close()

# 結果を表示する
print(s)
