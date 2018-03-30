import json

# 辞書型のデータ
data = {
    "no": 5,
    "code": ("jas", 1, 19),
    "scr": "be quick to listen, slow to speak, slow to anger"
}

# ファイルへ書き込む
fileName = "test.json"

with open(fileName, "w") as fp:
    # json形式で保存
    json.dump(data, fp)

# ファイルから読み込む
with open(fileName, "r") as fp:
    r = json.load(fp)
    print("no=", r["no"])
    print("code=", r["code"])
    print("scr=", r["scr"])

