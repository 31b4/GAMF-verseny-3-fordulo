with open('szoveg2.txt') as f:
    lines = f.readlines()
words = []
for line in lines:
    for word in line.split(' '):
        if 'E' in word and not 'A'in word and not 'O' in word and not 'U' in word and not 'I' in word:
            words.append(word)
print(len(words))