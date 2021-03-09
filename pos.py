from rippletagger.tagger import Tagger

with open("result/processed.txt", "r", encoding="utf-8") as file:
    words = [line.rstrip('\n').split("-")[0] for line in file]
print('Count of the total Words found: ', len(words))

# POS tagging
word = []

tagger = Tagger(language="tam")
for i in words:
    posTagger = tagger.tag(i)
    word.extend(posTagger)

with open("result/pos.txt", "w", encoding="utf-8") as f:
    for s in word:
        f.write(str(s[0]) + "-" + str(s[1]) + "\n")
