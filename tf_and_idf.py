import numpy as np
import jieba
word = np.load(file="word.npy")
passages = np.load(file="passages.npy")
tf = []
idf = np.zeros(np.shape(word))
i = 0
for passage in passages:
    i = i + 1
    print(i)
    tf_p = {}
    j = 0
    lenth = 0
    wp = set()
    for sentence in passage:
        for ws in sentence:
            if ws in word:
                if ws in tf_p:
                    tf_p[ws] = tf_p[ws] + 1
                else:
                    tf_p[ws] = 1
                if ws not in wp:
                    index = np.where(word == ws)
                    idf[index] = idf[index] + 1
            wp.add(ws)
        lenth = lenth + len(sentence)
    for key in tf_p:
        tf_p[key] = tf_p[key] / lenth
    tf.append(tf_p)
    print(tf_p)
idf = np.log10(500/idf)
tf = np.asarray(tf)
np.save(file="idf", arr=idf)
np.save(file="tf", arr=tf)
