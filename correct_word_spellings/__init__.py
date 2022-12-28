from textblob import TextBlob

# Spelling Correction
text = TextBlob("I love Machne Learnin")
print(text.correct())
