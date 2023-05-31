import time

counts=dict()
line=input('Enter the line of text:')

words=line.split()
print('Words:', words)

print('counting...')
time.sleep(2)

for word in words:
    counts[word]=counts.get(word, 0) +1

print('Counts:', counts)