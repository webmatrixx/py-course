word = input()
wordLenght = word.__len__()
sum = 0
for letter in range(0,wordLenght):
    currentLetter = word[letter]
    if currentLetter == 'a':
        sum += 1
    elif currentLetter == 'e':

        sum += 2
    elif currentLetter == 'i':
        sum += 3
    elif currentLetter == 'o':
        sum += 4
    elif currentLetter == 'u':
        sum += 5
print(sum)

