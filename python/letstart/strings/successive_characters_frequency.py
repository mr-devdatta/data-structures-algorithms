test_str = 'geeks are for geeksforgeeks'
que_word = "geek" 

test_str_len = len(test_str)
que_word_len = len(que_word)

pointer = 0
cnt = 0
while pointer < test_str_len:

    pos = test_str.find(que_word, pointer)
    if pos == -1:
        break
    
    cnt +=1
    pointer = pos + que_word_len

print(cnt)
    
    






