import re
lis = []

f1 = open("regex.txt", mode='r')
whole = f1.read()
lis.append(re.findall('[0-9]+', whole))

for numbers in lis:
    for number in numbers:

        for i in range (0, len(numbers)):
            numbers[i] = int(numbers[i])
        ans = sum(numbers)
    print (ans)
