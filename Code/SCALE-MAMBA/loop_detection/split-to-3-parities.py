import sys
import random

def split_numbers(num1, num2):
    nums1 = random.sample(range(1, num1), 2)
    nums2 = random.sample(range(1, num2), 2)
    nums3 = [num1 - nums1[0] - nums1[1], num2 - nums2[0] - nums2[1]]
    return nums1, nums2, nums3

# Check if the input file path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the input file path as a command-line argument.")
    sys.exit(1)

# Input and output file paths
input_file = sys.argv[1]
output_files = ["in.1", "in.2", "in.3"]

with open(input_file, 'r') as file:
    lines = file.readlines()

for output_file in output_files:
    with open(output_file, 'w') as file:
        for line in lines:
            num1, num2 = map(int, line.split())
            nums1, nums2, nums3 = split_numbers(num1, num2)
            file.write(' '.join(map(str, nums1 + nums2)) + '\n')

