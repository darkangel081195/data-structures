# // Main algorithm: in order to rotate the whole matrix, we'll just rotate one ring at a time
# // We can do this in-place to achieve O(1) additional space complexity
k = int(input())
n,m = map(int,input().split(','))
matrix = [None]*(n+1)
for i in range(n):
    matrix[i] = input().split(',')

numRings = min(n,m)//2
for i in range(numRings):
    numRotations = k%(2*(n + m - 4*i) - 4)
    if(i%2 == 0):
        # //Rotate anticlockwise direction
        for _ in range(numRotations):
            # // Rotate top row
            for j in range(i,m-i-1):
                matrix[i][j],matrix[i][j+1] = matrix[i][j+1],matrix[i][j]

            # // Rotate right column
            for j in range(i,n-i-1):                
                matrix[j][m-i-1],matrix[j+1][m-i-1] = matrix[j+1][m-i-1], matrix[j][m-i-1]
                
            # // Rotate bottom row
            for j in range(m-i-1,i,-1):
                matrix[n-i-1][j],matrix[n-i-1][j-1] = matrix[n-i-1][j-1],matrix[n-i-1][j]
                
            # // Rotate left column
            for j in range(n-i-1,i+1,-1):
                matrix[j][i],matrix[j-1][i] = matrix[j-1][i],matrix[j][i]

    else:
        # //Rotate clockwise direction
        for _ in range(numRotations): 
            # //Rotate Top row
            for j in range(m-i-1,i,-1):
                matrix[i][j],matrix[i][j-1] = matrix[i][j-1], matrix[i][j]

            # // Rotate left column
            for j in range(i,n-i-1):
                matrix[j][i],matrix[j+1][i] = matrix[j+1][i],matrix[j][i]
                
            # // Rotate bottom row
            for j in range(i,m-i-1):
                matrix[n-i-1][j],matrix[n-i-1][j+1] = matrix[n-i-1][j+1],matrix[n-i-1][j]
                
            # // Rotate right column
            for j in range(n-i-1,i+1,-1):
                matrix[j][m-i-1],matrix[j-1][m-i-1] = matrix[j-1][m-i-1],matrix[j][m-i-1]
            
# // Output final matrix
for i in range(n):
    print(','.join(matrix[i]))
