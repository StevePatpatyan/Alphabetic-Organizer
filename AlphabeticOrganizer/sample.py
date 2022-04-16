def split(word):
    return [char for char in word]
order = [None,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
entered = input("Enter a list of words. Separate each word with a space. Press enter when you are done.\n\n")
final = []
letterNum=0
counter = 1
words = entered.split(' ')
for word in words:
    if (len(word)>letterNum):
        letterNum = len(word)
while (letterNum>=0):
    final = []
    for orders in order:
        for word in words:
            if (len(word)-1<letterNum and orders==None):
                final.append(word)
            if (len(word)-1>=letterNum):
                if (split(word)[letterNum].capitalize()==orders):
                    final.append(word)
    words = final
    letterNum = letterNum-counter
print('\n'.join(final))

