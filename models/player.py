class Player:

	def __init__(self, name, race, life, att, defense, dex, intel, cha, mana):
		self.name = name
		self.race = race
		self.life_max = life
		self.life_point = life
		self.att = att
		self.defense = defense
		self.dex = dex
		self.intel = intel
		self.cha = cha
		self.mana = mana
		self.lvl = 1
		self.exp = 0
		self.weapon = None
		self.spell = []
		self.inventory = []

	def __str__(self):
		return print(
			'Nom: {}\n'
			'Race: {}\n'
			'Lvl: {}\n'
			'Exp: {}\n'
			'Vie: {}/{}\n'
			'Att: {}\n'
			'Def: {}%\n'
			'Int: {}\n'
			'Cha: {}\n'
			'Dex: {}\n'
			'Mana: {}\n'

			.format(
				self.name,
				self.race,
				self.lvl,
				self.exp,
				self.life_point,
				self.life_max,
				self.att,
				self.defense,
				self.intel,
				self.cha,
				self.dex,
				self.mana
			))
