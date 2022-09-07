CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '   '
        }

print('Welcome in text to morse converter')
while True:
    user_message = input('Enter message to convert: ').strip().upper()
    try:
        coded_message = [CODE[value] for value in user_message]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(coded_message)

    continue_decision = input('Do you want try again? Y/N: ').strip().upper()
    if continue_decision != 'Y':
        print('Good bye!')
        break
