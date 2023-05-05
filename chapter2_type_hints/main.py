from typing import Self


def add(x: int, y: int) -> int:
    return x + y


def add2(x: int | float, y: int | float) -> int:
    return x + y


class Shape:

    def __init__(self):
        self.scale = 0.0

    def set_scale(self, scale: float) -> Self:
        self.scale = scale
        return self
