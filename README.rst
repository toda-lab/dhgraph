dhgraph: Python Modlue for Directed Hypergraphs
===============================================

Introduction
============
A *directed hypergraph* is a generalization of digraph.
It consists of a set of *vertices* ``V`` and a set of *hyperarcs* ``H``.
A hyperarc is a pair of a nonempty subset of ``V`` (called *head*) and a vertex
of ``V`` (called *tail*).

Installation
============

.. code:: shell-session

    $ pip install dhgraph

Usage
=====

Let us import ``dhgraph`` module, create an empty directed hypergraph object, 
and add hyperarcs as follows.

.. code:: python

    from dhgraph import DirectedHypergraph

    g = DirectedHypergraph()

    #   1 ---> 2
    #   |      |
    #   v      v
    #   4----> 3

    h1 = g.add_hyperarc((1,),  2)
    h2 = g.add_hyperarc((1,),  4)
    h3 = g.add_hyperarc((4, 2), 3)
    H = {h1, h2, h3} # Set of hyperarc identifiers, used later.

    # NOTE: The order of vertices in head is not important.
    assert h3 == g.add_hyperarc((2, 4), 3) 

    # NOTE: The output of get_head() is sorted.
    assert g.get_head(h3) == (2,4)
    assert g.get_tail(h3) == 3

As above, ``add_hyperarc()`` has a tuple of vertex identifiers, head, as its 1st
argument and a vertex identifier, tail, as its 2nd argument, 
and returns the identifier of a hyperarc having the head and the tail.

The vertices and the hyperarcs added so far can be obtained 
by ``get_vertices()`` and ``get_hyperarcs()``, which respecitvely return 
a tuple of vertex identifiers and a tuple of hyperarc identifiers, as follows.

.. code:: python

    assert set(g.get_vertices())  == {1, 2, 3, 4}
    assert set(g.get_hyperarcs()) == H

Hyperarcs that are incident to a vertex can be obtained by
``get_hyperarcs_from()`` and ``get_hyperarcs_to()``, which respectively return
a tuple of hyperarcs emanating from a vertex and a tuple of hyperarcs pointing
to a vertex, as follows.

.. code:: python

    assert set(g.get_hyperarcs_from(1)) == {h1, h2}
    assert set(g.get_hyperarcs_to(3))   == {h3}
    # exceptinal cases
    assert set(g.get_hyperarcs_from(3)) == set()
    assert set(g.get_hyperarcs_to(1))   == set()

Vertices and hyperarcs can be assigned labels, if necessary, when they are added.

.. code:: python

    gg = DirectedHypergraph()

    gg.add_vertex(1, label="A")
    gg.add_vertex(2, label="B")
    gg.add_vertex(3, label="C")
    gg.add_vertex(4, label="D")
    h1 = gg.add_hyperarc((1,),   2, label="A->B")
    h2 = gg.add_hyperarc((1,),   4, label="A->D")
    h3 = gg.add_hyperarc((4, 2), 3, label="B,D->C")
    
    assert gg.get_vertex_label(4)    == "D"
    assert gg.get_hyperarc_label(h3) == "B,D->C"

If you prefer to use vertex labels, call ``add_vertex()`` 
for all vertices to which labels are to be assigned and then call ``add_hyperarc()``.
Otherwise, ``add_hyperarc()`` will add vertices appearing in head or tail 
so that they have vertex identifiers as their labels.

A directed hypergraph can be rendered as follows.

.. code:: python

    gg.render(filename="sample", format="png")

As a result, ``sample.png`` will be generated.
The arugments of ``render()`` are the same as those of ``render()`` of
Graphviz.
See `User Guide of Graphviz
<https://graphviz.readthedocs.io/en/stable/manual.html>`__ .

Bugs/Requests/Discussions
=========================

Please report bugs and requests from `GitHub Issues
<https://github.com/toda-lab/dhgraph/issues>`__ , and 
ask questions from `GitHub Discussions <https://github.com/toda-lab/dhgraph/discussions>`__ .

License
=======

Please see `LICENSE <https://github.com/toda-lab/dhgraph/blob/main/LICENSE>`__ .
