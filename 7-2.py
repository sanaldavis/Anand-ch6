def flatten_dict(a):
	result={}
	for x,y in a.items():
		if isinstance(y,dict):
			for p,q in y.items():
				print x+'.'+p,q
				result[x+'.'+p]=q
		else:
			print x,y
			result[x]=y
	print result

flatten_dict({'a':1,'b':{'c':2,'d':3},'e':4})

