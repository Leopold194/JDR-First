
class Creature:

	def __init__(self, kind, strength, health, name=None, score=None):
		self.kind = kind
		self.name = name
		self.strength = strength
		self.hp = health
		self.score = score