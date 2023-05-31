string = '{0:.2f} {1:s} are worth {2:d} EUR'

s = string.format(6.6642345, 'Regensburg Royals', 66) # use format method to input values to the arguments in the string

print(s)


# {0:.2f} formats first argumemt as float upto two decimal places
# {1:s} formats second argument as string
# {2:d} formats the third argument as perfet integer.
