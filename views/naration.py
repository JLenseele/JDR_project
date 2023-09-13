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
	def choice():
		pass

	@staticmethod
	def reaction():
		pass

	@staticmethod
	def situation():
		pass