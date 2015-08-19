## valref.py ###################################################################
## by value, by reference, neither... ##########################################
################################################################################


def changeMe(value):
	if(value == True):
		value = False;
	else:
		value = True;
	return;

def main():
	var = True
	print "value of var is ", var	
	changeMe(var);
	print "value of var is ", var
	
	return;



main();
