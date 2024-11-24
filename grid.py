from setting import TILE_SIZE, Vector2

def toLocalPoint(position):
        return (position // TILE_SIZE)
        pass

def toWorldPoint(position):
        return (position * TILE_SIZE)
        pass