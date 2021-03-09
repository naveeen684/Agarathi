from indicnlp.morph import unsupervised_morph
from indicnlp import common
from indicnlp import loader
from indicnlp.morph import unsupervised_morph

with open("result/sorted.txt", "r", encoding="utf-8") as file:
    words = [line.rstrip('\n').split("-")[0] for line in file]
print('Count of the total Words found: ', len(words))

INDIC_NLP_RESOURCES = r"D:\Studies\Niral\indic_nlp_resources-master"

common.set_resources_path(INDIC_NLP_RESOURCES)

loader.load()

analyzer = unsupervised_morph.UnsupervisedMorphAnalyzer('ta')

word = []
for i in range(0, len(words)):
    analyzes_tokens = analyzer.morph_analyze_document(words[i].split(' '))
    word.extend(analyzes_tokens)
    print(i)

with open("result/processed.txt", "a", encoding="utf-8") as f:
    for s in word:
        f.write(str(s) + "\n")
