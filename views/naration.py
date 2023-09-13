from randomizer_data.random_data import rnd_story


class Naration:

	@staticmethod
	def begin(player):

		place = rnd_story.rnd_place()
		mob = rnd_story.rnd_mob()
		attitude = rnd_story.rnd_attitude()
		print(
			'Vous débutez votre aventure dans {}.\n'
			'Vous faites face à {}\n'
			'{}'
			.format(place, mob, attitude)
			)

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
		return choice

	@staticmethod
	def reaction(player):
		pass

	@staticmethod
	def situation(player):
		pass