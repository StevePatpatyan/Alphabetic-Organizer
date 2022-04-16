order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
entered = input("Enter a list of words. Separate each word with a space. Press enter when you are done.\n\n")
final = []
words = entered.split(' ')
for orders in order:
    for word in words:
        print(word.split())
