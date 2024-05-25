MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

all_chars = list(MORSE_CODE_DICT.keys())
all_morse_code = list(MORSE_CODE_DICT.values())


def encrypt():
    text = str(input("Type something:")).upper()

    morse_key = ''
    encrypted = ''
    not_morse_key = ''

    for letter in text:
        if letter in all_chars:
            morse_key += letter
        else:
            not_morse_key += letter

    for letter in morse_key:
        encrypted += MORSE_CODE_DICT[letter]
        encrypted += ' '

    print(f"Text = {text}")
    print(f"Characters can be encrypted = {morse_key}")
    print(f"Characters cannot be encrypted = {not_morse_key}")
    print(f"Morse_code = {encrypted}")
    print("")


def decrypt():
    print("***Please insert blank space behind every morse code character")
    morse_code = (input("Paste morse code here: ")).split()

    text = ''
    morse_value = []
    not_morse_value = []

    for item in morse_code:
        if item in all_morse_code:
            text += list(MORSE_CODE_DICT.items())[all_morse_code.index(item)][0]
            morse_value.append(item)
        else:
            not_morse_value.append(item)

    print(f"Morse code = {morse_code}")
    print(f"Morse code can be decrypted = {morse_value}")
    print(f"Characters cannot be decrypted = {not_morse_value}")
    print(f"Text = {text}")
    print("")


def choices():
    choice = input("Encrypt(E) or Decrypt(D)?:").lower()
    if choice == 'encrypt' or choice == 'e':
        encrypt()
    elif choice == 'decrypt' or choice == 'd':
        decrypt()
    else:
        print("Please type only 'Encrypt(E)' or 'decrypt(D)'")
        print("")
        choices()


while input("Do you want to play?(Y/N): ").upper() == "Y":
    choices()

print("END")
