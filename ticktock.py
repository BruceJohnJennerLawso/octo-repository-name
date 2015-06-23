## Tick Tock ###################################################################
## gotta check that HCM ########################################################
################################################################################

from Tkinter import *
import time

import datetime
	
		
		
def sendReminder(prompt):
	root = Tk()
	w = Label(root, text=prompt)
	w.pack()
	root.wm_attributes("-topmost", 1)	
	root.mainloop()
	return
		
def formatTime(h, m, s):
	output = "foo"
	## better not reach the end like this
	if(m <= 9):
		if(s <= 9):
			output = "Sending Reminder at %i:0%i:0%i" % (h, m, s);
		else:
			output = "Sending Reminder at %i:0%i:%i" % (h, m, s);			
	else:
		if(s <= 9):
			output = "Sending Reminder at %i:%i:0%i" % (h, m, s);
		else:
			output = "Sending Reminder at %i:%i:%i" % (h, m, s);
		
	return output;
	## that wasnt too bad
		

def weekDay():
	output = datetime.datetime.today().weekday();
	return output;
	## 0 to 7, 0 is monday I guess?
	
def Focus():
	root = Tk()
	root.wm_attributes("-topmost", 1)	
	root.after(1000, lambda: root.focus_force())
	root.mainloop()
	
def Startup(title, message):
	print ("==" + title + "==\n");
	print (message);
	return

def Main():
	Reminder();
	return

Main();
