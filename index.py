def interpret_letter(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'

    # Validation
    if len(letter) != 1 or not letter.isalpha():
        return "Invalid input. Please enter a single letter."

    info = {}

    info['Original Letter'] = letter
    info['Uppercase'] = letter.upper()
    info['Lowercase'] = letter.lower()

    lower_letter = letter.lower()

    info['Type'] = 'Vowel' if lower_letter in vowels else 'Consonant'
    info['Alphabet Position'] = alphabet.index(lower_letter) + 1

    return info


# Main program
if __name__ == "__main__":
    letter = input("Enter a letter: ")
    result = interpret_letter(letter)

    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)