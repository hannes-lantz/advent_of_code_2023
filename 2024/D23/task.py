from collections import defaultdict

def read_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f.readlines()]

def build_graph(connections):
    graph = defaultdict(set)
    for conn in connections:
        a, b = conn.split("-")
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_interconnections(graph):
    sets_of_three = set()
    for node in graph:
        for neighbor in graph[node]:
            if node < neighbor:
                common_neighbors = graph[node] & graph[neighbor]
                for common in common_neighbors:
                    trio = tuple(sorted([node, neighbor, common]))
                    sets_of_three.add(trio)

    return sets_of_three

def filter_by_t(sets_of_three):
    return [trio for trio in sets_of_three if any(computer.startswith('t') for computer in trio)]

def bron_kerbosch(r, p, x, graph, cliques):
    if not p and not x:
        cliques.append(r)
        return
    for v in list(p):
        bron_kerbosch(r.union([v]), p.intersection(graph[v]), x.intersection(graph[v]), graph, cliques)
        p.remove(v)
        x.add(v)

def find_largest_clique(graph):
    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
    largest_clique = max(cliques, key=len)
    return sorted(largest_clique)

def main():
    input = read_input('input.txt')
    graph = build_graph(input)

    set_of_three = find_interconnections(graph)
    largest_clique = find_largest_clique(graph)
    password = ",".join(largest_clique)

    print(f"P1: {len(filter_by_t(set_of_three))}")
    print(f"P2: {password}")

if __name__ == "__main__":
    main()
