import abc

# task 1 
class Warrior:
	def __init__(self, damage: int, health: int, name: str) -> None:
		self.damage = damage
		self.health = health
		self.name = name

	def change_damage(self, new_damage) -> None:
		self.damage = new_damage

	def change_health(self, new_health) -> None:
		self.health = new_health

	def change_name(self, new_name) -> None:
		self.name = new_name

artes = Warrior(0, 0, '')
artes.change_damage(10)
artes.change_health(100)
artes.change_name('Arthes')


# task 2
class RailWayStation:
	def __init__(self) -> None:
		pass

class Employee(abc.ABC):
	def __init__(self) -> None:	
		pass

class Cashier(Employee):
	def __init__(self, railway: RailWayStation) -> None:
		super().__init__()
		self.railway = railway

	def sell_ticket(self):
		print('ticket sold')


# task 3
class Person(abc.ABC):
	@abc.abstractclassmethod
	def attack(self):
		pass

class Warrior(Person):
	def attack(self) -> None:
		super().attack()
		pass
	
class Archer:
	def attack(self) -> None:
		super().attack()
		pass

class Arena:
	def __init__(self, w1, w2) -> None:
		self.w1 = w1
		self.w2 = w2
	def battle(self) -> None:
		if isinstance(self.w1, Warrior) and isinstance(self.w2, Warrior):
			pass
		elif isinstance(self.w1, Warrior) and isinstance(self.w2, Archer):
			pass
		elif isinstance(self.w1, Archer) and isinstance(self.w2, Archer):
			pass


# task 4
class Computer(abc.ABC):
	def __init__(self) -> None:	
		pass

class Phone(Computer):
	def __init__(self) -> None:
		super().__init__()

class SmartPhone(Phone):
	def __init__(self) -> None:
		super().__init__()

class Samsung(SmartPhone):
	def __init__(self) -> None:
		super().__init__()


# task 5
class User:
	def __init__(self) -> None:
		pass

class DataBase:
	def __init__(self, user_list) -> None:
		self.user_list = user_list

	def save_user_to_db(self, user: User):
		self.user_list.append(user)


# task 6
class Permission:
	def __init__(self, type) -> None:
		self.type = type

	def get_type(self) -> None:
		return self.type

class User:
	def __init__(self, permission_type: Permission) -> None:
		self.permission_type = permission_type.get_type()

	def get_permission(self):
		if self.permission_type == 'staff':
			pass
		elif self.permission_type == 'simple':
			pass
		elif self.permission_type == 'admin':
			pass