def square(x):
	return x*x

def vector(square):
	def findsquare(x):
		result=[]
		for i in x:
			result.append(square(i))
		print result	

	return findsquare
	
def vectorize(length):
	def  findlen(x):
		result=[]
		for i in x:
			result.append(length(i))
		return result		

	return findlen 


f = vector(square)
f([1, 2, 3])


f=vectorize(len)
a=f([[1,2,3],[1,2]])
print a
a=f(["hello", "world"])
print a

