#greedy_algorithm.py
"""集合覆盖问题"""
from time import sleep
states_needed = set(["mt", "wa", "or", "id",
		"nv", "ut", "ca", "az"])

stations = {}
stations['kone'] = set(["id", "nv", "ut"])
stations['ktwo'] = set(["wa", "id", "mt"])
stations['kthree'] = set(["or", "nv", "ca"])
stations['kfour'] = set(["nv", "ut"])
stations['kfive'] = set(["ca", "az"])
final_stations = set()

while states_needed:
	best_station = None
	state_covered = set()
	covered = set()
	for station, states in stations.items():
		covered = states & states_needed#避免了每次选州时，都重复选择已出现过的广播台 #思考一下若此处没有并集，为什么会导致无限循环
		if len(covered) > len(state_covered):
			best_station = station
			state_covered = covered
	final_stations.add(best_station)
	states_needed -= state_covered
print(final_stations)
	








