def gender_features(word):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

classifier.classify(gender_features('Nemo'))
classifier.classify(gender_features('Thor'))

print(nltk.classify.accuracy(classifier, test_set))

print(classifier.show_most_informative_features(5)