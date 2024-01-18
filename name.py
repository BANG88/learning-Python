import sys

def main():
	hello()

	sys.exit(0)

def hello():
    if len(sys.argv) < 2:
     print("Usage: python name.py <name>")

    elif len(sys.argv) > 2:
     print("Usage: python name.py <name>")

    else:
     print("Hello, " + sys.argv[1] + "!")

for a in sys.argv[2:]:
    print(a)

main()