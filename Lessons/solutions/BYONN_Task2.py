#Task 2: initialize one random (normally distributed) matrix pxn, 
#       where n=748 and p = 100 
# wih = 

#rescale first:
#scaled_input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01

wih = numpy.random.normal(0.0, 1, (100, 784))
#advanced version:
wih = numpy.random.normal(0.0, pow(784, -0.5), (100, 784))