# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:56:51 2019

@author: Ravi
"""


from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.embeddings import Embedding

# define documents and sentiments
# open the file 'school_q7_train.txt' and 
# read in all the lines



# good to do strip leading, training white space from lines (optional)
 

# now extract the content and the sentiment ('pos' or 'neg'):


# now separate the reponse and the sentiment ('pos' or 'neg')
# into two lists called docs and sentiment respectively


# finally, create a list called labels,
# with code 'pos' as 1 and 'neg' as 0


# done preparing the data


# integer encode the documents
vocab_size = 5000  # just a large number!
encoded_docs = [one_hot(d, vocab_size) for d in docs]
print(encoded_docs)

# pad documents to a max length of 4 words
max_length = 40  # guessed this 
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
print(padded_docs)

# define the model
model = Sequential()
model.input_shape
model.output_shape

# Embedding(input_dim, output_dim, input_length)
model.add(Embedding(vocab_size, 50, input_length=max_length))
model.input_shape  # is the input_length
model.output_shape  # is the output_dim

model.add(Flatten())
model.input_shape  # is the input_length
model.output_shape

model.add(Dense(1, activation='sigmoid'))

# compile the model
model.compile(optimizer='adam', 
              loss='binary_crossentropy', 
              metrics=['acc'])

# summarize the model
model.summary()
# fit the model
model.fit(padded_docs, labels, epochs=50, verbose=0)
# evaluate the model
loss, accuracy = model.evaluate(padded_docs, labels, verbose=0)
print('Accuracy: %f' % (accuracy*100))


###################################################################

# but now predict on the test data!

# read in the lines in the 'school_q7.txt' file into a list


# good to do strip leading, training white space from lines (optional) 


# done reading in content

vocab_size = 5000
encoded_docs2 = [one_hot(d, vocab_size) for d in docs2]
print(encoded_docs2)

# pad documents to a max length of 4 words
max_length = 40  # guessed this 
padded_docs2 = pad_sequences(encoded_docs2, maxlen=max_length, padding='post')
print(padded_docs2)

pred = model.predict_classes(padded_docs2)
pred

# now count the zeros and ones (negative and positive sentiments):


# so more respondents expressed a positive sentiment than negative

#########################################################














