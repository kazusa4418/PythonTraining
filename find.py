# テキストからキーワードを探す
key = "find"

with open("ReadTester.txt", encoding="utf-8") as tf:
    # 1行ずつファイルを読む
    for i, line in enumerate(tf):
        # 文字列 key が行に含まれるか？
        if line.find(key) >= 0:
            print(i + 1, ":", line)
