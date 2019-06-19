#Task 5a: 


#10 output nodes, label 2 (example)
onodes = 10
label=2
targets = numpy.zeros(onodes) + 0.01
targets[int(all_values[label-1])] = 0.99