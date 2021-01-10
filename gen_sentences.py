import jieba
import numpy as np
path = "C:/Users/123/PycharmProjects/Text_Summarization/Text_Summarization/data/"
word = set()
passages = []
for i in range(500):
    path_txt = path+str(i)+".txt"
    f = open(path_txt, "r", encoding="utf-8")
    passage = []
    title = f.readline()
    paragraph = f.readline()
    title = list(jieba.cut(title))
    for i in title:
        if len(i) > 1:
            word.add(i)
    passage.append(title)
    paragraph = paragraph.split("。")
    for sentence in paragraph:
        sentence = list(jieba.cut(sentence))
        for i in sentence:
            if len(i) > 1:
                word.add(i)
        passage.append(sentence)
    passages.append(passage)
passages = np.asarray(passages)
word = list(word)
word = np.asarray(word)
np.save(file="passages", arr=passages)
np.save(file="word", arr=word)
