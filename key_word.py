import numpy as np
key = []
tfidf = np.load(file="tfidf.npy")
for p in tfidf:
    p_list = sorted(p, key=lambda item: item[1], reverse=True)
    top_5 = p_list[:5]
    key.append(top_5)
key = np.asarray(key)
np.save(file="key_word", arr=key)
