def three_color(nodes):
    colors = {'red', 'green', 'blue'}
    return {node: random(colors) | for node in nodes}
