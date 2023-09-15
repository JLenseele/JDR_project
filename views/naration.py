import time
import sys

from randomizer_data.random_data import rnd_story


class Naration:

	@staticmethod
	def begin():
		prologue = open("data/prologue/prologue1.txt", "r", encoding='UTF-8')
		return prologue

	@staticmethod
	def choice(player):
		choice_options = {
            1: 'Communiquer',
            2: 'Combattre',
            3: 'Fuir',
            4: 'Marchander',
            5: 'Looter'
        }
		for key in choice_options.keys():
			print(' ', key, '- ', choice_options[key])
		choice = int(input(''))
		return choice \

	@staticmethod
	def communication(player):
		pass

	@staticmethod
	def combat(player):
		pass

	@staticmethod
	def situation(player):
		pass

	@staticmethod
	def elnarator(texte):
		long = 0
		for sentence in texte:
			for c in sentence:
				if (long > 50 and c == ' ') or (c == '.'):
					c += '\n'
					long = 0
				sys.stdout.write(c)
				sys.stdout.flush()
				time.sleep(0.05)
				long += 1