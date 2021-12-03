#!/usr/bin/env python3.8

#input_file = 'test-input.txt'
input_file = 'puzzle-input.txt'

depth_orig = None
depth_next = None
depth = ''

increases = 0
decreases = 0

with open(input_file) as depth_data:
    print("opened file...")

    depth = depth_data.readline()
    depth_orig = int(depth)

    while (depth != ''):
        depth_next = int(depth)

        if depth_next > depth_orig:
            increases += 1
        elif depth_next < depth_orig:
            decreases += 1

        depth_orig = depth_next
        depth = depth_data.readline()

print(f"Found {increases} increases from the report")
print(f"Found {decreases} decreases from the report")