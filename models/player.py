class Player:

	def __init__(self, name, race, life, att, defense, agility):
		self.name = name
		self.race = race
		self.max_life = life
		self.life = life
		self.att = att
		self.defense = defense
		self.agility = agility
		self.lvl = 1
		self.exp = 0

	def __str__(self):
		return print(
			'Nom: {}\n'
			'Race: {}\n'
			'Lvl: {}\n'
			'Vie: {}\n'
			'Att: {}\n'
			'Def: {}\n'
			'Agi: {}\n'
			.format(
				self.name,
				self.race,
				self.lvl,
				self.life,
				self.att,
				self.defense,
				self.agility
			))
