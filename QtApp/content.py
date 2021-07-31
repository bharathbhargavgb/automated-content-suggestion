import sys

print "Hello"

f = open("/Users/baaskab/hackathon/AutomaticContentSuggestion/test.txt", "w")
f.write(sys.argv[1])
f.close()

print "Completed"
