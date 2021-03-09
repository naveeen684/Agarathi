import snowballstemmer

stemmer = snowballstemmer.stemmer('tamil')
print(stemmer.stemWords(
    "விடுதலையானஅந்தப்பறவைஉடனேநேராகஅரண்மனைக்கோபுரத்தின்உச்சிக்குப்பறந்துசென்றது".split()))
