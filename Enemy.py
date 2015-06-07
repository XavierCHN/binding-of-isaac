from pygame import *
from const import *
from math import *
from AStar import *
from random import randint

class Enemy:
	"""Enemy parent class"""

	isFlying = False
	dead = False
	path = []
	cx, cx = 0, 0
	health = 1
	weight = 1

	def hurt(self, ammount):
		if not self.dead:
			self.health -= ammount
			if self.health <= 0:
				self.die()

	def move(self):
		if not self.isFlying and len(self.path) != 0:
			# MOVE TO NEXT PATH

			dx, dy = self.x-self.path[0][0], self.y-self.path[0][1]

			if sqrt(dx**2+dy**2) < 0.15:
				self.path = self.path[1:]

		if len(self.path) > 0:
			dx, dy = self.path[0][0]-self.x, self.path[0][1]-self.y
		else:
			dx, dy = self.cx-self.x, self.cy-self.y

		something = sqrt(dx**2+dy**2)

		rx = dx/something
		ry = dy/something

		self.x += self.speed*rx
		self.y += self.speed*ry

	def pathFind(self, xy, nodes, paths):
		self.cx, self.cy = x, y = list(map(round,xy))

		if self.isFlying:
			return

		start, end = nodes[round(self.x)][round(self.y)], nodes[x][y]

		path = paths.search(start, end)
		if path is None:
			# There is no path found to the character

			print("HELP NO PATH!")
			print(self.x, self.y)
			self.path = []
		else:
			for i in range(len(path)):
				p = path[i]
				path[i] = (p.x, p.y)
			self.path = path[1:]
