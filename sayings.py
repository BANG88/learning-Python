import cowsay

def main():
	hello('Fred')
	goodbye('Fred')
	hello('Wilma')
	goodbye('Wilma')

def hello(name):
	print(cowsay.cow('Hello, ' + name))

def	goodbye(name):
	print(cowsay.cheese( 'Goodbye, ' + name))

if __name__ == '__main__':
	main()