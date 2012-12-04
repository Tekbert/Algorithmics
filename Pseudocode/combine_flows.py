
for (node1, node2) in arcs:
    if flow(node1, node2) > upper_capacity(node1, node2):
        overflow = f(node1, node2) - \
                   upper_capacity(node1, node2)
        flow(node1, node2) -= overflow
        flow(node2, node1) -= overflow
