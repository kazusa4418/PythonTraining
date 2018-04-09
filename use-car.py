# 定義したクラスを含むモジュールを取り込む
from car import Van
from car import Camper

# ワゴン車を作成
car1 = Van("Taro")
car1.turn_left()
car1.show_status()

# キャンピングカーを作成
car2 = Camper("Jiro")
car2.turn_right()
car2.show_status()
car2.make_ice()
