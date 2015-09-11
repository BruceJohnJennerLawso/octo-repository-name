## menu.py #####################################################################
## cmd-- in a way better language ##############################################
################################################################################
import sys

def caseInsensitiveMatch(str1, str2):
	if(str1.lower() == str2.lower()):
		return True;
	else:
		return False;

def foo():
	print "foo";
	
def bar(*times):
	for n in times:
		print "bar"*n;

class menuFunction:
	def __init__(self, input_function, help_string, id_string):
		## something to the effect of storing a function pointer or whatever
		self.function = input_function;
		self.helpString = help_string
		self.idString = id_string
		return
	
	def getIdString(self):
		return self.idString
		
	def getHelpString(Self):
		return self.helpString	
	
	def execute(self):
		self.function()
		
		
class dynMenu:
	
	def __init__(self, name, access):
		self.Access = access;
		## a string handle, ie the thing that the user types into the command
		## prompt to go to that menu
		self.nameMenu(name);
		## just something to id the object by
		self.linksUp = [];
		self.linksDown = [];
		self.Functions = [];
		return
		
		
	def Menu(self, lastInput):
		self.menuTitle(True);
		while (True):
		## a little bit ugly, but when its all said & done, it works
			i = "not q"
			i = raw_input("#: ");
			## request input from the user, and lets get started...
			for cy in i.split(" "):
				print cy;
			if((i == "q")or(i == "Q")):
				return "q";
			elif((i == "h")or(i == "H")):
				self.Help();
			elif(caseInsensitiveMatch(i, "ls") == True):
				self.lsStructure(0);	
			elif (caseInsensitiveMatch(i.split(" ")[0], "cd")):
				i = i.split(" ")[1];
				for up in self.linksUp:
					if(caseInsensitiveMatch(up.Access, i) == True):
						if((up.Menu(i)) == "q"):
							return "q";
						else:
							foundHit = True;
							break;
				for down in self.linksDown:
					if(caseInsensitiveMatch(down.Access, i) == True):
						if((down.Menu(i)) == "q"):
							return "q";
						else:
							foundHit = True;
							break;			
			else:
				foundHit = False;
				for func in self.Functions:
					if(caseInsensitiveMatch(func.getIdString(), i)):
						foundHit = True
						func.execute()
				if(foundHit == False):
					print "%s not found, please try again" % i;		
		
	def Help(self):
		print "Help placeholder here...";
		return
		
		
		
		
		
	def nameMenu(self, newName):
		self.Name = newName;
		## assign some new name to the object so we can test things
		return
	
	def menuTitle(self, scrub):
		if(scrub == True):
			sys.stdout.write("\x1b[2J\x1b[H");
		print "\n==" + self.Name + "==";
		return
		
	# attach links above and below	
	def linkUpTo(self, target):
		self.linksUp.append(target);
		return
		
	def linkDownTo(self, target):
		self.linksDown.append(target);
		return		
	# attach a submenu and tell the submenu to link itself to you as well	
	def attachSubMenu(self, target):
		self.linkDownTo(target);
		target.linkUpTo(self);
		return
	# attach self below a parent menu
	
	def attachFunction(self, fx, help_string, id_string):
		self.Functions.insert(0, menuFunction(fx, help_string, id_string))
	
	def attachParentMenu(self, target):
		self.linkUpTo(target);
		target.linkDownTo(self);
		return

	
	def lsStructure(self, scope):
		print "\n"
		self.printUpLinks(scope+1);
		print "%s: %s" % (self.Name, self.Access);
		self.printDownLinks(scope+1);
		return;
	
	# list menus below the current menu
	def getDownLink(self, scope):
		output = [];
		for down in self.linksDown:
			output.append( (scope*"  ") + "%s: %s" % (down.Name, down.Access) );
			output.extend( down.getDownLink(scope+1) );
			
		return output;
	
	def printDownLinks(self, scope):
		output = []
		output = self.getDownLink(scope+1);
		for i in output:
			print i;
		return
		
	# list menus above the current menu	
	def getUpLink(self, scope):
		output = []
		for up in self.linksUp:
			output.append( (scope*"  ") + "%s: %s" % (up.Name, up.Access) );
			output.extend(up.getUpLink(scope + 1));
		return output;	
		
	def printUpLinks(self, scope):
		output = [];
		output = self.getUpLink(scope +1);
		for i in reversed(output):
			print i;
		return;
		
			
	
def main():
	
	mainMenu = dynMenu("Main Menu", "m");
	chain = dynMenu("Intermediate Menu", "i");
	sub1 = dynMenu("Menu One", "one");
	sub2 = dynMenu("Menu Two", "two");
	sub3 = dynMenu("Menu Three", "three");
	mainMenu.attachSubMenu(chain);
	chain.attachSubMenu(sub1);
	sub1.attachFunction(foo, "prints out foo to the console, very useful", "foo")
	sub1.attachFunction(bar, "prints out bar to the console n times, very useful", "foo")
	chain.attachSubMenu(sub2);	
	chain.attachSubMenu(sub3);
	sub3.attachParentMenu(mainMenu);
	mainMenu.Menu("not q");
	
	return
	
if (__name__ == "__main__"):	
	main();
		
