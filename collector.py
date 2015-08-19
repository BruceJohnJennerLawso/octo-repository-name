## collector.py ################################################################
## collect arbitrary numbers of arguments as input to a function ###############
################################################################################


def printValues(*values):
	for i in values:
		print i, ", ",

def main():
	printValues(1, 2, 3, 4, 5, 6, "\n");
	printValues(6, 5, 4, 3, 2, 1, "foo", False);
	
	
	return;


main();
