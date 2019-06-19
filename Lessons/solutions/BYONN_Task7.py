#Task 7: run a simple query:

#number of input, hidden and output nodes
input_nodes = 3
hidden_nodes = 3
output_nodes = 3

# learning rate is 0.3
learning_rate = 0.3

# create instance of neural network
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)

# test query (doesn't mean anything useful yet)
input=[1.0, 0.5, -1.5]
n.query(input)
