sentence =input()
sentence2=""
words = sentence.split(" ");
for word in words:
    a_word = ''.join(sorted(word))
    #print a_word
    sentence2+=a_word+" ";
print sentence2
    