import random
xiti=random.randint(0,50)
xxitu=random.randint(0,50)
xriti=random.randint(0,30)
xxritu=random.randint(0,30)
class Bebrik():
    print("Привіт,обери своїх воїнів")
    def __init__(self,name,age,power,prizvanie):
        self.name = name
        self.age=age
        self.power=power
        self.prizvanie=prizvanie
        print("готово")
    def show(self):
        print("Ім'я:",self.name)
        print("Вік:",self.age)
        print("Сила",self.power)
        print("Професія:",self.prizvanie)


            

aaa=Bebrik(name=input("Введіть ім'я:"),age=int(input("Введіть вік:")),power=int(input("Введіть силу:")),prizvanie=input("Введіть професію(лучник\мечник\маг):"))
boec=Bebrik(name=input("Введіть ім'я:"),age=int(input("Введіть вік:")),power=int(input("Введіть силу:")),prizvanie=input("Введіть професію(лучник\мечник\маг):"))
aaa.show()
boec.show()
def bib():
    fi=input("Готові до битви?(так\ні)")
    if (fi=="так"):
        if(aaa.prizvanie=="маг"): #Якщо маг то сильніший
            aaa.power=aaa.power+xiti
        if(boec.prizvanie=="маг"):
            boec.power=boec.power+xxitu
        if(aaa.prizvanie=="лучник"):
            aaa.power=aaa.power+xriti #лучник тоже
        if(boec.prizvanie=="лучник"):
            boec.power=boec.power+xxritu
        if(aaa.power>boec.power):
            print(aaa.name,"переміг")
        if(aaa.power<boec.power):
            print(boec.name,"переміг")
bib()
print('сила:',aaa.power)
print('сила:',boec.power)