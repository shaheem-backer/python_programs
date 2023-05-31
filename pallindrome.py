"""num = input("Enter the number:")
size = len(num)
#print(type(size))
l=size-1
#i = int(0)
for i in range(l):
    #print(i)
    if num[i]!=num[l]:
        print('not pallindrome')
        break
    if num[i] == num[l]:
        l -= 1
        continue
    print('Pallindrome')
print('Done')"""



def is_palindrome(number):
    # Convert the number to a string
    #number_str = str(number)
    # Compare the string with its reverse
    if number == number[::-1]:
        return True
    else:
        return False
# Example usage
num = input('Enter the number:')
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

