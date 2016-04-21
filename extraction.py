import nltk

def mascom(texto, cant=10):
	tokens = nltk.word_tokenize(texto)
	sinsw = [word for word in tokens if word.isalpha() and word not in nltk.corpus.stopwords.words('spanish')]
	stemmer = nltk.stem.snowball.SpanishStemmer(ignore_stopwords=True)
	stemmed = [stemmer.stem(word) for word in sinsw]
	fd = nltk.FreqDist(stemmed)
	return fd.most_common(cant)
