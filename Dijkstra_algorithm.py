#Dijkstra_algorithm.py
def find_lowest_cost_node(costs):
	"""找到最小开销节点"""
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost_node = node
	return lowest_cost_node

#绘制图表
graph = {
		'start': {'a': 6, 'b': 2},
		'a': {'fin': 1},
		'b': {'a': 3, 'fin': 5},
		'fin': {}
}
#print(graph['start'].keys())
#print(graph['start']['a'])

#创建开销表
infinity = float('inf')
costs = {
		'a': 6,
		'b': 2,
		'fin': float('inf'),
}

#创建父节点
parents = {
		'a': 'start',
		'b': 'start',
		'fin': None
}

#创建存储处理过的散列表
processed = []

#狄克斯特拉算法代码
node = find_lowest_cost_node(costs)#未处理的节点中找出开销最小的
while node is not None:#当所有节点都被处理过后结束
	cost = costs[node]#储存当前节点的开销
	neighbors = graph[node]#找出当前节点的邻居
	for n in neighbors.keys():#遍历该节点的邻居
		new_cost = cost + neighbors[n]#计算抵达邻居的开销
		if costs[n] > new_cost:#任何不与当前节点直接连接的节点，其开销皆为无穷大*****
			costs[n] = new_cost
			parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)

print(parents)