class Hero :
    def __init__(self,name):
        self.name=name

class Vibor:
    def __init__(self,mast):
        self.mast = mast
        self.hero = []
    def add_hero(self,human):
        self.hero.append(human)
    def print_hero(self):
        if self.hero != []:
            print(f"Імена {self.mast} героїв:")
            for i in self.hero:
                print(i.name)
        else:
            print(f"Немає персонажів {self.mast}")
    
first=Hero("Чаклз")
second=Hero("Петро")
sescond=Hero("Олег")

bb= Vibor("Злий")
bb.add_hero(first)
bb.add_hero(second)
bb.print_hero()

bb= Vibor("Добрий")
bb.add_hero(sescond)
bb.print_hero()

    