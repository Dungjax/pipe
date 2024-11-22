from node import Node

class PathFinding:
    def __init__(self) -> None:
        
        pass

    def findPath(self, startNode, targetNode):
        openSet = []
        closedSet = []

        openSet.append(startNode)

        while len(openSet) > 0:
            currentNode = openSet[0]

            for node in openSet:
                if node.getCost() < currentNode.getCost():
                    currentNode = node

            openSet.remove(currentNode)
            closedSet.append(currentNode)

            if currentNode.position == targetNode.position:
                return
        pass