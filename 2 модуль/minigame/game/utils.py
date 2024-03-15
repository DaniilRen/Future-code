from classes.warriors import Knight, Archer, Paladin
from classes.weapons import Sword, Bow


def intro():
	print("Привет! Это простенькая игра-симуляция сражения")
	print("-------------->")
	print("Правила довольно простые: всего есть 3 типа бойцов: Рыцарь, Лучник и Паладин. У каждого типа бойца есть различные прибавки к каждому виду атаки (легкая или тяжелая).")
	print("Существует 2 вида оружия: лук и меч; они имеют различные характеристики урона и поглощения выносливости бойца, которые определяются в случайном порядке для каждого бойца")
	print("В начале игры тебе необходимо выбрать тип обоих бойцов и их оружие.\nЗатем можно будет начать игру. ")
	print("Побеждает тот боец, который сохранил выносливость больше 0. В случае если оба выносливость обоих бойцов будет меньше нуля, то выигрывает тот, у кого выносливость оказалась больше")
	print("-------------->")


def is_valid(type, value):
	if type == 'weapon':
		if value in ('л', 'м'):
			return True
	elif type == 'warrior':
		if value in ('п', 'р', 'л'):
			return True
	return False


def character_choice():
	intro()
	info = {'warrior1': '', 'name1': '', 'warrior2': '', 'name2': '', 'weapon1': '', 'weapon2': ''}

	war1 = input("Выберите класс первого воина (рыцарь=Р, лучник=Л паладин=П): ").strip().lower()
	if not is_valid('warrior', war1):
		print("Вы выбрали класс неверно!")
		return False
	info['warrior1'] = war1
	info['name1'] = input("Дайте имя воину: ").strip()

	wep1 = input("Выберите тип оружия воина (меч=М, лук=Л): ").strip().lower()
	if not is_valid('weapon', wep1):
		print("Вы выбрали тип неверно!")
		return False
	info['weapon1'] = wep1

	war2 = input("Выберите класс второго воина (рыцарь=Р, лучник=Л паладин=П): ").strip().lower()
	if not is_valid('warrior', war2):
		print("Вы выбрали класс неверно!")
		return False
	info['warrior2'] = war2
	info['name2'] = input("Дайте имя воину: ").strip()

	wep2 = input("Выберите тип оружия воина (меч=М, лук=Л): ").strip().lower()
	if not is_valid('weapon', wep2):
		print("Вы выбрали тип неверно!")
		return False
	info['weapon2'] = wep2

	return info


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
	print('<---------------->')
	print(f"Ход {attacking_warrior.name} (осталось {attacking_warrior.stamina} выносливости).")
	attack_type = input("Легкая атака (л) / Тяжелая атака (т) / пропустить (п)?: ").lower().strip()
	if attack_type == 'п':
		print(f'{attacking_warrior.name} пропустил ход')
	elif attack_type == 'л':
		dmg = attacking_warrior.attack('light')['dmg']
		defense_warrior.stamina -= dmg
		print(f'Выносливость {attacking_warrior.name} = {attacking_warrior.stamina}')
		print(f'Выносливость {defense_warrior.name} = {defense_warrior.stamina}')
	elif attack_type == 'т':
		dmg = attacking_warrior.attack('heavy')['dmg']
		defense_warrior.stamina -= dmg
		print(f'Выносливость {attacking_warrior.name} = {attacking_warrior.stamina}')
		print(f'Выносливость {defense_warrior.name} = {defense_warrior.stamina}')