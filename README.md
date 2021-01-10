# 抽取式文档摘要

## 内容列表

- [安装](#安装)
- [使用说明](#使用说明)

## 安装

这个项目使用了numpy，jieba，request库，请确保安装了它们

```sh
$ pip install numpy
$ pip install jieba
$ pip install request
```

## 使用说明

首先运行crawler.py，爬取简书博客的url，被保存在根目录中的url.txt中。再运行bs.py，爬取文章内容，被保存至/data中。最后依次运行gen_sentences.py, tf_and_idf.py, tf-idf.py和summarization.py, 最后生成的摘要被统一保存在/data中。