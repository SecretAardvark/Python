message =input('input your message: ')

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

#Loop through every possible key
for key in range(len(SYMBOLS)):
    #It is important to set the blank string so that the 
    #previous iterations value is cleared

    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex= SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex>= len(SYMBOLS):
                translatedIndex = translatedIndex-len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex+len(SYMBOLS
                   
            translated = translated + SYMBOLS[translatedIndex]

        else:
            translated = translated + symbol 

print('Key #%s: %s' % (key, translated))
        