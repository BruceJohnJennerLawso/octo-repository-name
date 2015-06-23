## menu.py #####################################################################
## menu building blocks ########################################################
## like Cmd++ but infinitely easier and better #################################
################################################################################



def printMenuHeader(style_char, menu_name):
	print ((2*style_char) + (menu_name)+ (2*style_char));
	return

class dynMenu:
	def __init__(self, menu_name, menu_id):
		self.menuName = menu_name;
		self.menuId = menu_id;
		
	def Menu(last_input):
		
