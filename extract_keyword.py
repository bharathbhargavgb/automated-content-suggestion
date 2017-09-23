from topia.termextract import extract
extractor = extract.TermExtractor()
inputFile = open("input.txt", 'r')
text = inputFile.read();
keywords = sorted(extractor(text))

for tuples in keywords:
    print tuples[0]
