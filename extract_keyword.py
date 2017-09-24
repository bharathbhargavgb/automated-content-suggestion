from topia.termextract import extract
#class KeyWord:
def extractKeywords(text):
    extractor = extract.TermExtractor()
    #inputFile = open("input.txt", 'r')
    #text = inputFile.read();    
    keywords = sorted(extractor(text))

    keyPhrases = []

    for tuples in keywords:
        keyPhrases.append(tuples[0])
    return keyPhrases
