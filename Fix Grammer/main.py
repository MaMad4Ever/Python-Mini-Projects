from textblob import TextBlob 

text = "I amm goodd"
originalText = TextBlob(text)

correctText = originalText.correct() 

print("originalText: " + text)
print("correctText: " + str(correctText)) 
