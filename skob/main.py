def check(str, ch1, ch2):
    n = 0
    for i in str:
        if i == ch1:
            n += 1
        elif i == ch2:
            n -= 1
        if n < 0: break
    if n == 0:
        return (True)
    else:
        return (False)

string = input()
if check(string, '{', '}') and check(string, '[', ']') and check(string, '(', ')'):
    print(True)
else:
    print(False)