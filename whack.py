## whackpy #####################################################################
## random crap written to do stuff #############################################
################################################################################


class dataBin:
	def __init__(self):
		self.Values = [];
		self.subBins = [];
		return
		
	def insertValue(self, val):
		self.Values.append(val);
		return
		
	def getValue(self, index):
		return self.Values[i];
		
	def printValues(self):
		print "\n--Top Object--"
		for i in range(0, len(self.Values)):
			print " %f," % (self.Values[i]);
		if(len(self.subBins) > 0):
			print "\n--Sub Objects--"
			for j in range(0, len(self.subBins)):
				if(len(self.subBins[j].Values) > 0):
					## make a double check that the sub bin isnt empty before we
					## print
					for k in range (0, len(self.subBins[j].Values)):
						print " %f," % (self.subBins[j].Values[k]);		
		return
	def Zeroes(self):		
		for i in range(0, len(self.Values)):
			i = 0;
			
	def createSubBin(self):
		nuRef = dataBin();
		cy = 10
		while (cy >= 1):
			nuRef.insertValue(rand(0, 10));
			cy -= 1;
		# no its NI NI NI!
		self.subBins.append(nuRef);
		nuRef.Zeroes();
		
class vector_III:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
		return
	
	def getVec(self):
		output = "(%f, %f, %f)\n" % (self.x, self.y, self.z)
		return output;
	
	def printVec(self): 
		print self.getVec();
		return
		
	def Plus(self, add):
		self.x += add.x
		self.y += add.y
		self.z += add.z
		return
		
	def Minus(self, sub):
		self.x -= sub.x
		self.y -= sub.y
		self.z -= sub.z
		return	
		
	def Dot(self, vec):
		output = ((self.x*vec.x)+(self.y*vec.y)+(self.z*vec.z));
		return output;
		
	def This(self):
		return self;
		# always unto thyself return?


def findPi(n): 
	prod = 1.0
	radic = 0.0
 
	for i in range(int(n)):
		radic = sqrt(2.0 + radic)
		prod *= 0.5*radic
		print 2.0/prod
	return
