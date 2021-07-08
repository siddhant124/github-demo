#Add header
def add(x,y):
	pass
#sub header
def sub(x,y):
	return x-y
#mul header
def multiply(x,y):
	return x*y
#div header
def devide(x,y): #div fun on bug789 branch
	if y==0:
        return DIVIDE_BY_ZERO_ERROR
    else:
        return x/y

#Square implementation
def square(x):
    return x*x