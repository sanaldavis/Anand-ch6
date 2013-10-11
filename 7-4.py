def treemap(f,a):
	for i in range(len(a)):
		if isinstance(a[i],list):
			print a[i]
			treemap(f,a[i])
		else:
			re=f(a[i])
			a.remove(a[i])
			a.insert(i,re)
	return a

print treemap(lambda x:x*x,[1,2,[3,4,[5]]])
