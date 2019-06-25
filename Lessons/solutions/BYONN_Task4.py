#Task 4: unusual matrix multiplication: 
# 1. create a column vector x which is simply the sequence 1:5
# 2. compute the dot product of x with its transpose 

x = numpy.linspace(1, 5,num=5)
#for kicks: inner product
numpy.dot(x,x)
#"outer product"
numpy.dot(x.reshape(5,1),x.reshape(1,5))