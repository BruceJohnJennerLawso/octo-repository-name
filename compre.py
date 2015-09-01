## compre.py ###################################################################
## list comprehension ##########################################################
################################################################################



def createList(*values):
	"""return a list created from values passed to this function"""
	output = [];
	for i in values:
		output.extend([i])
	return output;
def incrementWhatever(value):
	try:
		output = value + 1;
		return output;
	except TypeError:
		output = value + "+1";
		return output;

def main():
	list = createList(1, "fooo", 2, "bar", 2.020202020202)
	print list;
	newlist = [incrementWhatever(foo) for foo in list]
	print newlist
	return;



if (__name__ == "__main__"):
	main();
