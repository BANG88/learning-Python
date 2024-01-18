from calculator import square
import pytest

def test_square():
	assert square(1) == 1
	assert square(2) == 4
	assert square(3) == 9
	assert square(4) == 16
	assert square(5) == 25