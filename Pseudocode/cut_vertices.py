time = 0
visited_nodes = set()

def cut_vertices(graph):
    nodes = graph.nodes()
    for node in graph.nodes():
        node.color = 'white'
    while nodes:
        time = 0
        root = nodes.pop()
        root.previous = None
        # Check if the root of a DFS tree is a cut vertices
        root_children = {root_child
                         for node in visited_nodes
                         if node.previous = root}
        if len(root_children) > 1:
            print("{} is a cut vertices".format(root))
        # Remove visited nodes
        nodes.remove(visited_nodes)

def dfs(node):
    node.color = 'gray'
    visited_nodes.add(node)
    time += 1
    node.low = node.time_discovered = time
    for neighbour in node.neighbours():
        if neighbour.color = 'white':
            neighbour.previous = node;
            dfs(neighbour)
            node.low = min(node.low, neighbour.low)
            if node.time_discovered > 1 and
               neighbour.low >= node.time_discovered:
                print("{} is a cut vertices".format(node))
        elif neighbour != node.previous:
            node.low = min(node.low, neighbour.time_discovered)
    node.color = 'black'
