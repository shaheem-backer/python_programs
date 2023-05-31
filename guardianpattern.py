fhand=open('mbox.txt')

#text=fhand.read()

for line in fhand:
    line=line.rstrip()
    lst=line.split()
    #print(lst)
    if len(lst)<1:
        continue
    if lst[0] == 'From':
        print(lst[2])

