

MORSE_CODE ={".-": 'A', "-...": 'B', "-.-.": 'C', "-..": 'D', ".": 'E', "..-.": 'F',
"--.": 'G', "....": 'H', "..": 'I', ".---": 'J', "-.-": 'K', ".-..": 'L',
"--": 'M', "-.": 'N', "---": 'O', ".--.": 'P', "--.-": 'Q', ".-.": 'R',
"...": 'S', "-": 'T', "..-": 'U', "...-": 'V', ".--": 'W', "-..-": 'X',
"-.--": 'Y', "--..": 'Z', ".----": '1', "..---": '2', "...--": '3',
"....-": '4', ".....": '5', "-....": '6', "--...": '7', "---..": '8',
"----.": '9', "-----": '0'}


ENGLISH_CODE = dict((v,k) for k,v in MORSE_CODE.items())


def translate_morse(morse:str) ->str:
    try:
        return MORSE_CODE[morse]
    except:
        raise ValueError('?')


#Split morse string into a list
#Apply translate morse to each item in list
def translate_sequence(morse_sequence:str) ->str:
    morse_list = morse_sequence.split(' ')
    message = ''
    for morse in morse_list:
        try:
            message += translate_morse(morse)
        except ValueError as e:
            message += str(e)
    
    return message



#SPlit message into words using /
#Loop words and apply translate_sequence
# Add space
def translate_full_message(morse_message:str) -> str:
    word_list = morse_message.split('/')
    decoded_message = ''
    for word in word_list:
        decoded_message += translate_sequence(word.strip())
        decoded_message += ' '

    return decoded_message.strip()



def translate_english(eng:str) -> str:
    return ENGLISH_CODE[eng]


#Split english sentece into words list
#Loop each word and apply translation
def translate_english_sentence(msg:str) -> str:
    word_list = msg.split(' ')
    encoded_msg = ''
    for word in word_list:
        for char in word:
            encoded_msg += translate_english(char)
            encoded_msg += ' '
        
        encoded_msg +='/ '

    return encoded_msg[:-3]







if __name__ == "__main__":
    ...