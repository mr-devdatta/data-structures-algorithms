
sentence ="The quick brown fox jumped over the lazy dog"
lst = sentence.split(" ")
#print(lst)

cnt = 0
index = 0
for key, wrd in enumerate(lst):
    
    if len(wrd) >= cnt:
        index = key
        cnt = len(wrd)
        
    leng = len(wrd)

#print(lst[index])
    
# ------------------------------------------------------------------------------------

text = "The quick brown fox jumped over the lazy dog"
words = text.split()
print(words)

longStr = ""
for word in words:
    if len(word) > len(longStr):
        longStr = word
    
print(longStr)