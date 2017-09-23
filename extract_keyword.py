from topia.termextract import extract
extractor = extract.TermExtractor()
inputFile = open("input.txt", 'r')
text = inputFile.read();
print sorted(extractor(text))
