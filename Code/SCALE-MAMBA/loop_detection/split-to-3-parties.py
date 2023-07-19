import sys
import random

def split_number(num):
    num1 = random.randint(1, num-2)
    num2 = random.randint(1, num-num1-1)
    num3 = num - num1 - num2
    return num1, num2, num3

# Check if the input file path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the input file path as a command-line argument.")
    sys.exit(1)

# Input and output file paths
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    lines = file.readlines()

out1 = open('in.1', "w")
out2 = open('in.2', "w")
out3 = open('in.3', "w")

for line in lines:
   num1, num2 = map(int, line.split())
   split1 = split_number(num1)
   split2 = split_number(num2)
   out1.write(str(split1[0]) + " " + str(split2[0])+'\n')
   out2.write(str(split1[1]) + " " + str(split2[1])+'\n')
   out3.write(str(split1[2]) + " " + str(split2[2])+'\n')


out1.close()
out2.close()
out3.close()

