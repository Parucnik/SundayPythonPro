class Mage:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana
    
    def cast(self, spell_name):
        print(self.name, 'кастует', spell_name)

class Healer(Mage):
    def heal_myself(self):
        self.hp+= 20
        self.mana -=5
        self.cast('Лечение самого себя')

class WarMage(Mage):
    def __init__(self, name, hp, mana, armor):
        super().__init__(name, hp, mana)
        self.armor = armor
    
    def fireball(self, enemy):
        enemy.hp -= 50
        self.mana -= 10
        self.cast('файрболл')
        
        
h1 = Healer('Вася', 60, 20)
h1.heal_myself()

w1 = WarMage('Боря', 40, 20, 10)
w1.fireball(h1)
