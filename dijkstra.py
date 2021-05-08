import tube_network
import sys


def shortest_time(start, finish):
    graph = tube_network.network
    start = start.strip()
    finish = finish.strip()
    start = start.replace("'", "")
    finish = finish.replace("'", "")
    start = start.upper()
    finish = finish.upper()

    if start == "KINGS CROSS" or start == "ST PANCRAS":
        start = "KINGS CROSS ST PANCRAS"

    if finish == "KINGS CROSS" or finish == "ST PANCRAS":
        finish = "KINGS CROSS ST PANCRAS"

    if start not in graph or finish not in graph:
        return "Error"

    distance_dict = {}
    predecessor_dict = {}
    shortest_route = []

    for key in graph:
        distance_dict.update({key: 999999})
        predecessor_dict.update({key: ''})

    distance_dict[start] = 0

    cursor = start

    while finish in distance_dict:

        for key, val in graph[cursor].items():
            if key in distance_dict:
                if distance_dict[key] > distance_dict[cursor] + val:
                    distance_dict[key] = distance_dict[cursor] + val
                    predecessor_dict[key] = cursor
                #print(key, distance_dict[key])            

        if cursor == finish:
            travel_time = distance_dict[cursor]

        distance_dict.pop(cursor)

        cursor = min(distance_dict, key=distance_dict.get)

    cursor = finish

    while start not in shortest_route:
        shortest_route.append(cursor)
        cursor = predecessor_dict[cursor] 

    shortest_route.reverse()

    travel_time = int(round(travel_time, 0))

    """for k, v in predecessor_dict.items():
        print(k, 'P: ' + v)"""

    return shortest_route, travel_time

