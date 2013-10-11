def tree_reverse(a):
	a.reverse()
	print a 
	for i in a:
		if isinstance(i,list):
			tree_reverse(i)
	#print a
tree_reverse([[1, 2], [3, [4, 5]], 6])

