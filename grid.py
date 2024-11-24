from setting import TILE_SIZE, Vector2

grids = {}

def toLocalPoint(position):
        return (position // TILE_SIZE)
        pass

def toWorldPoint(position):
        return (position * TILE_SIZE)
        pass