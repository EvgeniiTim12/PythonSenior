import random

class Human:
    def __init__(self,name = "Human",job = None,home = None,car = None):
        self.name=name
        self.money = 100
        self.gledness = 50
        self.seitie = 50
        self.job = job
        self.home = home
        self.car = car

    def GetHome(self):
        pass
    def GetCar(self):
        pass
    def GetJob(self):
        pass
    def eat(self):
        pass
    def home(self):
        pass
    def job(self):
        pass
    def shopping(self,mange):
        pass
    def chill(self):
        pass
    def cleanhome(self):
        pass
    def daysIndex(self,day):
        pass
    def IsAlive(self):
        pass
    def Live(self):
        pass

class Auto:
    def __init__(self,brand_list):
        self.brand=random.choice(list(brand_list))
        self.color=brand_list[self.brand]["color"]
class Home:
    def __init__(self):
        self.food=0
        self.nest=0
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
    "Youtuber":{"salary":44,"gladness_less":2}
}
