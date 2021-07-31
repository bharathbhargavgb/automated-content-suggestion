# @Author: Bharath Bhargav G B <baaskab>
# @Date:   2017-09-25T11:04:04+05:30
# @Email:  baaskab@amazon.com
# @Last modified by:   baaskab
# @Last modified time: 2017-09-25T23:06:44+05:30



import wikipedia

def seeAlsoURL(word, outputFile):
    try:
        #print word
        wikipage = wikipedia.WikipediaPage(word)
        #print wikipage.url
        seeAlso = wikipage.section("See also")
        #print seeAlso
        a = seeAlso.split('\n')
        #print a
        for i in range(0, len(a)):
            if i == 3:
                break
            print wikipedia.page(a[i]).url
            outputFile.write(wikipedia.page(a[i]).url)
    except Exception as e:
        print "";

seeAlsoURL("Object composition", "summa")
