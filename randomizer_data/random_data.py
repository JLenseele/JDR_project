import random as rnd


class rnd_story:

	@staticmethod
	def rnd_place():
		place = [
			'une taverne',
			'une grotte',
			'un cimetière'
		]
		return rnd.choice(place)

	@staticmethod
	def rnd_mob():
		mob = [
			'un Lutin',
			'un Troll',
			'un Homme'
		]
		return rnd.choice(mob)

	@staticmethod
	def rnd_attitude():
		attitude = [
			"Il semble pacifiste",
			"Il semble agressif",
			"Il vous observe d'un air malicieux"
		]
		return rnd.choice(attitude)