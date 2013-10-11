import itertools
per=[]
a=itertools.permutations([1,2,3])
for i in a:
	print i
	per.append(list(i))
print per
