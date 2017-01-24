#global and local variable
x = 5  #defining x(at tis point it is a local variable)

def example():
	z = 10 
	print('the value of z',z)
	pass
def example2():
	globx = x   #assigning a proxy variable to x
	print(globx)
	globx+=globx
	print(globx)
	return globx # now it returns a value to the rest of the program , other subsactions can you globx value
	pass
def example3():
	global x #defining x to be a global variable 
	print(x)
	print(x+5)
	pass
example()
example2()
x = example2()
print(x)
example3()