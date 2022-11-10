import numpy as np

'''
It works only for the simple case of 1 mismatch
Correct for the multicase
'''

def verifyMagicSquare(matrix) -> bool:
    
    main_diagonal = []
    second_diagonal = []
    
    upTo = 0
    i = 0
    for line in matrix:
        
        main_diagonal.append(line[i])
        second_diagonal.append(len(line)-1-i)

        if i == 0:
            upTo = sum(line)
        if(sum(line) != upTo):
            return False         
        i += 1

    for line in matrix.T:
        if(sum(line) != upTo):
            return False         
    return True

def substitute(x, matrix, coordinates) -> bool:
    
    result = False
    
    for coord in coordinates:
        old = matrix[coord[0]][coord[1]]
        matrix[coord[0]][coord[1]] = x
        result = verifyMagicSquare(matrix)
        if result == True:
            cost = np.abs(old - x)
            return True, cost
        else:
             matrix[coord[0]][coord[1]] = old
    return result


matrix = np.array([[4, 9, 2], [3, 5, 7], [8, 1, 5]])
result = verifyMagicSquare(matrix)


series = [1,2,3,4,5,6,7,8,9]
matrix_set = np.unique(matrix)
diff = list(set(series) - set(matrix_set))

seen = set()
dupes = [x for x in np.ravel(matrix) if x in seen or seen.add(x)]   

if result == False:
    print('da correggere')


for double in dupes:
    a = np.where(matrix == double)

listOfCoordinates= list(zip(a[0], a[1]))


for x in diff:
    result, cost = substitute(x,matrix,listOfCoordinates)
    if result == True:
        print(matrix)
        print(cost)
        break 

