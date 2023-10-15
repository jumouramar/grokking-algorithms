'''
PT-BR PSEUDOCODE!

1. Procure o vértice com custo mais baixo.*
2. Enquanto existe vértice com custo menor que infinito:
    a. Mapeie os vizinhos.
    b. Para todos os vizinhos:
        1. Calcule qual seria o custo de chegar naquele vizinho a partir do custo de chegar no vértice atual.
        2. Se o custo for menor que o atual:
            a. Troca o custo pelo novo calculado.
            b. Troca o pai do vizinho pelo vértice atual.
    c. Adicione o vértice em 'processados'.
    d. Procure próximo vértice com custo mais baixo.*

    
* FUNÇÃO find_lowest_code_node
1. Para todos os nós:
    a. Se o custo for menor que infinito e ainda não foi processado:
        1. Substitui o menor custo por esse. 
2. Retorna menor custo (Será None se não achar outro).

'''

# the graph
graph = {
    'START': {'A': 6, 'B': 2},
    'A': {'END': 1},
    'B': {'A': 3, 'END': 5},
    'END': {}
}

# the costs table
costs = {
    'A': 6,
    'B': 2,
    'END': float("inf")
}

# the parents table
parents = {
    'A': 'START',
    'B': 'START',
    'END': None
}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Find the lowest-cost node that you haven't processed yet.
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            parents[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)