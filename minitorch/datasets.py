import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N: int) -> List[Tuple[float, float]]:
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N: int) -> Graph:
    """
    Generates a simple dataset where points are classified based on x_1.
    If x_1 < 0.5 then y = 1, else y = 0.
    Args:
        N: Number of points.
    Returns:
        Graph: Object containing points and labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N: int) -> Graph:
    """
    Generates a dataset with diagonal split.
    If x_1 + x_2 < 0.5 then y = 1, else y = 0.
    Args:
        N: Number of points.
    Returns:
        Graph: Object containing points and labels.
    """

    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N: int) -> Graph:
    """
    Generates a dataset with two regions split along x-axis.
    If x_1 < 0.2 or x_1 > 0.8 then y = 1, else y = 0.
    Args:
        N: Number of points.
    Returns:
        Graph: Object containing points and labels.
    """

    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N: int) -> Graph:
    """
    Generates an XOR pattern dataset.
    If (x_1 < 0.5 and x_2 > 0.5) or (x_1 > 0.5 and x_2 < 0.5) then y = 1, else y = 0.
    Args:
        N: Number of points.
    Returns:
        Graph: Object containing points and labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if ((x_1 < 0.5 and x_2 > 0.5) or (x_1 > 0.5 and x_2 < 0.5)) else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N: int) -> Graph:
    """
    Generates a circular pattern dataset.
    If (x_1 - 0.5)^2 + (x_2 - 0.5)^2 > 0.1 then y = 1, else y = 0.
    Args:
        N: Number of points.
    Returns:
        Graph: Object containing points and labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = (x_1 - 0.5, x_2 - 0.5)
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N: int) -> Graph:
    """
    Generates a spiral pattern dataset.
    Creates two interleaved spirals, one for each class (y = 0 and y = 1).
    Args:
        N: Number of points.
    Returns:
        Graph: Object containing points and labels.
    """
    def x(t: float) -> float:
        return t * math.cos(t) / 20.0

    def y(t: float) -> float:
        return t * math.sin(t) / 20.0

    X = [
        (x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    X = X + [
        (y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {
    "Simple": simple,
    "Diag": diag,
    "Split": split,
    "Xor": xor,
    "Circle": circle,
    "Spiral": spiral,
}
