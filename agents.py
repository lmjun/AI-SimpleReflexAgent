# Lucas Junginger
# EECS 492 Homework 1

import world
from numpy.random import randint

class simple_reflex_agent:
	def __init__(self):
	# Agent has no state, so nothing to do here
		return		
	# Given a valid percept (a string), return a valid action (also as a string)
	def choose_action(self, percept):
		##### Implement this function #####
		if percept in ('start', 'move_succeeded'):
			return 'sense_water'
		if percept == 'needs_watering':
			return 'water'
		if percept in ('does_not_need_watering', 'watering_succeeded'):
			return 'sense_weed'
		if percept == 'needs_weeding':
			return 'weed'
		if percept in ('weeding_succeeded', 'does_not_need_weeding', 'hit_barrier'):
			return 'move'
	#################################


class state_reflex_agent:
	def __init__(self, worldstate):
		# This agent has a state, so wants to do BFS on the world
		# self.plan is a list of moves for the agent to take through the world
		# self.position is the position in the list
		self.plan, plan_exists = world.BFS(worldstate)
		if not plan_exists:
			raise RuntimeError('Plan does not exist or BFS iteration limit exceeded')
		self.position = 0

	# Given a valid percept (a string), return a valid action (also as a string)
	def choose_action(self, percept):
		#### Implement this function ####
		
		if percept == 'start':
			return 'sense_water'
		if percept == 'needs_watering':
			return 'water'
		if percept in ('does_not_need_watering', 'watering_succeeded'):
			return 'sense_weed'
		if percept == 'needs_weeding':
			return 'weed'
		if percept in ('weeding_succeeded', 'does_not_need_weeding'):
			return(self.plan[self.position])
		if percept == 'move_succeeded':
			self.position = self.position + 1
			return 'sense_water'

		#################################

class random_reflex_agent:
	def __init__(self):
		# Agent has no state, so nothing to do here
		return
	# Given a valid percept (a string), return a valid action (also as a string)
	def choose_action(self, percept):
		#### Implement this function ####
		dict = {0 : 'move_north', 1 : 'move_east', 2 : 'move_south', 3 : 'move_west'}
		
		if percept in ('start', 'move_succeeded'):
			return 'sense_water'
		if percept == 'needs_watering':
			return 'water'
		if percept in ('does_not_need_watering', 'watering_succeeded'):
			return 'sense_weed'
		if percept == 'needs_weeding':
			return 'weed'
		if percept in ('weeding_succeeded', 'does_not_need_weeding', 'hit_barrier'):
			x = randint(4)
			return(dict[x])
		#################################

class better_reflex_agent:
	def __init__(self):
		w, h = 100, 100
		self.Coords = [[0 for x in range(w)] for y in range(h)]
		self.X = 50
		self.Y = 50
		self.dir = 0
	# Given a valid percept (a string), return a valid action (also as a string)
	

	def choose_action(self, percept):
		##### Implement this function #####
		# You may store any amount of information about past percepts and actions,
		# use additional state variables, and perform any additional computation 
		# that you see fit, in order to outperform simple_reflex_agent.
		# Do not use randomness, or data structures not built into Python
		# You may only use sense_water, sense_weed, water, weed, and move as action
		
		if percept == 'start':
			self.Coords[self.X][self.Y] = 1
			return 'sense_water'
		
		if percept == 'move_succeeded':
			if self.dir == 0:
				self.X = self.X + 1
			elif self.dir == 1:
				self.Y = self.Y + 1
			elif self.dir == 2:
				self.X = self.X - 1
			else:
				self.Y = self.Y - 1
				
			if self.Coords[self.X][self.Y] == 0:
				self.Coords[self.X][self.Y] = 1
				return 'sense_water'
			else:
				return 'move'
			
		if percept == 'needs_watering':
			return 'water'
		if percept in ('does_not_need_watering', 'watering_succeeded'):
			return 'sense_weed'
		if percept == 'needs_weeding':
			return 'weed'
		if percept in ('weeding_succeeded', 'does_not_need_weeding'):
			return 'move'
		
		if percept == 'hit_barrier':
			if self.dir == 3:
				self.dir = 0
			else:
				self.dir = self.dir + 1
			return 'move'
		#################################

