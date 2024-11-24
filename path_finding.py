from pipe import pipes, Pipe

nodes = []

def findPath(startNode, targetNode):
    s = startNode.__class__(startNode.position)
    openSet = [startNode]
    closedSet = {}
    pipes.clear()

    for w in range(1000):
        currentNode = openSet[0]
        for i in range(1, len(openSet), 1):
            if openSet[i].getCost() < currentNode.getCost() or (openSet[i].getCost() == currentNode.getCost() and openSet[i].hCost < currentNode.hCost):
                currentNode = openSet[i]

        openSet.remove(currentNode)
        closedSet[tuple(currentNode.position)] = "closed"
        
        if currentNode.position == targetNode.position:
            #print(w)
            retracePath(startNode, currentNode)

            for pipe in nodes:
                pipe.changeDirection()

            for pipe in nodes:
                pipe.setSprite()
            return
        
        for neighbor in currentNode.getNeighbors(Pipe):
            if closedSet.get(tuple(neighbor.position)) == "closed":
                continue

            newMovementCostToNeighbor = currentNode.gCost + currentNode.getDistance(neighbor)

            if newMovementCostToNeighbor < neighbor.gCost or neighbor not in openSet:
                neighbor.gCost = newMovementCostToNeighbor
                neighbor.hCost = neighbor.getDistance(targetNode)
                neighbor.parent = currentNode

                if neighbor not in openSet:
                    openSet.append(neighbor)
            pass
    pass

def retracePath(startNode, targetNode):
    currentNode = targetNode

    while currentNode != startNode:
        nodes.append(currentNode)
        pipes.append(currentNode)
        currentNode = currentNode.parent
        pass

    nodes.reverse()
    pass