#import things
import os

#normal alphabet
alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '.', ',', '?', "'", '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '"', '$', '@'
]

#morse alphabet
morse_code = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
    '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----',
    '.-.-.-', '--..--', '..--..', '.----.', '-.-.--', '-..-.', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.', '-...-', '.-.-.', '-....-', '..--.-', '.-..-.', '...-..-', '.--.-.'
]

#def things
def translate(mores_type, message):
    output = []
    if mores_type == "morse_code":
        words = message.split("   ")
        for word in words:
            letters = word.split()
            for letter in letters:
                index = 0
                while letter != morse_code[index]:
                    index += 1
                output.append(alphabet[index])
            output.append(" ")
        del output[-1]
        return "".join(output)
    if mores_type == "normal":
        words = message.split()
        for word in words:
            for letter in range(len(word)):
                index = 0
                while word[letter] != alphabet[index]:
                    index += 1
                output.append(morse_code[index])
                output.append(" ")
            output.append("   ")
        del output[-1]
        return "".join(output)
            
#clear screen
os.system('cls' if os.name == 'nt' else 'clear')

thing_to_translate = input(f"input a sentece in english or morse code and I will tell you the translated message(if it's morse code put three spaves between words): ")
if thing_to_translate[0] == "." or thing_to_translate[0] == "-":
    print((translate("morse_code", thing_to_translate)).capitalize())
else:
    print(translate("normal", thing_to_translate.upper()))