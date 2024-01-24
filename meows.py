import argparse

parser = argparse.ArgumentParser("meows")

# -n
parser.add_argument("-n", "--number", type=int, default=1,help="number of meows")

args = parser.parse_args()

for i in range(args.number):
	print("meow")