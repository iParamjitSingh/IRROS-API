import osmnx as ox
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from route import constructGraph


def getRoute(src, dest, per, user):
    G = constructGraph(user)
    nodes, edges = ox.graph_to_gdfs(G)

    src_gcord = ox.geocoder.geocode(src)
    dest_gcord = ox.geocoder.geocode(dest)

    # Testing
    print('source: ', src_gcord)
    print('destination: ', dest_gcord)

    # Nearest OSMNx node wrt Address
    origin = ox.nearest_nodes(G, src_gcord[1], src_gcord[0], return_dist = True)
    destination = ox.nearest_nodes(G, dest_gcord[1], dest_gcord[0], return_dist = True)

    if per == True:
        route = ox.routing.shortest_path(G, origin[0], destination[0], weight='Total_Cost')
    else:
        route = ox.routing.shortest_path(G, origin[0], destination[0], weight='length')

    fig, ax = ox.plot_graph_route(G, route, route_color='blue', route_linewidth=10, figsize=(30, 30), edge_color='black', node_color='black', bgcolor='white', edge_linewidth=1, node_size=0.5)
    return fig