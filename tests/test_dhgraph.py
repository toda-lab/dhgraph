from dhgraph import DirectedHypergraph

def test_dhgraph():
    testcase_list = [\
        #0) list of head-tail pairs,      1)list of isolated vertices
        [[((2,),1), ((3,1),2), ((1,),3)], [0,4]],\
        [[((2,3),1), ((3,2),4), ((3,),2)], [-1]],\
        [[], []],\
        [[], [1,2,3]],\
        [[((1,2,3,4),1)], []],\
        [[((1,),1)], []],\
    ]

    for head_tail_pair_list, isolated_vertex_list in testcase_list:
        g = DirectedHypergraph()
        # Initialize auxilliary data structures for testing.
        V = set()                # set of vertices
        H = set()                # set of hyperarcs
        head_dict = {}           # hyperarc -> head
        tail_dict = {}           # hyperarc -> tail
        hyperarcs_from_dict = {} # head -> set of hyperarcs
        hyperarcs_to_dict   = {} # tail -> set of hyperarcs
        # Add hyperarcs.
        for pair in head_tail_pair_list:
            h = g.add_hyperarc(pair[0], pair[1])
            # Update auxilliary data structures.
            H.add(h)
            assert not h in head_dict
            head_dict[h] = tuple(sorted(pair[0]))
            assert not h in tail_dict
            tail_dict[h] = pair[1]
            for v in pair[0]:
                V.add(v)
                if not v in hyperarcs_from_dict:
                    hyperarcs_from_dict[v] = set()
                hyperarcs_from_dict[v].add(h)
            if not pair[1] in hyperarcs_to_dict:
                hyperarcs_to_dict[pair[1]] = set()
            V.add(pair[1])
            hyperarcs_to_dict[pair[1]].add(h)
        # Test vertex set and hyperarc set.
        assert set(g.get_vertices())  == V
        assert set(g.get_hyperarcs()) == H
        # Test get_head() and get_tail().
        for h in g.get_hyperarcs():
            assert g.get_head(h) == head_dict[h]
            assert g.get_tail(h) == tail_dict[h]
        # Test get_hyperarcs_from() and get_hyperarcs_to().
        for h in g.get_hyperarcs():
            head = g.get_head(h)
            tail = g.get_tail(h)
            for v in head:
                assert h in g.get_hyperarcs_from(v)
                assert set(g.get_hyperarcs_from(v)) == hyperarcs_from_dict[v]
            assert h in g.get_hyperarcs_to(tail)
            assert set(g.get_hyperarcs_to(tail)) == hyperarcs_to_dict[tail]
        # Test whether vertices are isolated.
        for v in isolated_vertex_list:
            assert not v in g.get_vertices()
        # Add isolated vertices.
        for v in isolated_vertex_list:
            g.add_vertex(v)
        # Test vertex set agvain.
        assert set(g.get_vertices()) == (V | set(isolated_vertex_list))
        # Test get_hyperarcs_from() and get_hyperarcs_to().
        for v in isolated_vertex_list:
            assert g.get_hyperarcs_from(v) == ()
            assert g.get_hyperarcs_to(v)   == ()
        # Test get_vertex_label() and get_hyperarc_label().
        for v in g.get_vertices():
            assert g.get_vertex_label(v)   == str(v)
        for h in g.get_hyperarcs():
            assert g.get_hyperarc_label(h) == str(h)
