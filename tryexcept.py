raw=input('Enter a number:')
try:
    val=int(raw)
except:
    val= -1

if val>0:
    print('Nice Work.')
else:
    print('Not a Number.')
