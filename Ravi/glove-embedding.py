# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:22:28 2019

@author: Ravi
"""

%reset

from numpy import asarray
from numpy import zeros
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding

# define documents
docs = ['Well done!',
        'Good work',
        'Great effort',
        'nice work',
        'Excellent!',
        'Weak',
        'Poor effort!',
        'not good',
        'poor work',
        'Could have done better.']

# define class labels
labels = [1,1,1,1,1,0,0,0,0,0]

########################################################
# this is new...
# we are going to add our own words to the embedding

# prepare tokenizer
t = Tokenizer()

t.fit_on_texts(docs)
vocab_size = len(t.word_index) + 1
vocab_size  # 15

# integer encode the documents
encoded_docs = t.texts_to_sequences(docs)
print(encoded_docs)

# pad documents to a max length of 4 words
max_length = 4
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
print(padded_docs)

# load the whole glove100 embedding into memory
embeddings_index = dict()
f = open('glove.6B/glove.6B.100d.txt', mode='rt', encoding='utf-8')

for line in f:
    values = line.split()
    word = values[0]
    coefs = asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Loaded %s word vectors.' % len(embeddings_index))

# create a weight matrix of zeros for words in training docs
embedding_matrix = zeros((vocab_size, 100))
embedding_matrix

# and we now want to fill in the weights from the GloVe vectors 
for word, i in t.word_index.items():
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector

embedding_matrix

# we are done getting our word vectors from the glove100 embedding
######################################################################
        
model = Sequential()
e = Embedding(vocab_size, 100, weights=[embedding_matrix], input_length=4, trainable=False)
model.add(e)
model.output_shape
model.add(Flatten())
model.output_shape

model.add(Dense(1, activation='sigmoid'))

# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
# summarize the model
model.summary()
# fit the model
model.fit(padded_docs, labels, epochs=50, verbose=0)
# evaluate the model
loss, accuracy = model.evaluate(padded_docs, labels, verbose=0)
print('Accuracy: %f' % (accuracy*100))



