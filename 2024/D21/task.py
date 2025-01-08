from collections import defaultdict, deque
from math import inf

def read_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

numpad = {
	'A': ('0<', '3^'),
	'0': ('A>', '2^'),
	'1': ('2>', '4^'),
	'2': ('0v', '1<', '3>', '5^'),
	'3': ('Av', '2<', '6^'),
	'4': ('1v', '5>', '7^'),
	'5': ('2v', '4<', '6>', '8^'),
	'6': ('3v', '5<', '9^'),
	'7': ('4v', '8>'),
	'8': ('5v', '7<', '9>'),
	'9': ('6v', '8<'),
}

dirpad = {
	'A': ('>v', '^<'),
	'^': ('A>', 'vv'),
	'<': ('v>',),
	'>': ('v<', 'A^'),
	'v': ('<<', '>>', '^^'),
}

def serch_all_paths(g, src, dst, cache={}):
	k = src, dst
	if k in cache:
		return cache[k]

	queue = deque([(src, '')])
	distance = defaultdict(lambda: inf, {src: 0})
	paths = []

	while queue:
		node, path = queue.popleft()
		if node == dst:
			paths.append(path)
			continue

		for neighbor, direction in g[node]:
			d = distance[node] + 1
			if d > distance[dst] or d > distance[neighbor]:
				continue

			distance[neighbor] = d
			queue.append((neighbor, path + direction))

	cache[k] = paths
	return paths


def solve(pad, code, robot, cur='A', cache={}):
	if not code:
		return 0

	k = code, robot, cur
	if k in cache:
		return cache[k]

	nxt = code[0]
	paths = serch_all_paths(pad, cur, nxt)

	if robot == 0:
		best = len(paths[0]) + 1
	else:
		best = min(solve(dirpad, p + 'A', robot - 1) for p in paths)

	res = cache[k] = best + solve(pad, code[1:], robot, nxt)
	return res


def main():
    total1 = total2 = 0
    codes = read_input('input.txt')
    for code in codes:
        num = int(code[:-1])
        total1 += num * solve(numpad, code, 2)
        total2 += num * solve(numpad, code, 25)

    print('Part 1:', total1)
    print('Part 2:', total2)

if __name__ == "__main__":
    main()