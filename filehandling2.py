"""try:
    fhand=open(input('enter file name:'))
except:
    print('file not found')
    exit()
#count=0
for line in fhand:
    line=line.rstrip()
    #count+=1
   # if not line.startswith('From:'):
  #      continue
    if line.find('@uct.ac.za') == -1:
        continue
    else:
        print(line)
#print('line count:', count)

"""