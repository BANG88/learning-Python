def f(*args,**kwargs):
	print("Positional: ", args)
	print("Keyword: ", kwargs)


f(1, 2, 3, 4, 5,a=2,b=3,c=4,d=5)