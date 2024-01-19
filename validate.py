import re


email = input("Enter your email address: ").strip()

# check if email is valid use regex
# regex is a sequence of characters that define a search pattern
# \w matches any alphanumeric character
# \d matches any digit
# + matches one or more of the preceding character
# \. matches the period character
# {2,4} matches between 2 and 4 of the preceding character
# $ matches the end of the string

regex = re.compile(r"[\w\d\.\+]{1,64}@[\w\d\.\+]{1,255}\.[\w]{2,4}$")

if regex.match(email):
	print("Valid email")
else:
	print("Invalid email")