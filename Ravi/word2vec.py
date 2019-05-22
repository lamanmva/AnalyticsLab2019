from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

sentences = [["this", "is", "the", "first", "sentence", "for", "word2vec"],
            ["this", "is", "the", "second", "sentence"],
            ["one", "more", "sentence"],
            ["and", "the", "final", "sentence"]]
			
			
model = Word2Vec(sentences, min_count=1)

X = model[model.wv.vocab]

pca = PCA(n_components=2)
result = pca.fit_transform(X)