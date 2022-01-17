"""
problem is to convert the negative entries in matrix, the surrounding of positive nums can expand into 4 directions, and convert negative nums into 
positive, and the problem is asking the minimal rounds of the conversion to turn the whole matrix into non-negative. 
BFS 
"""
# Input:

# mat = [
# 	[-1, -9,  0, -1,  0],
# 	[-8, -3, -2,  9, -7],
# 	[ 2,  0,  0, -6,  0],
# 	[ 0, -7, -3,  5, -4]
# ]

# Output: 3


# Input:

# mat = [
# 	[1, 9, 1],
# 	[8, 3, 2],
# 	[7, 3, 4]
# ]

# Output: 0


# The solution should return -1 if conversion is not possible.

# Input:

# mat = [
# 	[-1, -9, -1],
# 	[-8, -3, -2],
# 	[-7, -3, -4]
# ]

# Output: -1


import sys 
from collections import deque
	
def findMinPasses(mat):
  # Write your code here.

  def isValid(mat,r,c):
    return 0<=r<len(mat) and 0<=c<len(mat[0])
  
  def hasNegative(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] < 0:
                return True
    return False
 
  q=deque()
  #mat's shape
  m, n =len(mat),len(mat[0])
  #traverse mat to get positive integers and locate at front of deque
  for i in range(m):
    for j in range(n):
      if mat[i][j]>0:
        #record the row,col, and level of BFS
        q.append((i,j,0))
  # 	  (-1,0)		
  # (0,-1)(0,0)(0,1)
  #       (1,0)
  dir_row = [1,0,-1,0]
  dir_col=[0,-1,0,1]
  last =-1
  while q:
    
    for _ in range(len(q)):
      row,col,level =q.popleft()
      last =level
      for i in range(len(dir_row)):
        next_row =row+dir_row[i] 
        next_col =col+dir_col[i] #row,col moves to row,col+1
        
        if isValid(mat,next_row,next_col): 
          if mat[next_row][next_col]==0:
            continue 
          elif mat[next_row][next_col] <0:
            mat[next_row][next_col] *=-1
            q.append((next_row,next_col,level+1))
  if hasNegative(mat) ==True:
    print('negative')
  return last
if __name__ =='__main__':
  mat = [
    [-1, -9,  0, -1,  0],
    [-8, -3, -2,  9, -7],
    [ 2,  0,  0, -6,  0],
    [ 0, -7, -3,  5, -4]
  ]
  findMinPasses(mat)
