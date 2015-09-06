class Student():
	def __init__(self, name="you", magic=False, MIT=False, boxer=False, brave=False, cunning=False, witty=False, choice=None):
		self.name = name
		self.magic = magic
		self.MIT = MIT
		self.boxer = boxer
		self.brave = brave
		self.cunning = cunning
		self.witty = witty
		self.choice = choice

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name