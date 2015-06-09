class HogwartsHouse(object):
	""" This class contains basic properties for Hogwarts Houses"""
	def __init__(self, name, color):
		self.name = name
		self.color = color

	def houseName(self):
		return self.name

	def houseColor(self):
		raise self.color

	def __str__(self):
		return self.houseName()

GRYFFINDOR = HogwartsHouse('Gryffindor', 'red')
SLYTHERINE = HogwartsHouse('Slytherine', 'green')
RAVENCLAW = HogwartsHouse('Ravenclaw', 'blue')
HUFFLEPUFF = HogwartsHouse('Hufflepuff', 'yellow')
