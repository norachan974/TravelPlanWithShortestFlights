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

def test_shortest_flights_for_path_happy_case():
    path = ['JFK', 'ORD','JFK']
    flights = [
        ("JFK", "LAX", 7, 300),
        ("JFK", "ORD", 2, 150),
        ("ORD", "LAX", 4, 200),
        ("ORD", "JFK", 2, 220)
    ]
    graph = build_graph(flights)
    assert shortest_flights_for_path(path, graph) == "JFK->ORD, cost=2<br>ORD->JFK, cost=2<br>total cost is 4<br>"

def test_shortest_flights_for_path_sad_case():
    path = [1]
    flights = [
        ("JFK", "LAX", 7, 300),
        ("JFK", "ORD", 2, 150),
        ("ORD", "LAX", 4, 200),
        ("ORD", "JFK", 2, 220)
    ]
    graph = build_graph(flights)
    try:
        shortest_flights_for_path(path, graph)
    except TypeError as e:
        assert str(e) == "Expected a string, but got int"
    else:
        assert False, "Expected TypeError was not raised"






