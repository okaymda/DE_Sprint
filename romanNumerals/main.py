dict = {0: ['I', 'V', 'X'], 1: ['X', 'L', 'C'], 2:['C', 'D', 'M'], 3:['M']}
x = []
romanNum = ''
arabNum = int(input())

while arabNum != 0:
    x.append(arabNum % 10)
    arabNum //= 10
for i in range (len(x) - 1, -1, -1):
    if x[i] != 0:
        if 1 <= x[i] <= 3:
            romanNum += (dict[i])[0] * x[i]
        elif x[i] == 4:
            romanNum += (dict[i])[0] + (dict[i])[1]
        elif x[i] == 5:
            romanNum += (dict[i])[1]
        elif 6 <= x[i] <= 8:
            romanNum += (dict[i])[1] + ((dict[i])[0] * (x[i]-5))
        else:
            romanNum += (dict[i])[0] + (dict[i])[2]

print(romanNum)