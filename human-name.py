# クラスの定義
class HumanName:
    """ 人をあらわすクラス """
    def setName(self, name):
        """ 名前を設定するメソッド """
        self.name = name

    def getName(self):
        """ 名前を取得するメソッド """
        return self.name


# インスタンスを作成
taro = HumanName()
taro.setName("Taro")
print(taro.getName())
