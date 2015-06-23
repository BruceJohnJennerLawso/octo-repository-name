## menu.py #####################################################################
## menu building blocks ########################################################
## like Cmd++ but infinitely easier and better #################################
################################################################################

def caseInsensitivematch(value1, value2):
	return False;

def printMenuHeader(style_char, menu_name):
	print ((2*style_char) + (menu_name)+ (2*style_char));
	return

class dynMenu:
	def __init__(self, menu_name, menu_id):
		self.menuName = menu_name;
		self.menuId = menu_id;
		menuList.append(self);
		
	menuList = [];	
		
	def Menu(last_input, prompt):
		if((last_input == "q")or(last_input == "Q")):
			return "q";
		else:
			i = "notqorQ";
			while((i != "q")and(i !="Q")):
				i = raw_input(prompt);
				
				for cy in range(0, len(menuList)):
					if(menuList[cy].matchId(i) == True):
						
					
					
	def matchId(i):
		return caseInsensitivematch(self.menuId, i);
			
					
					
					
					
