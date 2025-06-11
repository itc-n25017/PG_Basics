nunber=[13,25,1,5,14,2,35,28]
while True:
    anser=input("数字を当ててみよ")
    if anser=="q":
        break
    try:
        anser=int(anser)
    except ValueError:
        print("数字を入力するか、ｑで終了します")
    if anser in nunber:
        print("正解")
    else:
        print("不正解")
