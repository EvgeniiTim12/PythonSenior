from re import A


print("КАЛьКулятор")
while True:
    a=float(input("введіть першу змінну:"))
    b=float(input("введіть другу змінну:"))

    q=input("виберіть дію(додавання,ділення,віднімання,множення,степінь):")
    if(q=="додавання"):
        print(a+b)
    elif(q=="віднімання"):
        print(a-b)
    elif(q=="ділення"):
        if(b==0):
            print("На ноль ділити неможна!")
        else:
            print(a/b)
    elif(q=="множення"):
        print(a*b)
    elif(q=="степінь"):
        print(a**b)
    else:
        print("ви вказали дію неправильно")
