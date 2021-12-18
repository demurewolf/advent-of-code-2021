#!/usr/bin/env python3.8

#file_name = "test-input.txt"
file_name = "puzzle-input.txt"

days_to_watch = 18
days_to_watch = 80

lantern_fish = []

with open(file_name) as fish_file:
	lantern_fish_tmp = fish_file.readline().split(',')
	lantern_fish_tmp[-1] = lantern_fish_tmp[-1].rstrip()
	lantern_fish = [int(i) for i in lantern_fish_tmp]

print(f"Initial State: {lantern_fish}")

for day in range(1, days_to_watch+1):
	new_lantern_fish = []
	fish_to_add = []

	for fish in lantern_fish:
		if fish > 0:
			new_fish = fish - 1
			new_lantern_fish.append(new_fish)

		elif fish == 0:
			new_fish = 6
			new_lantern_fish.append(new_fish)
			fish_to_add.append(new_fish + 2)


	for fish in fish_to_add:
		new_lantern_fish.append(fish)

	lantern_fish = new_lantern_fish

	#print(f"After	{day} days: {lantern_fish}")

print(f"After {day} days, there are {len(lantern_fish)} lanternfish")