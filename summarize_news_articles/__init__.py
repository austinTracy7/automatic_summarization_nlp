import tkinter
import nltk
from textblob import TextBlob
from newspaper import Article

url = "https://edition.cnn.com/2020/09/13/tech/microsoft-tiktok-bytedance/index.html"
article = Article(url)

article.download()
article.parse()
article.nlp()

analysis = TextBlob(article.text)
print(analysis.polarity)

