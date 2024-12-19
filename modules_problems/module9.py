def preLetterCase(input_str, letter):
    if letter not in input_str:
        return input_str.lower()
    result = []
    for i in range(len(input_str)):
        if input_str[i] == letter:
            result.append(input_str[:i].lower())
            result.append(letter.upper())
            result.append(input_str[i + 1:].upper())
            break
    return ''.join(result)
input_str = input("Enter the string: ")
letter = input("Enter the letter: ")
print("The modified string is:")
print(preLetterCase(input_str, letter))
