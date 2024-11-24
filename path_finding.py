from pipe import pipes, Pipe
from grid import grids
from enums import Direction
from pygame import Vector2

nodes = []

def findPath(_startNode, _targetNode):
    startNode = _startNode

    targetNode = Pipe(_targetNode.position + Vector2(1, 0))

    match _targetNode.endDirection:
        case Direction.LEFT:
            targetNode.position = _targetNode.position + Vector2(-1, 0)
        
        case Direction.TOP:
            targetNode.position = _targetNode.position + Vector2(0, -1)

        case Direction.DOWN:
            targetNode.position = _targetNode.position + Vector2(0, 1)
    
    openSet = [startNode]
    closedSet = {}

    pipes.clear()

    for w in range(1000):
        if len(openSet) > 0:
            currentNode = openSet[0]
        else:
            return
        
        for i in range(1, len(openSet), 1):
            if openSet[i].getCost() < currentNode.getCost() or (openSet[i].getCost() == currentNode.getCost() and openSet[i].hCost < currentNode.hCost):
                currentNode = openSet[i]

        openSet.remove(currentNode)
        closedSet[tuple(currentNode.position)] = "closed"
        
        if currentNode.position == targetNode.position:
            retracePath(startNode, currentNode)

            for pipe in nodes:
                pipe.changeDirection()

            pipe.endDirection = _targetNode.startDirection

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

    nodes.clear()

    while currentNode != startNode:
        nodes.append(currentNode)
        pipes.append(currentNode)
        grids[tuple(currentNode.position)] = currentNode
        currentNode = currentNode.parent
        pass

    nodes.reverse()
    pass