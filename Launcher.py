# System call hack to display colors on Windows
from os import system as osystem
osystem("")

endColor = '\033[0m'
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

def menu():
	print(green,
	"""
	$$$$$$$$\ $$$$$$$$\ $$\       $$$$$$$$\ 
	\____$$  |$$  _____|$$ |      $$  _____|
	    $$  / $$ |      $$ |      $$ |      
	   $$  /  $$$$$\    $$ |      $$$$$\    
	  $$  /   $$  __|   $$ |      $$  __|   
	 $$  /    $$ |      $$ |      $$ |      
	$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$ |      
	\________|\________|\________|\__|      
	""")
	print('Calculateur des vos limites Zelf.')

	print(
	f"""
		{blue}1){endColor} Limite de dépense {bright_red}(Zelf non vérifié){endColor}
		{blue}2){endColor} Limite de rechargement {bright_red}(Zelf non vérifié){endColor}
		{blue}3){endColor} Limite de remboursement {bright_red}(Zelf non vérifié){endColor}

		{blue}0){endColor} Code source (Github)
	""")

	choice = int(input('Ton choix ? '))
	osystem('cls')
	if choice == 1:
		osystem('py SpendLimit/app.py')
		menu()

	elif choice == 2:
		osystem('py TopupLimit/app.py')
		menu()

	elif choice == 3:
		osystem('py RefundLimit/app.py')
		menu()

	elif choice == 0:
		osystem('start https://github.com/Poloin34/ZelfObtainLimitsData')
		print(yellow, 'Le lien a été ouvert dans ton navigateur', endColor)
		menu()

osystem('cls')
menu()
