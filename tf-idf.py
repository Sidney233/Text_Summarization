import numpy as np
tf = np.load(file="tf.npy")
idf = np.load(file="idf.npy")
word = np.load(file="word.npy")
i = 0
for p in tf:
    i = i + 1
    print(i)
    for w in p:
        index = np.where(word == w)
        p[w] = p[w] * idf[index]
np.save(file="tfidf", arr=tf)
