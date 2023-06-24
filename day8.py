import numpy as np
with open('day8.txt', 'r') as f:
    lines=f.readlines()
    lines = [entry.strip() for entry in lines]

trees = np.zeros((len(lines), len(lines[0])), dtype=int)
for i, line in enumerate(lines):
    trees[i, :] = np.array(list(line))

numVis=2*len(lines[0])+2*(len(lines)-2)

for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        tCol=trees[:, j]-trees[i,j]
        tRow=trees[i,:]-trees[i,j]
        posRoutes=[tRow[:j], tRow[j+1:], tCol[:i],tCol[i+1:]]
        if sum(list(map(lambda route: (route<0).all(), posRoutes)))>0:
            numVis+=1
print(numVis)

sceneScore = np.zeros((len(lines), len(lines[0])), dtype=int)
def compSceneScore(route):
    bigassArray = list(route>=0)
    if True in bigassArray:
        return bigassArray.index(True)+1
    else:
        return len(bigassArray)
    
for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        tCol = trees[:, j] - trees[i, j]
        tRow = trees[i, :] - trees[i, j]
        routeList = [tRow[j-1::-1], tRow[j+1:], tCol[i-1::-1], tCol[i+1:]]
        sceneScore[i,j]=np.prod(list(map(compSceneScore, routeList)))
print(np.max(sceneScore))
    
