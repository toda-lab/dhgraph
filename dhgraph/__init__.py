# dhgraph: Python module for directed hypergraphs

import importlib.metadata

__version__ = importlib.metadata.version(__package__)

from .dhgraph import DirectedHypergraph

__all__ = [
    "DirectedHypergraph",
]
