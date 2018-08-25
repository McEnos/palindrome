def palindrome(argument):
    #make a list to hold only letter from the argument
    values = []
    for letter in argument:
        #ignore a space or puctuation
        if letter.isspace() or not letter.isalpha():
            continue
        #append only letter/alphabets
        else:
            values.append(letter)
    #make a complete continous string from the letters in values above and convert it to lower case
    string = ''.join(values).lower()
    ##check if string is the same with its reversed version
    return string == string[::-1]
