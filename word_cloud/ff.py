# -*- coding:utf-8 -*-

import jieba.analyse
import matplotlib.pyplot as plt
import requests
from scipy.misc import imread
from wordcloud import WordCloud

def read_txt():
	with open("ff.txt") as files:
		lines=files.readlines()
		# print(lines)
		for line in lines:
			yield line


def word_segment(texts):
	jieba.analyse.set_stop_words("./stopwords.txt")
	for text in texts:
		tags = jieba.analyse.extract_tags(text, topK=50)
		yield " ".join(tags)


def generate_img(texts):
	data = " ".join(text for text in texts)

	mask_img = imread('./heart-mask.jpg', flatten=True)
	wordcloud = WordCloud(
		font_path='msyh.ttc',
		background_color='white',
		mask=mask_img
		).generate(data)
	plt.imshow(wordcloud)
	plt.axis('off')
	plt.savefig('./heart.jpg', dpi=1200)


if __name__ == '__main__':
	generate_img(word_segment(read_txt()))