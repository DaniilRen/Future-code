import abc

class Warrior(abc.ABC):
	@abc.abstractclassmethod
	def __init__(self, name, weapon, warrior_type, stamina) -> None:
		self.stamina = stamina
		self.type = warrior_type
		self.name = name
		self.weapon = weapon

	@abc.abstractclassmethod
	def attack(self, attack_type):
		pass


class Knight(Warrior):
	def __init__(self, name, weapon) -> None:
		super().__init__(name, weapon, "Knight", 100)
		self.light_attack_bonus = 3
		self.heavy_attack_bonus = 3

	def attack(self, attack_type):
		if attack_type == 'light':
			res = self.weapon.light_attack(self)
		elif attack_type == 'heavy':
			res = self.weapon.heavy_attack(self)
		return res

class Archer(Warrior):
	def __init__(self, name, weapon) -> None:
		super().__init__(name, weapon, "Archer", 110)
		self.light_attack_bonus = 5
		self.heavy_attack_bonus = 1

	def attack(self, attack_type):
		if attack_type == 'light':
			res = self.weapon.light_attack(self)
		elif attack_type == 'heavy':
			res = self.weapon.heavy_attack(self)
		return res


class Paladin(Warrior):
	def __init__(self, name, weapon) -> None:
		super().__init__(name, weapon, "Knight", 85)
		self.light_attack_bonus = 0
		self.heavy_attack_bonus = 6

	def attack(self, attack_type):
		if attack_type == 'light':
			res = self.weapon.light_attack(self)
		elif attack_type == 'heavy':
			res = self.weapon.heavy_attack(self)
		return res