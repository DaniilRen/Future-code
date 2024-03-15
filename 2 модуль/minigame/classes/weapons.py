import random
import abc

class Weapon(abc.ABC):
	@abc.abstractclassmethod
	def __init__(self, type) -> None:
		self.type = type
	
	@abc.abstractclassmethod
	def light_attack():
		pass
	
	@abc.abstractclassmethod
	def heavy_attack():
		pass


class Bow(Weapon):
	def __init__(self) -> None:
		super().__init__("Bow")
		self.light_attack_damage = random.randint(5, 10)
		self.heavy_attack_damage = random.randint(10, 15)

	def light_attack(self, warrior):
		print(f'{warrior.name} совершил выстрел из лука!')
		info = {'dmg': self.light_attack_damage+warrior.light_attack_bonus,
			'cost': 3}
		warrior.stamina -= info['cost']
		return info
	
	def heavy_attack(self, warrior):
		print(f'{warrior.name} совершил тяжелый выстрел из лука!')
		info = {'dmg': self.heavy_attack_damage+warrior.heavy_attack_bonus,
			'cost': 5}
		warrior.stamina -= info['cost']
		return info
	

class Sword(Weapon):
	def __init__(self) -> None:
		super().__init__("Sword")
		self.light_attack_damage = random.randint(4, 6)
		self.heavy_attack_damage = random.randint(12, 19)

	def light_attack(self, warrior):
		print(f'{warrior.name} ударил врага мечом!')
		info = {'dmg': self.light_attack_damage+warrior.light_attack_bonus,
			'cost': 2}
		warrior.stamina -= info['cost']
		return info
	
	def heavy_attack(self, warrior):
		print(f'{warrior.name} совершил тяжелый удар мечом!')
		info = {'dmg': self.heavy_attack_damage+warrior.heavy_attack_bonus,
			'cost': 4}
		warrior.stamina -= info['cost']
		return info
