# -*- coding: utf-8 -*-
# -*- version: python3 -*-

# Get the name of file and open is
name = input("Enter the file name: ")
handle = open(name, "r")
text = handle.read()
words = text.split()

# Count word frequency
counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1
    print(word, ":", counts[word])

# find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

# all done
print(bigword, ":", bigcount)