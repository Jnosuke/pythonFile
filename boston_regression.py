from sklearn import datasets
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

#データセットを読み込む
boston = datasets.load_boston() #ボストン市の住宅価格と連携データ
boston_df = DataFrame(boston.data) #DataFrame型にする
boston_df.columns = boston.feature_names #列名を設定する
boston_df["Price"] = boston.target #住宅価格を追加する
print(boston_df[:10]) #最初の10行だけ

#訓練データを作る
rooms_train = DataFrame(boston_df["RM"])
y_train = boston.target #ターゲット（住宅価格）
model = linear_model.LinearRegression() #回帰モデルを作る
model.fit(rooms_train, y_train) #訓練する

#部屋数のテストデータを作る
rooms_test = DataFrame(np.arange(rooms_train.values.min(), rooms_train.values.max(),  0.1))
price_test = model.predict(rooms_test) #モデルを使って住宅価格を予想する
#グラフを表示する(部屋数と住宅価格)
plt.scatter(rooms_train.values.ravel(), y_train, c= "b", alpha = 0.5) #訓練データ
plt.plot(rooms_test.values.ravel(), price_test, c = "r") #回帰直線
plt.title("Boston House Price dataset")
plt.xlabel("room")
plt.ylabel("price $1000's")
plt.show()
