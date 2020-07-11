from random import randint

number = []

while len(number) < 10:
    n = randint(-10, 90)
    if n < 0 :
        print("中断されました")
        break
    
    if n in number :
        continue
        
    number.append(n)
    
else :
    print(number)