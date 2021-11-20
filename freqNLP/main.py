from nltk.corpus import stopwords
#variabls
TOKEN_DELIMITER = [",", ".", "!", "?", "/", "&", "-", ":", ";", "@", "'", "..."]
EMPTY_SPACE = ' '

# functions
def endOfSent(sentence,index):
    return len(sentence) == index

def DocMap(text):
    index = 0
    word = ""
    words = []
    while not endOfSent(text, index):
        if text[index] == EMPTY_SPACE and len(word) > 0:
            words.append(word.strip())
            word = ""
        elif text[index] in TOKEN_DELIMITER:
            words.append(word.strip())
            words.append(text[index])
            word = ""
        else:
            word += text[index]
        index += 1

    return words

def frequanceyTable(words):
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
    return frequency

def SentenceTokenizer(words):
    sentence = ""
    sentences = []
    for word in words:
        if word in TOKEN_DELIMITER and len(sentence) > 0:
            sentences.append(sentence.strip())
            sentence = ""
        else:
            sentence += word + " "
    return sentences

#reading the file and converting it into a list.
def readFile(filename):
    with open(filename,"r") as f:
        text = f.read()
        return text

#removing the puncuation.
def removePunc(words):
    text_nopunc = " ".join([char for char in words if char not in TOKEN_DELIMITER])
    return text_nopunc

#reading the file.
text = readFile("ztest.txt")
print(text)

words = DocMap(text)
#convertin the list to lowercase.
words = [each_string.lower() for each_string in words]
print(SentenceTokenizer(words))

#removing the puncuation.
cleanText = removePunc(words)

cleanTexts = DocMap(cleanText)
#extracting the stopwords from the list.
stops = set(stopwords.words('english'))
wordsFiltered = []
for w in cleanTexts:
    if w not in stops:
        wordsFiltered.append(w)

freq = frequanceyTable(wordsFiltered)
#print frequanceyTable
print("The Frequency Table")
for index, i in enumerate(freq):
    print(str(index+1) + " " + i + " " + str(freq[i]))
