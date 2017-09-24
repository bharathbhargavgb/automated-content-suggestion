from extract_keyword import extractKeywords
from fetchURL import *
from summarizer import summarize
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# Get input from file
#print "GETTING INPUT FROM FILE"
#inputFile = open("input.txt", 'r')
#text = inputFile.read()

# Getting input from command line
text = str(sys.argv[1])
print "Input text: ", text, '\n'
# Extract essential keyphrases from the input
print "EXTRACTING KEYWORDS"
keyPhrases = extractKeywords(text)

print "Keyword count: ", len(keyPhrases)
for key in keyPhrases:
    print key

print '\n'

# Get URLs corresponding to each keyword
print "OBTAINING URL FROM KEYWORD"
URLs = []
for keys in keyPhrases:
    URLset = findURLfromKeyword(keys)
    for URLitem in URLset:
        if URLitem not in URLs:
            URLs.append(URLitem)

print "URL count: ", len(URLs)
for url in URLs:
    print url

print '\n'
# Open file to write output
outputFile = open("/Users/baaskab/hackathon/automated-content-suggestion/suggestion.txt", "w")

# Summarize the text from a given URLs
print "SUMMARIZING THE GIVEN URL"
for url in URLs:
    print url , '\n'
    outputFile.write(url + '\n')
    for content in summarize(url):
        print "--> ", content
        outputFile.write("-->" + str(content) + '\n')
    print '\n'
    outputFile.write('\n')

print '\n'

# Find related products on amazon.com based on the extracted keywords
print "FINDING RELATED PRODUCTS ON AMAZON"
products = []
for key in keyPhrases:
    productList = findProductsfromKeyword(key)
    for prod in productList:
        if prod not in products:
            products.append(prod)
            print prod
            outputFile.write(prod + '\n')

outputFile.close()
