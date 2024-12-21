print("OE#1")

class Hero:
    def __init__(self, name, role, dmg_type, health, auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg

    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power."

hero_mm1 = Hero("Lesley", "marksman", "attack damage", "2490", "115")
hero_fighter1 = Hero("Zilong", "fighter", "attack damage", "2689", "123")
hero_mg1 = Hero("Kagura", "mage", "magic damage", "2496", "130")
hero_ass1 = Hero("Hayabusa", "assassin", "attack damage", "2429", "117")
hero_sup1 = Hero("Diggie", "support", "magic damage", "2468", "115")

print(f'''
{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.dmg_type}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attack damage
{hero_mm1.describe()}

{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.dmg_type}
{hero_fighter1.health} HP
{hero_fighter1.auto_atk_dmg} basic attack damage
{hero_fighter1.describe()}

{hero_mg1.name}
{hero_mg1.role}
{hero_mg1.dmg_type}
{hero_mg1.health} HP
{hero_mg1.auto_atk_dmg} basic attack damage
{hero_mg1.describe()}

{hero_ass1.name}
{hero_ass1.role}
{hero_ass1.dmg_type}
{hero_ass1.health} HP
{hero_ass1.auto_atk_dmg} basic attack damage
{hero_ass1.describe()}

{hero_sup1.name}
{hero_sup1.role}
{hero_sup1.dmg_type}
{hero_sup1.health} HP
{hero_sup1.auto_atk_dmg} basic attack damage
{hero_sup1.describe()}
''')