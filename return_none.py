def calc(num):
    unit_price = 180
    try :
        num = float(num)
        return num * unit_price
    except :
        return "数値を入れてください"

while True :
    num = input("個数を入れてください。（qで終了）")
    if num == "" :
        continue
    elif num == "q" :
        break

    result = calc(num)
    print(result)
