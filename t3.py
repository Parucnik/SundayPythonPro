class Mage():
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

    def cast(self, cast_name):
        print(self.name, f'кастует заклинание {cast_name}...')
# 1-й Вариант наследования (только новые методы)
class Healer(Mage):
    def heal(self, aim):
        self.cast('лечение')
        aim.hp += 20
# 2-й вариант наследования     
class WarMage(Mage):
    def __init__(self, name, hp, mana, armor):
        super().__init__(name, hp, mana)
        self.armor = armor

