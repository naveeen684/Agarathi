import tamil

with open("result/pos.txt", "r", encoding="utf-8") as file:
    words = [line.rstrip('\n') for line in file]
print('Count of the total Words found: ', len(words))

unique_words = {}
ini = ["ா", "ி", "ீ", "ு", "ூ", "ெ", "ே", "ை", "ொ", "ோ", "்", "ௌ", "ஹ்", "க்", "ங்", "ச்",
       "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்", "ன்", "ங", "ற"]

for word in words:
    l = tamil.utf8.get_letters(word.split("-")[0])[0]
    if(not any([l == x for x in ini]) and
       len(tamil.utf8.get_letters(word.split("-")[0]))) > 1:
        unique_words[word] = 1 + unique_words.get(word, 0)

print('Count of the unique Words found: ', len(unique_words))

word_array = {k: v for k, v in sorted(unique_words.items(
), reverse=True, key=lambda item: len(tamil.utf8.get_letters(item[0].split("-")[0])))}

with open("result/result.txt", "w", encoding="utf-8") as f:
    for s in word_array.items():
        f.write(str(s[0].split("-")[0]) + "-" +
                str(len(tamil.utf8.get_letters(s[0].split("-")[0])))+"-"+str(s[1]) + "\n")

word_array = {k: v for k, v in sorted(unique_words.items())}

with open("result/alphabetical.txt", "w", encoding="utf-8") as f:
    for s in word_array.items():
        f.write(str(s[0]) + "-" +
                str(len(tamil.utf8.get_letters(s[0].split("-")[0])))+"-"+str(s[1]) + "\n")
