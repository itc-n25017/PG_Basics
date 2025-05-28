yuto={"身長": "165cm",
      "食べ物": "ゴーヤーチャンプルー",
      "ゲーム": "VAGLANT",
      "飲み物": "ルートビア",
      "スト６": "ケン"}

n=input("気になることを入力")
if n in yuto:
    yuto=yuto[n]
    print(yuto)
else:
    print("そんな質問すんなや！")
