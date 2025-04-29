import pytest
from algorithm import *
# happy case
def test_build_graph_happy_case():
    flights = [
        ("JFK", "LAX", 6, 300),
        ("JFK", "ORD", 2, 150),
        ("ORD", "LAX", 4, 200)
    ]
    graph = build_graph(flights)
    assert graph["JFK"] == [(6, "LAX"), (2, "ORD")]
    assert graph["ORD"] == [(4, "LAX")]
    assert "LAX" not in graph

# sad case
def test_build_graph_sad_case():
    flights = "this is not a list"
    try:
        build_graph(flights)
    except TypeError as e:
        assert str(e) == "Expected a list, but got str"
    else:
        assert False, "Expected TypeError was not raised"

