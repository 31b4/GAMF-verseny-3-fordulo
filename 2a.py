with open('szoveg2.txt') as f:
    lines = f.readlines()
words = []
for line in lines:
    for word in line.split(' '):
        if word == '' or word == ' ':
            continue
        if "\n" in word:
            word = word.replace(' ', '')[:-2].upper()
        if not word in words:
            words.append(word)
print(words)
print(len(words))