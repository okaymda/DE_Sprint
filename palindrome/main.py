def reversed(string):
    res=''
    for i in range(len(string)-1,-1,-1):
        res+=string[i]
    return res

str = input()
str = str.replace(' ', '')
str1 = reversed(str)

if str == str1:
    print('True')
else:
    print('False')