from random import randint
miss = 0  # 間違えた数
correct = 0  # 正解数
print("問題！3回間違えたら終了。qで止める")

while miss < 3:
    a = randint(0, 100)
    b = randint(0, 100)
    ans = a + b

    # 問題を出題し、キーボードからの入力待ちにする
    question = f"{a} + {b}は？"
    value = input(question)

    # qと入力されたら中断する
    if value == "q":
        break  # ブレイクする

    # 正解かどうか判定する
    if value == str(ans):
        correct += 1
        print("正解です！")

    else:
        miss += 1
        print("間違い", "x" * miss)  # ミスの数だけxを表示する

print("-" * 20)
print("正解：", correct)
print("間違い：", miss)
