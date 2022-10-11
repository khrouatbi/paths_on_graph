def main(): 
    NeighborNodes = dict() 
    NeighborNodes['A'] = ['B', 'D', 'H']
    NeighborNodes['B'] = ['A', 'D','C'] 
    NeighborNodes['C'] = ['B', 'D','F'] 
    NeighborNodes['D'] = ['A', 'B', 'C', 'E'] 
    NeighborNodes['E'] = ['D', 'F','H'] 
    NeighborNodes['F'] = ['C', 'E', 'G'] 
    NeighborNodes['G'] = ['F', 'H'] 
    NeighborNodes['H'] = ['A', 'E', 'G'] 
    
    paths = getAllSimplePaths('A', 'H', NeighborNodes)
    for path in paths:
        print(path)

def getAllSimplePaths(originNode, targetNode, NeighborNodes): 
    return getAllPaths(targetNode, 
                                 [originNode], 
                                 set(originNode), 
                                 NeighborNodes, 
                                 list()) 
 
def getAllPaths(targetNode, 
                          currentPath, 
                          usedNodes, 
                          NeighborNodes, 
                          answerPaths): 

    lastNode = currentPath[-1] 
    if lastNode == targetNode: 
        answerPaths.append(list(currentPath)) 
    else: 
        for neighbor in NeighborNodes[lastNode]: 
            if neighbor not in usedNodes: 
                currentPath.append(neighbor) 
                usedNodes.add(neighbor) 
                getAllPaths(targetNode, 
                                      currentPath, 
                                      usedNodes, 
                                      NeighborNodes, 
                                      answerPaths) 
                usedNodes.remove(neighbor) 
                currentPath.pop() 
    return answerPaths 
 
if __name__ == '__main__': 
    main() 