## work in understanding #######################################################
## Python ######################################################################
################################################################################

class linkBlock:
	
	def __init__(self, name):
		
		
		##self.Name = name;
		self.nameSelf(name);
		## just something to id the object by
		
		self.Links = [];
		## a list of other objects assumed to be of this type that this object
		## is storing a name to
		
		## kinda like a pointer but less evil
		
	def nameSelf(self, newName):
		self.Name = newName;
		## assign some new name to the object so we can test things
		return
		
	def linkTo(self, target):
		self.Links.append(target);
		## append the name of the target object to the list that stores
		## references to other objects
		return
		
	def hitLinks(self):
		print "%s's links say:\n" % self.Name;
		for i in self.Links:
			##i.identifySelf();
			i.talkLinks();
		return
	
	def identifySelf(self):
		print ("Hi I am " + self.Name);
		return
		
	def talkLinks(self):
		self.identifySelf();
		self.hitLinks();
		## identify self, then prompt our subs to do the same, who then get
		## their subs to do likewise...
		
		## obviously not great when we have a circular reference setup, but what
		## can ya do
		return
		
	


def Main():
	main = linkBlock("Main");
	sub = linkBlock("Sub");
	main.linkTo(sub);
	sub.nameSelf("Subber");
	main.talkLinks();
	## such of glorious.
	## I would like my eulogy to be written in python please
	return


Main();
