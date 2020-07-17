#DSA-Exer-15

def pattern_search(text, pattern):
    return text.count(pattern,0,len(text))

#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result=pattern_search(text, pattern)
print("The given text:",text)
print("Pattern:",pattern)
print("No. of occurrences of the pattern :",result)