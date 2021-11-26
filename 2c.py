with open('szoveg2.txt') as f:
    lines = f.readlines()
words = []
for line in lines:
    for word in line.split(' '):
        word = word.strip('\n')
        if len(word)>=2:
            words.append(word)
counter = 0
test_word = []
for word in words:
    if word[::-1] in words: #szamoknal mindig jo?
        counter+=1
        test_word.append(word)
print(test_word)
print(counter)