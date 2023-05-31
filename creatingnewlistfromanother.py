a=[1,2,3]
b=a # here a and b represents the same list
c=list(a) #create a new list c with values same as a

print(a is b)

print(a is not c)

print(a==c) #only check for values

print(a,b,c)

print(type(a),type(b),type(c))