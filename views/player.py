class PlayerViews(object):

	def __init__(self):
		return

	@staticmethod
	def player_name():
		return input("Quel est votre nom ? :")

	@staticmethod
	def player_race():
		print("Quel est votre race ?")
		race_options = {
			1: 'Humain',
			2: 'Elfe',
			3: 'Nain'
		}
		for key in race_options.keys():
			print(' ', key, '- ', race_options[key])
		choice = int(input(''))
		return race_options[choice]
		