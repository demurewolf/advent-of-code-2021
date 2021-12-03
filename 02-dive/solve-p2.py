#!/usr/bin/env python3.8

#input_file = "test-input.txt"
input_file = "puzzle-input.txt"

horizontal_pos = 0
depth_pos = 0
aim_pos = 0

with open(input_file) as commands:
    for c in commands:
        dir, mag_str = c.split()
        mag = int(mag_str)

        if dir == 'forward':
            horizontal_pos += mag
            depth_pos += (aim_pos * mag)
        else:
            if dir == 'up':
                aim_pos -= mag
            elif dir == 'down':
                aim_pos += mag
            else:
                raise KeyError(f"No direction suitable for {dir}")

print(f"Horizontal Pos: {horizontal_pos}")
print(f"Depth Position: {depth_pos}")
print(f"Area of displacement: {horizontal_pos * depth_pos}")