city = input("調べる地名: ")
members = {"東京": 21, "大阪": 16, "福岡": 14}

try:
    value = members[city]
    print(f"{city}の値は{value}です")
except KeyError:
    print(f"{city}のデータありません")
except Exception as error:
    print(error)
