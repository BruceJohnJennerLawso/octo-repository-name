## menu.py #####################################################################
## cmd-- in a way better language ##############################################
################################################################################


def caseInsensitiveMatch(str1, str2):
	if(str1.lower() == str2.lower()):
		return True;
	else:
		return False;

class menuAction:
	
	def __init__(self, stuff):
		
		## something to the effect of storing a function pointer or whatever
		
		return

class dynMenu:
	
	def __init__(self, name, access):
		self.Access = access;
		## a string handle, ie the thing that the user types into the command
		## prompt to go to that menu
		self.nameMenu(name);
		## just something to id the object by
		self.linksUp = [];
		self.linksDown = [];
		return
		
		
	def Menu(self, lastInput):
		while (True):
		## a little bit ugly, but when its all said & done, it works
			i = "not q"
			self.menuTitle();
			i = raw_input("#: ");
			## request input from the user, and lets get started...
			if((i == "q")or(i == "Q")):
				return "q";
			elif((i == "h")or(i == "H")):
				self.Help();
			elif(caseInsensitiveMatch(i, "ls") == True):
				## some sort of if statement here depending on whether there
				## actually is anything above
				print "\n"
				#for up in self.linksUp:
				#	print ("%s: %s" % (up.Name, up.Access));
				self.printUpLinks(0);
				print "%s: %s" % (self.Name, self.Access);
				##for down in self.linksDown:
				##	print "%s: %s" % (down.Name, down.Access);
				self.printDownLinks(0);
				
					
				## got an idea for a sort of nested thing, like
				## ->
				##   ->
				##   ->
			else:
				foundHit = False;
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
				if(foundHit == False):
					print "%s not found, please try again" % i;		
		
	def Help(self):
		print "Help placeholder here...";
		return
		
		
		
		
		
	def nameMenu(self, newName):
		self.Name = newName;
		## assign some new name to the object so we can test things
		return
	
	def menuTitle(self):
		print "\n==" + self.Name + "==";
		return
		
	def linkUpTo(self, target):
		self.linksUp.append(target);
		return
		
	def linkDownTo(self, target):
		self.linksDown.append(target);
		return		
		
	def attachSubMenu(self, target):
		self.linkDownTo(target);
		target.linkUpTo(self);
		return
		
	def attachParentMenu(self, target):
		self.linkUpTo(target);
		target.linkDownTo(self);
		return
	
	def goAbove(self, scope):
		if(len(self.linksUp) > 0):	
			for up in self.linksUp:
				##print "continuing up scope tree with scope %i" % scope;
				up.goAbove(scope + 1);
		else:
			##print "Reached top of scope tree"
			self.printTopLinks(scope);
		return
	
	def getUpLink(self, scope):
		upList = [];
		
		for up in self.linksUp:
			upList.append((scope*"  ") + "->%s: %s" % (up.Name, up.Access))
			if(len(up.linksUp) > 0):
				aboveList = up.getUpLink(scope+1);
				for cy in range(0, len(aboveList)):
					upList.insert(0, aboveList[cy]);
				##upList.insert(0, up.getUpLink(scope+1));
			
		return upList;

	
	def printUpLinks(self, scope):
		##for up in self.linksUp:
			##self.goAbove(0);	
		output = self.getUpLink(scope);
		for cy in range(1, len(output)):
			print output[cy];
		return
			
	
	def printDownLinks(self, scope):
		for down in self.linksDown:
			print (scope*"  ") + "->%s: %s" % (down.Name, down.Access);
			down.printDownLinks(scope + 1);
		return
		
	def printTopLinks(self, scope):
		if(scope > 0):
			for down in self.linksDown:
				print (scope*"  ") + "->%s: %s" % (down.Name, down.Access);
				down.printDownLinks(scope - 1);
		return
		
			
	
def main():
	mainMenu = dynMenu("Main Menu", "m");
	chain = dynMenu("Intermediate Menu", "i");
	sub1 = dynMenu("Menu One", "one");
	sub2 = dynMenu("Menu Two", "two");
	sub3 = dynMenu("Menu Three", "three");
	mainMenu.attachSubMenu(chain);
	chain.attachSubMenu(sub1);
	chain.attachSubMenu(sub2);	
	chain.attachSubMenu(sub3);
	sub3.attachParentMenu(mainMenu);
	mainMenu.Menu("not q");
	
	return
	
main();
		
