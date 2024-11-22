from enum import Enum


class Direction(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
    LEFT_TOP = "LEFT_TOP"
    LEFT_DOWN = "LEFT_DOWN"
    RIGHT_TOP = "RIGHT_TOP"
    RIGHT_DOWN = "RIGHT_DOWN"


class State(Enum):
    READY = "READY"
    PROCESS = "PROCESS"
    END = "END"