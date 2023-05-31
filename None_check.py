def addmul(a,b,c=None):
    result=a+b
    if c is not None:
        result = result*c

    return result


n=addmul(1,2,234)

print(n)