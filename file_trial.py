"""file=open('backer.txt')
text=file.read()
for cheese in file:
    print(cheese)
n=len(text)
print('length is', n)"""

fname=input('Enter file name:')
try:
    fhand=open(fname)
except:
    print('file doesnot exists')
    quit()
text=fhand.read()
print(text)