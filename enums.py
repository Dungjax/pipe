from enum import Enum

class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"
    TOP = "T"
    DOWN = "D"


class State(Enum):
    READY = "READY"
    PROCESS = "PROCESS"
    END = "END"

class NodeType(Enum):
    ALLOWED = "ALLOWED"
    BLOCKED = "BLOCKED"