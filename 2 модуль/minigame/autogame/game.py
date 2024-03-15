from classes.warriors import Knight, Archer, Paladin
from classes.weapons import Sword, Bow
from random import randint


def character_choice():
	warriors = ['р', 'п', 'л']
	weapons = ['м', 'л']
	return {'warrior1': warriors[randint(0, len(warriors) - 1)], 'name1': 1, 'warrior2': warriors[randint(0, len(warriors) - 1)], 'name2': 2, 'weapon1': weapons[randint(0, len(weapons) - 1)], 'weapon2': weapons[randint(0, len(weapons) - 1)]}


def weapon_create(weapon_type):
	if weapon_type == 'м':
			return Sword()
	elif weapon_type == 'л':
			return Bow()


def warrior_create(warrior_type, name, weapon):
	if warrior_type == 'р':
		return Knight(name, weapon)
	elif warrior_type == 'л':
		return Archer(name, weapon)
	elif warrior_type == 'п':
		return Paladin(name, weapon)


def character_create():
	info = character_choice()
	if not info:
		return
	weapon1 = weapon_create(info['weapon1'])
	weapon2 = weapon_create(info['weapon2'])
	warrior_type1, warrior_type2 = info['warrior1'], info['warrior2']
	warrior1 = warrior_create(warrior_type1, info['name1'], weapon1)
	warrior2 = warrior_create(warrior_type2, info['name2'], weapon2)
	return (warrior1, warrior2)


def move(attacking_warrior, defense_warrior):
	attack_types = ['л', 'т']
	attack = attack_types[randint(0, len(attack_types)-1)]
	if attack == 'л':
		dmg = attacking_warrior.attack('light')['dmg']
		defense_warrior.stamina -= dmg
	elif attack == 'т':
		dmg = attacking_warrior.attack('heavy')['dmg']
		defense_warrior.stamina -= dmg

def autogame():
	wins = []
	for _ in range(25):
		warrior1, warrior2 = character_create()
		cnt = 1
		while warrior1.stamina > 0 and warrior2.stamina > 0:
			if cnt % 2 == 0:
				move(warrior1, warrior2)
			else:
				move(warrior2, warrior1)
			cnt += 1
		if warrior1.stamina <= 0 and warrior1.stamina < warrior2.stamina:
			print(f'{warrior2.name} выиграл!')
			wins.append(2)
		else:
			print(f'{warrior1.name} выиграл!')
			wins.append(1)
		print('--------------------------')
	return wins