# 単語の出現回数をカウント
text = """
Keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# 単語を区切る
text = text.replace(";", "")
text = text.replace(",", "")
text = text.replace(".", "")
words = text.split()

# 単語を数える
counter = {}

for w in words:
    # 小文字に変換
    ws = w.lower()
    # もじ辞書型にすでにキーがあれば値を1つ追加
    if ws in counter:
        counter[ws] += 1
    # もし辞書型にキーがなければ、値を１としてキーも登録
    else:
        counter[ws] = 1

# 結果を表示
for k, v in sorted(counter.items()):
    if v >= 3:
        print(k, v)
