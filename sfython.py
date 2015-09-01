## sfml python #################################################################
## best of both worlds #########################################################
################################################################################
import sfml as sf


def init():
	## create the main window
	try:
		print "Running init";
		## load a sprite to display
		##texture = sf.Texture.from_file("cute_image.png")
		##sprite = sf.Sprite(texture)

		## create some graphical text to display
		##font = sf.Font.from_file("arial.ttf")
		##text = sf.Text("Hello SFML", font, 50)

		## load music to play
		##music = sf.Music.from_file("nice_music.ogg")
	except IOError: exit(1)

def main():

	# play the music
	#music.play()
	window = sf.RenderWindow(sf.VideoMode(800, 600), "sfython");
	# start the game loop
	while window.is_open:
		## process events
		for event in window.events:
			## close window: exit
			if type(event) is sf.CloseEvent:
				window.close()

		window.clear() 
		## clear screen
		
		##window.draw(sprite) # draw the sprite
		##window.draw(text) # draw the string
		window.display() 
		## update the window

if (__name__ == "__main__"):
	init();
	main();
