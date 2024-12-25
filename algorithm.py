from collections import defaultdict
from heapq import heappop, heappush

flights = [("oslo", "lofoton", 185, 155), ("lofoton", "oslo", 175, 144), \
           ("oslo", "tromso", 115, 89), ("tromso", "oslo", 120, 89), \
           ("tromso", "lofoton", 135, 210), ("lofoton", "tromso",120, 295), \
           ("tromso", "longyearbyen", 100, 133), ("longyearbyen", "tromso", 95, 120), \
           ("tromso", "stockholm", 125, 120), ("stockholm", "tromso", 115, 127), \
           ("longyearbyen", "stockholm", 300, 146), ("stockholm", "longyearbyen", 325, 162),\
           ("stockholm", "oslo", 60, 58), ("oslo", "stockholm", 60, 59), \
           #("stockholm", "lofoton", ), ("lofoton", "stockholm", ), \
           #("lofoton", "longyearbyen"), ("longyearbyen", "lofoton"), \
           ("oslo", "longyearbyen", 260, 142), ("longyearbyen", "oslo", 265, 124),\
           ]

def build_graph(flights):
  graph = defaultdict(list)
  for start, end, duration, price in flights:
    graph[start].append((duration, end))
  return graph
  #print(graph)



def shortest_path_to_visit_all_nodes(graph, start):
    n = len(graph)  # Number of nodes
    visited = set()
    pre = dict()
    for node in graph.keys():
      pre[node] = None
    distance = dict()
    for node in graph.keys():
      distance[node] = float('inf')
    #distance = [float('inf')] * n
    distance[start] = 0
    heap = [(0, start)]  # (current_cost, current_node)

    while heap:
        curr_dist, curr_node = heappop(heap)

        if curr_node in visited:
            continue
        visited.add(curr_node)

        for weight, neighbor in graph[curr_node]:
            if neighbor not in visited:
                new_dist = curr_dist + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    pre[neighbor] = curr_node
                    heappush(heap, (new_dist, neighbor))
    if len(visited) != n:
        return None, None
    path = []
    for node in graph.keys():
      if node == start:
        continue
      curr = node
      temp_path = []
      while curr != None:
        temp_path.append(curr)
        curr = pre[curr]
      temp_path.reverse()
      path.extend(temp_path[1:])
    return distance, [start] + path

path = ['oslo', 'lofoton', 'tromso', 'longyearbyen', 'stockholm', 'oslo']

graph = build_graph(flights)
def shortest_flights_for_path(path, graph):
  total = 0
  curr = 'oslo'
  res = ""
  for city in path[1:]:
    for cost, neighbor in graph[curr]:
      if neighbor == city:
        total += cost
        #print(f"{curr}->{city}, cost={cost}")
        res += f"{curr}->{city}, cost={cost}<br>"
        curr = city
        break
  #print(f"total cost is {total}")
  res += f"total cost is {total}<br>"
  return res
# print(curr == "oslo")
# print(total)