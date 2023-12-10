""" Used to declared types used"""
from collections.abc import Sequence
from typing import Union


NumReal = Union[float, int]
Number = Union[float, int, complex]
VectorReal = Sequence[NumReal]
