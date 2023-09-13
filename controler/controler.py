from models.player import Player

from views.menu import Menu
from views.player import PlayerViews
from views.naration import Naration


class MainController(object):
	"""docstring for MainController"""
	def __init__(self):
		self.player = None
		self.menu = Menu()

	def run(self):
		menu_choice = self.menu.main_menu()
		if menu_choice == 1:
			self.create_player()
			Naration.begin(self.player)
			while True:
				Naration.choice()
				Naration.reaction()
				Naration.situation()

	def create_player(self):
		name = PlayerViews.player_name()
		race = PlayerViews.player_race()
		stats = self.define_stats(race)
		self.player = Player(name,
							 race,
							 stats[0],
							 stats[1],
							 stats[2],
							 stats[3])
		self.player.__str__()

	def define_stats(self, race):
		# Humain
		if race==1:
			stats = [12,4,4,3]
		# Elfe
		elif race==2:
			stats = [10,5,2,6]
		# Nain
		elif race==3:
			stats = [15,3,4,2]
		return stats
