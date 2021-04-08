import tube_network


def shortest_time(start, finish):
    graph = tube_network.network
    start = start.upper()
    finish = finish.upper()
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
            print(distance_dict[cursor])

        distance_dict.pop(cursor)

        cursor = min(distance_dict, key=distance_dict.get)

    cursor = finish

    while start not in shortest_route:
        shortest_route.append(cursor)
        cursor = predecessor_dict[cursor] 

    shortest_route.reverse()

    """for k, v in predecessor_dict.items():
        print(k, 'P: ' + v)"""

    print(shortest_route) 

    





