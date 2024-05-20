import osmnx as ox
import requests
import pandas as pd


params = [
    'Crime_Locations',
    'CCTV_Cameras',
    'Speed_Limit',
    'Traffic_Delay',
    'Road_Condition',
    'Street_Lights',
    'Road_Width',
    'Traffic_Lights',
    'Number_of_Lanes',
    'Road_Length'
]


def constructGraph(user):
    G = ox.graph_from_place("Gurgaon, Gurugram District, Haryana, India", network_type="drive")
    nodes, edges = ox.graph_to_gdfs(G)

    if user == 1:
        df = pd.read_csv('User/U1.csv')
    else:
        df = pd.read_csv('User/U2.csv')

    total_cost = df['Total_Cost'].tolist()

    print('Top 5 entries: ', total_cost[:5])
    print('Length of total_cost: ', len(total_cost))
    print('EdgeDF Shape: ', edges.shape)
    print('OSMNX v: ',ox.__version__)

    edges['Total_Cost'] = total_cost
    G = ox.graph_from_gdfs(nodes, edges, graph_attrs=G.graph)
    return G
