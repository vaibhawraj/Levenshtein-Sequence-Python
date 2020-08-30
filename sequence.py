import numpy as np
import sys

def getMemorizationMatrix(StringA,StringB):
    matrix = np.zeros([len(StringA)+1,len(StringB)+1])
    
    for j in range(0,len(StringB)+1):
        matrix[0][j] = j
    
    for i in range(0,len(StringA)+1):
        matrix[i][0] = i
        
    for i in range(1,len(StringA)+1):
        for  j in range(1,len(StringB) + 1):
            if(StringA[i-1]==StringB[j-1]):
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = np.min([matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1]])+1
    
    return matrix

def backtrackSequence(matrix,  StringA, StringB, i=None, j=None):
    if(i==None):
        i = len(StringA)
    if(j==None):
        j = len(StringB)
    if(i==0 and j==0):
        return [[[],StringA,0]]
    if(i>=0 and j>=0 and StringA[i-1] == StringB[j-1]):
        paths = backtrackSequence(matrix,StringA,StringB,i-1,j-1)
        return paths
    else:
        paths = []
        if(matrix[i-1][j] + 1 == matrix[i][j] and i-1 >= 0):
            allPaths = backtrackSequence(matrix,StringA,StringB, i-1,j)
            for path in allPaths:
                cS = path[1]
                deviation = path[2]
                path[1] = cS[0:i+deviation-1] + cS[i+deviation:len(cS)]
                path[2] = deviation - 1
                #print(cS + " delete " + StringA[i-1] + " " + path[1] + " " + "("+str(i)+","+str(j)+")")
                path[0].append(cS + " delete " + StringA[i-1] + "("+str(i-1+deviation)+")")
            paths.extend(allPaths)
            #print('Paths',paths)
        if(matrix[i][j-1] + 1 == matrix[i][j] and j-1 >= 0):
            allPaths = backtrackSequence(matrix,StringA,StringB, i,j-1)
            for path in allPaths:
                cS = path[1]
                deviation = path[2]
                path[1] = cS[0:i+deviation] + StringB[j-1] + cS[i+deviation:len(cS)]
                path[2] = deviation + 1
                path[0].append(cS + " insert " + StringB[j-1] +  "("+str(i-1+deviation)+")")
            paths.extend(allPaths)
            #print('Paths',paths)
        if(matrix[i-1][j-1] + 1 == matrix[i][j] and i-1 >= 0 and j-1 >= 0):
            allPaths = backtrackSequence(matrix,StringA,StringB,i-1,j-1)
            for path in allPaths:
                cS = path[1]
                deviation = path[2]
                path[1] = cS[0:i+deviation-1] + StringB[j-1] + cS[i+deviation:len(cS)]
                path[0].append(cS + " replace " + StringA[i-1]  + " with " + StringB[j-1] +  "("+str(i-1+deviation)+")")
            paths.extend(allPaths)
            #print('Paths',paths)
        return paths

def listAllSequence(StringA,StringB):
    matrix = getMemorizationMatrix(StringA,StringB)
    allSequence = backtrackSequence(matrix,StringA,StringB)
    for path in allSequence:
        if(len(path[0])>0):
            print(" -> ".join(path[0])," -> ",path[1])
        else:
            print(StringA," -> ",StringB)

    
if __name__ == '__main__':
	if not len(sys.argv) == 3:
		print("Usage: $ sequence.py StringA StringB")
	else:
		listAllSequence(sys.argv[1],sys.argv[2])
