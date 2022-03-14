def numberOfWord(word,text):
    print(text)
    newText=text.split()
    i=0
    count=0

    while i<len(newText):
        if newText[i]==word:
            count=count+1
        i+i+1
    return (count)

fullText='Where is Waldo ? I think Waldo is hiding behind the wall, we have to find Waldo b'
targetText='Waldo'
num=numberOfWord(targetText,fullText)
print('there are',num,'Waldo in the text')