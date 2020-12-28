from time import time

import networkx as nx

def parse_rule(rule):
    if 'other' in rule:
        return False
    start_node, tmp = rule.replace('.','').replace(' bags','').replace(' bag','').split(' contain ')
    tmp = tmp.split(', ')
    nodes = [i for i in range(len(tmp))]
    weights = [i for i in range(len(tmp))]
    for i in range(len(tmp)):
        weights[i], nodes[i] = tmp[i].split(' ',1)

    start_node = [start_node for i in range(len(nodes))]
    weighted_edges = list(zip(start_node, nodes, weights))

    return weighted_edges 

def construct_graph(rules):
    graph = nx.DiGraph()
    
    for rule in rules:
        weighted_edges = parse_rule(rule)
        if not weighted_edges:
            continue
        graph.add_weighted_edges_from(weighted_edges)

    return graph

def dfs(G, curr_node, parent=None):
    node_value = 0
    children = nx.descendants_at_distance(G,curr_node,1)

    for child in children:
        weight = int(graph[curr_node][child]['weight'])
        node_value += weight + weight * dfs(G, child, curr_node)
        
    if children == set():
        return 0
    return node_value
rules = open('input.txt').read().split('\n')

t0 = time()

graph = construct_graph(rules)

number_of_paths = 0

for node in graph.nodes:
    paths = list(nx.all_simple_paths(graph, node, 'shiny gold'))
    if len(paths) != 0:
        number_of_paths += 1

print(number_of_paths)
print(time() - t0)

# Part 2
t1 = time()
print(dfs(graph, 'shiny gold'))
print(time() - t1)