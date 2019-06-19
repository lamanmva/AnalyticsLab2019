#Task 0: Plot this rectangular array of numbers using the imshow() function
import matplotlib.pyplot
# take the data from a record, rearrange it into a 28*28 array and plot it as an image
all_values = training_data_list[0].split(',')
image_array = numpy.asfarray(all_values[1:]).reshape((28,28))
matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')