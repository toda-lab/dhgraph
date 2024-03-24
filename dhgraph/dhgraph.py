from typing import Set, Tuple, Union, Optional
from os import PathLike

import graphviz

class DirectedHypergraph:
    """Class of directed hypergraph.

    A directed hypergraph is a generalization of digraph.
    It consists of a set of vertices V and a set of hyperarcs H.
    A hyperarc is a pair of a nonempty subset of V (called head) 
    and a vertex of V (called tail)."""

    def __init__(self) -> None:
        self._V                   = set()
        """Set of vertices"""
        self._H                   = set()
        """Set of hyperarcs"""
        self._vertex_label_dict   = {}
        """Dictionary that maps vertex to label."""
        self._hyperarc_label_dict = {}
        """Dictionary that maps hyperarc to label."""
        self._hyperarc_dict       = {}
        """Dictionary that maps pair of head and tail to hyperarc."""
        self._head_dict           = {}
        """Dictionary that maps hyperarc to head."""
        self._tail_dict           = {}
        """Dictionary that maps hyperarc to tail."""
        self._hyperarcs_from_dict = {}
        """Dictionary that maps vertex to set of hyperarcs from that vertex."""
        self._hyperarcs_to_dict   = {}
        """Dictionary that maps vertex to set of hyperarcs to that vertex."""

    def add_vertex(self, v: int, label: str = "") -> int:
        """Add a vertex with label.

        Nothing is done if v has been added.
        A label need not be unique to the vertex it is to be asscoaited to, 
        though the vertices of the same label will be rendered as a single 
        vertex by render().
        If label is not given, a vertex has its own identifier as label.

        Args:
            v: A vertex (identifier).
            label: A string to be associated to a vertex.

        Returns:
            A vertex (identifier).

        Raises:
            TypeError: if v is not an int.
            TypeError: if label is not a str.
        """
        if not isinstance(v, int):
            raise TypeError()
        if not isinstance(label, str):
            raise TypeError()
        if v in self._V:
            return self._V[v]
        self._V.add(v)
        self._vertex_label_dict[v] = label if label != "" else str(v)
        return v

    def add_hyperarc(self, head: Tuple[int], tail: Tuple[int], label: str = "")\
        -> int:
        """Adds a pair of head and tail (as a hyperarc) with label.

        Nothing is done if a pair of head and tail has been added.
        If head contains a vertex that is not yet added 
        or tail is not yet added, then all such vertices will be added 
        but with default label. If you prefer to set vertex label as you like, 
        call add_vertex() in advance.
        If label is not given, a hyperarc has its own identifier as label.

        Args:
            head: A tuple of vertices (i.e. vertex identifiers).
            tail: A vertex (identifier).
            label: A string to be associated to a hyperarc.

        Returns:
            A hyperarc (identifier).

        Raises:
            TypeError: if head is not a tuple.
            Exception: if head is an empty tuple.
            TypeError: if tail is not an int.
            TypeError: if label is not a str.
        """
        if not isinstance(head, tuple):
            raise TyperError()
        if len(head) == 0:
            raise Exception("empty head given")
        if not isinstance(tail, int):
            raise TypeError()
        if not isinstance(label, str):
            raise TypeError()
        normalized_head = tuple(sorted(head))
        key = (normalized_head, tail) 
        if key in self._hyperarc_dict:
            return self._hyperarc_dict[key]
        new_hyperarc = len(self._hyperarc_dict)+1
        self._hyperarc_dict[key] = new_hyperarc
        self._head_dict[new_hyperarc] = normalized_head
        self._tail_dict[new_hyperarc] = tail
        assert not new_hyperarc in self._H
        self._H.add(new_hyperarc)
        for v in head:
            if not v in self._V:
                self.add_vertex(v) # NOTE: add v with default label
            if not v in self._hyperarcs_from_dict:
                self._hyperarcs_from_dict[v] = set()
            self._hyperarcs_from_dict[v].add(new_hyperarc)
        if not tail in self._V:
            self.add_vertex(tail) # NOTE: add tail with default label
        if not tail in self._hyperarcs_to_dict:
            self._hyperarcs_to_dict[tail] = set()
        self._hyperarcs_to_dict[tail].add(new_hyperarc)
        self._hyperarc_label_dict[new_hyperarc] =\
            label if label != "" else str(new_hyperarc)
        return new_hyperarc

    def get_vertices(self) -> Tuple[int]:
        """Gets a tuple of all vertices.

        Returns:
            A tuple of all vertices (i.e. vertex identifiers).
        """
        return tuple(self._V)

    def get_hyperarcs(self) -> Tuple[int]:
        """Gets a tuple of all hyperarcs.

        Returns:
            A tuple of all hyperarcs (i.e. hyperarc identifiers).
        """
        return tuple(self._H)

    def get_head(self, h: int) -> Tuple[int]:
        """Gets the head of a hyperarc.

        Args:
            h: A hyperarc (identifier).

        Returns:
            A (sorted) tuple of vertices (i.e. vertex identifiers).

        Raises:
            TypeError: if h is not an int.
        """
        if not isinstance(h, int):
            raise TypeError()
        return self._head_dict[h]

    def get_tail(self, h: int) -> int:
        """Gets the tail (a vertex) of a hyperarc.

        Args:
            h: A hyperarc (identifier).

        Returns:
            A vertex (identifier).

        Raises:
            TypeError: if h is not an int.
        """
        if not isinstance(h, int):
            raise TypeError()
        return self._tail_dict[h]

    def get_hyperarcs_from(self, v: int) -> Tuple[int]:
        """Gets a tuple of all hyperarcs emanating from a vertex.

        Args:
            v: A vertex (identifier).

        Returns:
            A (possibly empty) tuple of hyperarcs (i.e. hyperarc identifiers).

        Raises:
            TypeError: if v is not an int.
        """
        if not isinstance(v, int):
            raise TypeError()
        if not v in self._hyperarcs_from_dict:
            return ()
        return tuple(self._hyperarcs_from_dict[v])

    def get_hyperarcs_to(self, v: int) -> Tuple[int]:
        """Gets a tuple of all hyperarcs pointing to a vertex.

        Args:
            v: A vertex (identifier).

        Returns:
            A (possibly empty) tuple of hyperarcs (i.e. hyperarc identifiers).

        Raises:
            TypeError: if v is not an int.
        """
        if not isinstance(v, int):
            raise TypeError()
        if not v in self._hyperarcs_to_dict:
            return ()
        return tuple(self._hyperarcs_to_dict[v])

    def get_vertex_label(self, v: int) -> str:
        """Gets the label of a vertex.

        Args:
            v: A vertex (identifier).

        Returns:
            A vertex label.

        Raises:
            TypeError: if v is not an int.
        """
        if not isinstance(v, int):
            raise TypeError()
        return self._vertex_label_dict[v]

    def get_hyperarc_label(self, h: int) -> str:
        """Gets the label of a hyperarc.

        Args:
            h: A hyperarc (identifier).

        Returns:
            A hyperarc label.

        Raises:
            TypeError: if h is not an int.
        """
        if not isinstance(h, int):
            raise TypeError()
        return self._hyperarc_label_dict[h]

    def render(self, filename: Union[PathLike,str,None] = None,\
    directory: Union[PathLike,str,None] = None, view: bool = False,\
    cleanup: bool = False, format: Optional[str] = None,\
    renderer: Optional[str] = None, formatter: Optional[str] = None,\
    neato_no_op: Union[bool,int,None] = None, quiet: bool = False,\
    quiet_view: bool = False, outfile: Union[PathLike,str,None] = None,\
    engine: Optional[str] = None, raise_if_result_exists: bool = False,\
    overwrite_source: bool = False) -> None:
        """Saves the source to file and renders with the Graphviz engine.

        The arguments are the same as those of render() of Graphviz:
        https://graphviz.readthedocs.io/en/stable/manual.html .
        The vertices of the same label will be rendered as a single vertex,
        and isolated vertices (i.e. those no hyperarc is incident to) 
        will not be rendered.
        """
        dot = graphviz.Digraph()
        for h in self.get_hyperarcs():
            for u in self.get_head(h):
                v = self.get_tail(h)
                dot.edge(self.get_vertex_label(u), self.get_vertex_label(v),\
                    self.get_hyperarc_label(h))
        dot.render(filename=filename, directory=directory, view=view,\
            cleanup=cleanup, format=format, renderer=renderer,\
            formatter=formatter, neato_no_op=neato_no_op, quiet=quiet,\
            quiet_view=quiet_view, outfile=outfile, engine=engine,\
            raise_if_result_exists=raise_if_result_exists,\
            overwrite_source=overwrite_source)
