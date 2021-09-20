import sys
import copy
import heapq
import os
import time
from threading import Thread


# wait = ['|', '\\', '-', '/']
wait = ['.     ', '..    ', '...   ', '....  ', '..... ', '......']

getNeighboorCoors = lambda size, y, x: [(y1, x1) for y1, x1 in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)] if ((0 <= y1 < size) and (0 <= x1 < size))]
getTuple = lambda matrix: tuple(tuple(line) for line in matrix)

def manhattanDist(state, puzzle):
	dist = 0
	for y, _ in enumerate(state):
		for x, _ in enumerate(state[y]):
			if state[y][x]:
				y1, x1 = puzzle.goal[state[y][x]]
				dist += abs(x - x1) + abs(y - y1)
	return dist

def parseFile(path):
	out = []
	def getLine(line):
		out = []
		for val in line:
			if not val.isdigit():
				print ("Error %s is not a digit !" % val)
			out.append(int(val))
		return out

	with open(path, 'r') as f:
		for l in f.readlines():
			line = l.split()
			if line[0] == '#':
				pass
			elif len(line) == 1 and line[0].isdigit():
				size = int(line[0])
			else:
				gridLine = getLine(line)
				out.append(gridLine)
	return out

def	aStar(start, puzzle):
	# def printWait(stop_thread):
	# 	waiter = 0.0
	# 	while True:
	# 		if stop_thread is True:
	# 			return
	# 		print ("\r%c\r" % wait[int(waiter)], end='')
	# 		waiter += 0.01
	# 		if waiter > 3.0:
	# 			waiter = 0.0
	
	# stop_thread = False
	# thread = Thread(target=printWait, args=(lambda : stop_thread, ))
	openSet = []
	seenset = {}

	# thread.start()
	waiter = 0.0
	seenset[getTuple(start.state)] = start.g
	start.g = 0
	openSet.append((start.g + start.h, id(start), start))
	while len(openSet) > 0:
		print ("\r%s%s\r" % ('.' * (int(waiter) + 1), ' ' * (16 - int(waiter))), end='')
		waiter += 0.0003
		if waiter > 15.0:
			waiter = 0.0
		current = heapq.heappop(openSet)[2]
		if current.h == 0:
			# stop_thread = True
			return current
		for matrix in current.getNeighboorStates():
			move = State(matrix, puzzle)
			move.g = current.g + 1
			key = getTuple(move.state)
			if key not in seenset or move.g < seenset[key]:
				seenset[key] = move.g
				move.parent = current
				heapq.heappush(openSet, (move.g + move.h, id(move), move))
	# stop_thread = True
	return None



class	State():

	def __init__(self, matrix, puzzle):
		self.state = matrix
		self.parent = 0
		self.g = puzzle.size * puzzle.size
		self.h = manhattanDist(matrix, puzzle)

	def zeroPos(self):
		y = 0
		while y < len(self.state):
			x = 0
			while x < len(self.state):
				if self.state[y][x] == 0:
					return y, x
				x += 1
			y +=1

	def getNeighboorStates(self):
		y, x = self.zeroPos()
		neighboorCoords = getNeighboorCoors(puzzle.size, y, x)
		neighboors = [copy.deepcopy(self.state) for _ in neighboorCoords]
		for i in range(len(neighboorCoords)):
			y1, x1 = neighboorCoords[i]
			neighboors[i][y][x], neighboors[i][y1][x1] = self.state[y1][x1], self.state[y][x]
		return neighboors


class	Puzzle:
	def __init__(self, size):
		self.size = size

	def get_goal(self):
		def rotate(rows, cols, x):
			print(x)
			return ([list(range(x, x + cols))] + \
			[list(reversed(x)) for x in zip(*rotate(cols, rows - 1, x + cols))]
			if 0 < cols \
			else [[0]])
		self.goal_array = rotate(self.size, self.size, 1)
		self.goal = {}
		for y, _ in enumerate(self.goal_array):
			for x, _ in enumerate(self.goal_array[y]):
				self.goal[self.goal_array[y][x]] = (y, x)

def print_matrix(matrix):
	for line in matrix:
		for val in line:
			print ((" %3d " % val if val != 0 else " %3c " % ' '), end='')
		print()
	print()

def printSolution(state, start):
	if state is not start:
		printSolution(state.parent, start)
	print_matrix(state.state)

if __name__ == "__main__":
	inputGrid = parseFile(sys.argv[1])
	startTime = time.time()
	puzzle = Puzzle(len(inputGrid))
	puzzle.get_goal()
	start = State(inputGrid, puzzle)
	neighboors = start.getNeighboorStates()
	finish = aStar(start, puzzle)
	print('\r', end='')
	printSolution(finish, start)
	endTime = time.time()
	print('Time to solve : %.4f seconds' % (endTime - startTime))
