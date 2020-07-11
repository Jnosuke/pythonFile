fruits = {"apple" : 7, "orange" : 5, "peach" : 6}
while fruits:
    key = input("どのフルーツを取り出しますか？（qで終了）：")
    if key == "":
        continue
    elif key == "q":
        print("終了します")
        break
    try:
        value = fruits.pop(key)
        print(f"{key}は{value}個")
    except KeyError :
        print(f"{key}はありません")
    except Exception as error :
        print(error)
        break

else :
    print("もう空っぽです。 ")