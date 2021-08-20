# Python program to rotate a matrix

# Function to rotate a matrix
def rotateMatrix(mat):

	if not len(mat):
		return
	
	"""
		top : starting row index
		bottom : ending row index
		left : starting column index
		right : ending column index
	"""

	top = 0
	bottom = len(mat)-1

	left = 0
	right = len(mat[0])-1

	print (bottom)

# Utility Function



# Test case 1
matrix =[
			[1, 2, 3, 4 ],
			[5, 6, 7, 8 ],
			[9, 10, 11, 12 ],
			[13, 14, 15, 16 ]
		]
# Test case 2
"""
matrix =[
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]
		]
"""

matrix = rotateMatrix(matrix)
# Print modified matrix
