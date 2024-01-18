from calculator import square
def main():
	test_square()

def test_square():
	if square(2) != 4:
		print('square(2) did not return 4')
	assert square(3) == 91


if __name__ == '__main__':
	main()