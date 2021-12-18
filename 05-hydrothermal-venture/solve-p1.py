#!/usr/bin/env python3.8


#file_name = "test-input.txt"
file_name = "puzzle-input.txt"

# Dictionary will be a mapping of 
# Tuples -> integer
# (x1, y1) -> collision_count
collisions = {}

with open(file_name) as data_file:
	for line in data_file:
		tmp = line.split(' -> ')
		if len(tmp) == 2:
			tmp_p1 = tmp[0]
			tmp_p2 = tmp[1].rstrip()

			tmp = tmp_p1.split(',')
			x1 = int(tmp[0])
			y1 = int(tmp[1])

			tmp = tmp_p2.split(',')
			x2 = int(tmp[0])
			y2 = int(tmp[1])

			x_diff = x2 - x1
			y_diff = y2 - y1

			if y_diff == 0:
				# Horizontal line
				if x1 > x2: # Force x2 to always be > x1
					tmp = x1
					x1 = x2
					x2 = tmp

				for x in range(x1, x2+1):
					p = (x, y1) # Either y will work
					if p in collisions:
						collisions[p] += 1
					else:
						collisions[p] = 1


			elif x_diff == 0:
				# Vertical line
				if y1 > y2:
					tmp = y1
					y1 = y2
					y2 = tmp

				for y in range(y1, y2+1):
					p = (x1, y)
					if p in collisions:
						collisions[p] += 1
					else:
						collisions[p] = 1


	#print(f"Collisions hash: {collisions}")
	danger_count = 0
	for p in collisions:
		if collisions[p] >= 2:
			danger_count += 1

	print(f"Danger Count: {danger_count}")