from bs4 import BeautifulSoup
import tamil
from urllib.request import urlopen
import pypandoc
import pdfkit
import docx

link="https://www.projectmadurai.org/pmworks.html"
base = "https://www.projectmadurai.org/pm_etexts/utf8/"

soup = BeautifulSoup(urlopen(link), "html.parser")

links=[]
genres=[]
list_=["கட்டுரைகள்","சிறுகதைகள்","ஆராய்ச்சிக்","வரலாறு","நாடக வரலாறு","நாவல்","கதைகள்","புதினம்","கதை","சொற்பொழிவுகள்","சுய சரிதை"]

for tr in soup.find_all('tr')[2:]:
    if(any(word in tr.find_all('td')[3].text for word in list_)):
        tds = tr.find_all('td')[5]
        href = tds.find_all(href=True)
        for i in href:
            links.append(i.text)

print(links)
for i in range(0,len(links)):
    print(base+links[i])
    soup = BeautifulSoup(urlopen(base+links[i]), "html.parser")
    content =soup.getText()
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~—=|`+'''
    for ele in content:  
        if ele in punc:  
            content = content.replace(ele, " ") 

    
    letters = tamil.utf8.get_letters(content)
    words = tamil.utf8.get_tamil_words(letters)
    unique_words = {}
    for word in words:
        if(len(tamil.utf8.get_letters(word))>1):
            unique_words[word] = 1 + unique_words.get(word, 0)
    

    word_array = {k: v for k, v in sorted(unique_words.items(
    ), reverse=True, key=lambda item: len(tamil.utf8.get_letters(item[0])))}

    with open("projectMadurai/"+links[i]+".txt" , "w", encoding="utf-8") as f:
        for s in word_array.items():
            f.write(str(s[0]) + "-" +
                str(len(tamil.utf8.get_letters(s[0])))+"-"+str(s[1]) + "\n")

    

