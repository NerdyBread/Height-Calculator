from sys import exit


class CLI:
	def __init__(self, runMethod):
		self.runMethod = runMethod
		self.options = {"banner": self._banner,
						"run": self.runMethod,
						"quit": exit}
		self.prefix = "-"


	def startMsg(self):
		self._banner()
		self._showOptions()
		self._getCommand()

	def _banner(self):
		banner = '''
		|------------------|
		|   Height         |
		|     Calculator   |
		|------------------|
		'''
		print(banner)

	def _showOptions(self):
		print("\nCommands\n")
		for option in self.options.keys():
			print(f"{self.prefix}{option}")

	def _getCommand(self):
		while True:
			nextCommand = str(input(">> "))
			if nextCommand[1:] in self.options.keys():
				self.options[nextCommand[1:]]()
			else:
				print("Invalid command")


if __name__ == "__main__":
	cli = CLI(print) # Test run
	cli.startMsg()
