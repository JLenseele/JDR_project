class Menu(object):

	def __init__(self):
		self.choice = None

	@staticmethod
	def presentation():
		print("=========================================\n"
              "|||||||||||  QUICK ADVENTURE  |||||||||||\n"
              "=========================================\n")
	
	@staticmethod
	def main_menu():
		menu_options = {
			1: 'Créer un nouvel aventurier',
			2: 'Selectionner un aventurier',
			3: 'Quitter'
		}
		for key in menu_options.keys():
			print(' ',key, '- ',menu_options[key])
		choice = int(input(''))
		return choice