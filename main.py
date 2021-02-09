from window import Window
from cli import CLI

if __name__ == '__main__':
	def makeWindow():
		main_win = Window(500, 300, "Height Calculator",
						  "Enter your height:", True)
		main_win.run()
	cli = CLI(makeWindow)
	cli.startMsg()
