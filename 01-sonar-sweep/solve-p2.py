#!/usr/bin/env python3.8

#input_file = 'test-input.txt'
input_file = 'puzzle-input.txt'

depth_sum = None
depth_sum_next = None
depth_data = []

increases = 0
decreases = 0

with open(input_file) as depth_file:
    print("opened file...")
    depth_data = depth_file.readlines()
    
for i in range(len(depth_data)):
    depth_data[i] = int(depth_data[i])

groups = [0] * (len(depth_data) - 2)

for i in range(len(depth_data) - 2):
    try:
        groups[i] = (depth_data[i], depth_data[i+1], depth_data[i+2])
    except Exception as e:
        print(f"Couldn't make tuple for key {i}, going to stop reading.")
        e.print_exc()
        break

print(groups)

for g in groups:
    depth_sum_next = sum(g)

    try:
        if depth_sum_next > depth_sum:
            increases += 1
            print(f"{depth_sum_next} (increased)")
        elif depth_sum_next < depth_sum:
            decreases += 1
            print(f"{depth_sum_next} (decreased)")
        else:
            print(f"{depth_sum_next} (no change)")

    except Exception as e:
        print(f"{depth_sum_next} (N/A, no previous sum)")

    depth_sum = depth_sum_next
#     while (depth != ''):
#         depth_next = int(depth)

#         if depth_next > depth_orig:
#             increases += 1
#         elif depth_next < depth_orig:
#             decreases += 1

#         depth_orig = depth_next
#         depth = depth_data.readline()

print(f"Found {increases} increases from the report")
print(f"Found {decreases} decreases from the report")