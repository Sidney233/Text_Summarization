import numpy as np
key = np.load(file="key_word.npy")
passages = np.load(file="passages.npy")
f = open("C:/Users/123/PycharmProjects/Text_Summarization/Text_Summarization/data/summary.txt", "w", encoding="utf-8")
j = 0
for passage in passages:
    summary = []
    need_cover = key[j]
    while len(need_cover) > 0:  # 直到所有关键词被覆盖
        max_cover = 0
        max_num = -1
        one_cover = [0 for i in range(len(passage))]
        all_cover = []
        for i in range(0, len(passage)):  # 遍历所有句子
            cover = []
            for keyword in need_cover:  # 计算每一句覆盖的关键词
                if keyword in passage[i]:
                    one_cover[i] += 1
                    cover.append(keyword)
            all_cover.append(cover)
            if one_cover[i] > max_cover:  # 找到其中覆盖最多关键词的句子
                max_cover = one_cover[i]
                max_num = i
        need_cover = [i for i in need_cover if i not in all_cover[max_num]]  # 将该句覆盖的词从关键词表中删除
        sentence = ''.join(passage[max_num])
        summary.append(sentence)
    summary = '。'.join(summary)
    j = j + 1
    print(j)
    print(summary)
    f.write(str(j)+":"+summary+"\n")

