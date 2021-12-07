#!/usr/bin/env python3.8


#input_file = "test-input.txt"
input_file = "puzzle-input.txt"

gamma_bin = ''
epsilon_bin = ''

with open(input_file) as bin_file:
    data = bin_file.readlines()

    # Remove trailing newline from all memebers
    bin_data = list(map(lambda x: x.rstrip(), data))
    bin_length = len(bin_data[0])

    for pos in range(bin_length):
        
        # Find most common bit in bin_num
        ones = 0
        zeros = 0

        for bin_num in bin_data:
            if bin_num[pos] == '1':
                ones += 1
            else:
                zeros += 1

        print(f"Pos: {pos}, ones = {ones}, zeros = {zeros}")

        # Add the most common bit to gamma_bin
        # Add the leaset common bit to epsilon_bin
        if ones > zeros:
            gamma_bin += '1'
            epsilon_bin += '0'
        else:
            gamma_bin += '0'
            epsilon_bin += '1'

print(f"Binary gamma: {gamma_bin}")
print(f"Binary epsilon: {epsilon_bin}")

gamma = int(gamma_bin, base=2)
epsilon = int(epsilon_bin, base=2)

print(f"Gamma rate: {gamma}")
print(f"Epsilon rate: {epsilon}")

power = gamma * epsilon

print(f"Power consumption: {power}")