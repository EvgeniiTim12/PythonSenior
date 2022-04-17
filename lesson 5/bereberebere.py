#що більше
def f(x,y):
    if (x>y):
        print("x>y")
    else:
        print("x<y")
    

result = f(float(input('Введи число:')),float(input('Введи число:')))
print(result)
#рахує речення
def a (f):
    return len(f)
resule=a(input("Введіть речення:"))
print(resule)

#середнє арифметичне
def bb(a,b,c):
    return (a+b+c)/3
resulee=bb(float(input("Введіть число:")),float(input("Введіть число:")),float(input("Введіть число:")))
print(resulee)
#місяць за номером
def abb(a):
    if a == 1:
        print('Січень')
    elif a == 2:
        print('Лютий')
    elif a == 3:
        print('Березень')
    elif a == 4:
        print('Квітень')
    elif a == 5:
        print('Травень')
    elif a == 6:
        print('Червень')
    elif a == 7:
        print('Липень')
    elif a == 8:
        print('Серпень')
    elif a == 9:
        print('Вересень')
    elif a == 10:
        print('Жовтень')
    elif a == 11:
        print('Листопад')
    elif a == 12:
        print('Грудень')
micac=abb(int(input('Введіть номер місяця: ')))


    
