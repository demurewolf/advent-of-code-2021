#!/usr/bin/env python3.8

def make_deep_copy(data):
    copy_data = [item for item in data]
    return copy_data

def find_most_common_bits(data, position=0):
    ones = 0
    zeros = 0

    # Find most common bit in binary data for position pos
    for bin_num in data:
        if bin_num[position] == '1':
            ones += 1
        else:
            zeros += 1

    # O2: Determine most common bit value, and keep only numbers with that bit in position pos. If 0 and 1 are equal, keep values with 1 in pos.
    # CO2: Determine the least common bit value and keep only numbers with that bit in position pos. If 0 and 1 are equal, keep values with 0 in pos.

    if ones >= zeros:
        return ('1', '0')
    else:
        return ('0', '1')


#input_file = "test-input.txt"
input_file = "puzzle-input.txt"

oxygen_rating_bin = ''
carbon_diox_rating_bin = ''


with open(input_file) as bin_file:
    data = bin_file.readlines()

    # Remove trailing newline from all memebers
    bin_data = list(map(lambda x: x.rstrip(), data))
    bin_length = len(bin_data[0])

    ox_nums = bin_data
    co2_nums = make_deep_copy(bin_data)

    for pos in range(bin_length):
        
        ox_filter_bit = ''
        co2_filter_bit = ''

        ox_nums_tmp = []
        co2_nums_tmp = []    

        print(f"position: {pos}")

        ox_filter_bit, _ = find_most_common_bits(ox_nums, pos)
        _, co2_filter_bit = find_most_common_bits(co2_nums, pos)

        print(f"ox_nums: {ox_nums}, filtering for {ox_filter_bit}")
        print(f"co2_nums: {co2_nums}, filtering for {co2_filter_bit}")

        for bin_num in ox_nums:
            if bin_num[pos] == ox_filter_bit:
                ox_nums_tmp.append(bin_num)
        
        for bin_num in co2_nums:
            if bin_num[pos] == co2_filter_bit:
                co2_nums_tmp.append(bin_num)

        ox_nums = ox_nums_tmp
        co2_nums = co2_nums_tmp

        if len(ox_nums) == 1:
            oxygen_rating_bin = ox_nums[0]
        elif len(co2_nums) == 1:
            carbon_diox_rating_bin = co2_nums[0]
        


print(f"Binary O2: {oxygen_rating_bin}")
print(f"Binary CO2: {carbon_diox_rating_bin}")

o2 = int(oxygen_rating_bin, base=2)
co2 = int(carbon_diox_rating_bin, base=2)

print(f"O2 generator rating: {o2}")
print(f"CO2 scrubber rating: {co2}")

life_support = o2 * co2

print(f"Life support rating: {life_support}")