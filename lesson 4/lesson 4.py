name=str(input("Як вас звуть:"))
surname=str(input("Яке у вас прізвище"))
age=int(input("Скільки вам років:"))
city=str(input("З якого ви міста\села:"))
kraina=str(input("З якої ви країни:"))
if(type(name==int)):
    print("так не буває,ваше ім'я не ",name)
elif(type(surname==int)):
    print("так не буває, ваше прізвище не",surname)
else:  
    print("Ім'я: ",name)
    print('Прізвище: ',surname)
    print('Вік: ',age)
    print('Місто\село:',city)
    print('Країна: ',kraina)
