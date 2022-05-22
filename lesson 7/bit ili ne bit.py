import random

class Human:
    def __init__(self,name = "Human",job = None,home = None,car = None):
        self.name=name
        self.money = 100
        self.gladness = 50
        self.seitie = 50
        self.job = job
        self.home = home
        self.car = car

    def GetHome(self):
        self.home = Home(Homes)

    def GetCar(self):
        self.car=Auto(brands_of_car)
    def GetJob(self):
        self.job=Job(Job_list)
    def eat(self):
        if self.home.food<=0:
            self.shoping("food")
        else:
            if self.seitie>=100:
                self.seitie=100
            self.seitie+=5
            self.home.food -= 5
    def home(self):
        pass
    def job(self):
        self.money +=self.job.salary
        self.gladness-=self.job.gladness_less
        self.seitie-=4
    def shopping(self,manage):
        if manage=="food":
            print("i bought food")
            self.money-=50
            self.home.food+=30

    def chill(self):
        self.gladness+=10
        self.home.mess+=5
    def cleanhome(self):
        self.gladness-5
        self.home.mess=0
    def daysIndex(self,day):
        day=f"Today the {day} of {self.name}`s life"
        print(f"{day:=^50}")

        human_indexes=self.name+"`s indexes"
        print(f"{human_indexes:=^50}","\n")
        print(f"Money - {self.money}","\n")
        print(f"Gladness - {self.gladness}","\n")
        print(f"Saiety - {self.seitie}","\n")
        home_indexes="Home indexes"
        print(f"{home_indexes:=^50}","\n")
        print(f"Food - {self.home.food}","\n")
        print(f"Gladness - {self.home.mess}","\n")
    def IsAlive(self):
        if self.gladness<=0:
            print("Depression...")
            return False
        if self.seitie<=0:
            print("Golod...")
            return False
        if self.money< -500:
            print("Bankrupt...")
            return False

    def Live(self,day):
        if self.IsAlive==False:
            return False
        if self.home is None:
            print("You are bomj")
            self.GetHome()
            print(f"I get a home {self.home}, it`s{self.home.type}")
        if self.car is None:
            print("Buy a car, you must be on ponti")
            self.GetCar()
            print(f"I get a car {self.car.brand}, it`s {self.car.color}")
        if self.job is None:
            print("You need find a job if u don`t want to be a bomj!")
            self.GetJob()
            print(f"I get a job {self.job}, with salary {self.job.salary}")
        self.daysIndex(day)
        dice=random.randint(1,3)
class Auto:
    def __init__(self,brand_list):
        self.brand=random.choice(list(brand_list))
        self.color=brand_list[self.brand]["color"]
class Home:
    def __init__(self,house_list):
        self.brand=random.choice(list(house_list))
        self.color=house_list[self.brand]["type"]
        self.food=0
        self.mess=0
class Job:
    def __init__(self,job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness=job_list[self.job]["gladness_less"]
brands_of_car={
    "Ferrari":{"color:yellow"},
    "BMW":{"color:black"},
    "Lada":{"color:red"},
    "Mercedes":{"color:blue"},
    "Volvo":{"color:greeen"}
}
Job_list={
    "Python developer":{"salary":40,"gladness_less":3},
    "JavaScript developer":{"salary":30,"gladness_less":5},
    "Teacher":{"salary":22,"gladness_less":11},
    "Youtuber":{"salary":34,"gladness_less":2}
}
Homes={
    "Big_house":{"type:Big"},
    "Kvartira":{"type:Kvartira"},
    "Dacha":{"type:za_mistom"},
    "Small_house":{"type:Small"},
    "Hom":{"type:normal"}
}
