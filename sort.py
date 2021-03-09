import numpy
import operator
import tamil


with open("combined/total.txt", "r", encoding="utf-8") as file:
    words = [line.rstrip('\n').split("-")[0] for line in file]


print('Count of the total Words found: ', len(words))

punc = '''அஆஇஈஉஊஎஏஐஒஓஔ'''

unique_words = {}
for word in words:
    unique_words[word] = 1 + unique_words.get(word, 0)

print('Count of the unique Words found: ', len(unique_words))

word_array = {k: v for k, v in sorted(unique_words.items(
), reverse=True, key=lambda item: len(tamil.utf8.get_letters(item[0])))}

with open("result/sorted.txt", "w", encoding="utf-8") as f:
    for s in word_array.items():
        f.write(str(s[0]) + "-" +
                str(len(tamil.utf8.get_letters(s[0])))+"-"+str(s[1]) + "\n")
