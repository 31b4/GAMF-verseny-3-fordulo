with open('szoveg2.txt') as f:
    lines = f.readlines()
words = []
for line in lines:
    for word in line.split(' '):
        if word == '' or word == ' ' or len(word)<1:
            continue #kerdezzuk meg emantol
        if "\n" in word:
            word = word.replace(' ', '')[:-1].upper()
        if not word in words and len(word)>=1:
            words.append(word)
#print(words)
print(len(words))