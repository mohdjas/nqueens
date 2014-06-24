# N Queens Problem
from datetime import datetime

numberOfBoards = 0

class Board:
	"""Class representing an NxN chess board."""
	def __init__(self, q, ec):
		self.queens = q
		self.emptyCols = ec 
		
def display(bd):
  print bd.queens,
  print bd.emptyCols
	
def nextBoards(bd):
	
	return placeQueens(bd, nextQueenPositions(bd))

def nextQueenPositions(bd):
	ecs = list(bd.emptyCols)
	for sq in bd.emptyCols:
		if not safeSquare(bd, sq):
			try:
				ecs.remove(sq)       #each element is guaranteed to appear only once
			except:
				pass
	
	return ecs

def safeSquare(bd, sq):
	for q in bd.queens:
		if attacks(bd, q, sq):
			return False
	return True

def attacks(bd, q, sq):
	try:
		r1, c1 = bd.queens.index(q), q
		r2, c2 = len(bd.queens), sq
	except:
	  pass
	return abs(r2-r1) == abs(c2-c1)

def placeQueens(bd, nextQueenPositions):
	#Make a list of Boards given current bd config and the nextQueenPositions
	nextBoards = []
	for sq in nextQueenPositions:
		nqns = list(bd.queens)
		necs = list(bd.emptyCols)
		try:
			nqns.append(sq)
			necs.remove(sq)
			nextBoard = Board(nqns, necs)
			nextBoards.append(nextBoard)
		except:
			pass
	return nextBoards
		
def queens(n):
	bd = Board([], [x for x in range(n)])
	
	return queensBoard(bd)
	
def queensBoard(bd):
	global numberOfBoards
	numberOfBoards = numberOfBoards + 1
	if solved(bd):
		return bd
	else:
		return queensList(nextBoards(bd))

def queensList(nextBds):
	if not nextBds: #next-bds is empty
		return False
	else:
		
	  child = queensBoard(nextBds[0])
	  
	  if child:
	  	return child
	  else:
	  	return queensList(nextBds[1:])
	
def solved(bd):
	return not bd.emptyCols

for n in range(4, 20):
	startTime = datetime.now()
	
	print "n: ", n, "\t",
	display(queens(n))
	print "t: ", (datetime.now()-startTime), "\t",
	print numberOfBoards
	print ""
	

