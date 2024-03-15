import matplotlib.pyplot as plt
from game.utils import character_create, move
from autogame.game import autogame


def game():
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
	else:
		print(f'{warrior1.name} выиграл!')


def main():
	mode = input('Игру можно запустить в режиме одного матча с выбором персонажей и оружия (1) или в режиме случайного подбора с выводом статистики через matplotlib (2). Как вы хотите запустить игру (1/2)?: ').strip()
	if mode == '1':
		game()
	elif mode == '2':
		statistics = autogame()
		print(f"Первый воин выиграл: {statistics.count(1)} раз, Второй воин выиграл: {statistics.count(2)} раз")
		fig = plt.figure(figsize=(2, 5))
		ax = fig.add_subplot()
		y = statistics
		ax.hist(y)
		ax.grid()
		plt.show()

			
main()
