#Task 3: multiply this matrix with the first MNIST digit vector 
#        (which you should rescale first to lie between 0.01 and 1)
 

#rescale first:
scaled_input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
#scaled_input[0:10]
inputs = numpy.array(scaled_input, ndmin=2).T
inputs.shape #(784,1)
wih.shape #(100, 784)
hidden_inputs = numpy.dot(wih, inputs)
