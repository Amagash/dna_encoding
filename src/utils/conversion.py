class Conversion:
    def __init__(self) -> None:
        self.cipher = {
        'A': '00',
        'C': '01',
        'G': '10',
        'T': '11',
        '00': 'A',
        '01': 'C',
        '10': 'G',
        '11': 'T'
        }
    class Colors:
        DBLUE = '\033[34m'
        LBLUE = '\033[36m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        RED = '\033[31m'
        PURPLE = '\033[35m'
        ENDC = '\033[0m'

    def menu(self):
        option = str(input(f"{self.Colors.LBLUE}Encrypt or decrypt ? (e/d): {self.Colors.ENDC}"))
        match option:
            case "e":
                self.encrypt()
            case "E":
                self.encrypt()
            case "d":
                self.decrypt()
            case "D":
                self.decrypt()
            case _:
                print(f"{self.Colors.RED} => Please enter a valid option. (e/d){self.Colors.ENDC}")
            
        return option

    def encrypt(self):
        str_to_format = str(input(f"{self.Colors.LBLUE}Message to encrypt : {self.Colors.ENDC}"))
        result = self.str_format(str_to_format)
        format_to_binary = self.str_to_binary(result)
        binary_to_dna = self.binary_to_dna(format_to_binary)
        print(f"{self.Colors.LBLUE}Encrypted DNA sequence : {self.Colors.ENDC}{self.Colors.GREEN}{binary_to_dna}{self.Colors.ENDC}\n")

    def decrypt(self):
        dna = str(input(f"{self.Colors.LBLUE}DNA sequence to decrypt : {self.Colors.ENDC}"))
        retrieved_message = self.dna_to_str(dna)
        print(f"{self.Colors.LBLUE}Decrypted DNA sequence : {self.Colors.ENDC}{self.Colors.GREEN}{retrieved_message}{self.Colors.ENDC}\n")

    def str_format(self, sentence):
        '''
        Returns the formatted sentence with the variations needed to avoid repeated patterns.

            Parameters:
                    sentence (str): The str sentence

            Returns:
                    encapsulated_formatted_sentence (str): The sentence with variations and encapsulated with "START" and "STOP"

            Example:
                    sentence = "hello world"
                    returns "STARThelLo wOrld STOP"
        '''
        formatted_sentence = ""
        count = {}
        for char in sentence:
            if char not in count:
                formatted_sentence += char
                count[char] = 1
            elif char == " ":
                options = ["#", "&", "§", "_", "+", "^", " "]
                pick = count[char] % 7 - 1
                char_new = options[pick]
                formatted_sentence += char_new
                count[char] += 1
            elif count[char] % 2 != 0:
                char_up = char.upper()
                formatted_sentence += char_up
                count[char] += 1
            else:
                formatted_sentence += char
                count[char] += 1
        encapsulated_formatted_sentence = "START" + formatted_sentence + "STOP"
        return encapsulated_formatted_sentence

    def str_to_binary(self, sentence):
        '''
        Returns the binary sequence of a string.

            Parameters:
                    sentence (str): The str sentence

            Returns:
                    binary (str): The binary sequence of the variable sequence

            Example:
                    sentence = "hi"
                    returns "0110100001101001"
        '''
        binary = ''
        for char in sentence:
            bin_char = format(ord(char), 'b')
            if len(bin_char) < 8:
                bin_char = ("0" * (8-len(bin_char))) + bin_char
            binary = binary + bin_char
        return binary

    def binary_to_dna(self, binary):
        '''
        Returns the dna sequence of a binary sequence.

            Parameters:
                    binary (str): The binary sequence

            Returns:
                    dna (str): The dna sequence of the variable binary

            Example:
                    binary = "0110100001101001"
                    returns "CGGACGGC"
        '''
        dna = ''
        for i in range(0, len(binary), 2):
            bits = binary[i:i+2]
            dna += self.cipher[bits]
        return dna

    def dna_to_binary(self, dna):
        '''
        Returns the binary sequence of a dna sequence.

            Parameters:
                    dna (str): The dna sequence

            Returns:
                    binary (str): The binary sequence of the variable dna

            Example:
                    dna = "CGGACGGC"
                    returns "0110100001101001"
        '''
        binary = ''
        for base in dna.upper():
            binary += self.cipher[base]
        return binary

    def binary_to_str(self, binary):
        '''
        Returns the sentence of a binary sequence.

            Parameters:
                    binary (str): The binary sequence

            Returns:
                    sentence (str): The sentence of the variable binary

            Example:
                    binary = "0110100001101001"
                    returns "hi"
        '''
        sentence = ''
        for i in range(0, len(binary), 8):
            sentence += chr(int(binary[i:i+8], 2))
        return sentence

    def str_reverse(self, formatted_sentence):
        '''
        Returns the lower-cased sentence of a formatted sentence (e.g a sentence with the variations needed to avoid repeated patterns).

            Parameters:
                    formatted_sentence (str): The formatted sentence

            Returns:
                    reverse (str): The reverse of the variable formatted sentence

            Example:
                    formatted_sentence = "STARTThis IS#a&secrEt§meSsAgE!STOP"
                    returns "this is a secret message!"
        '''
        reversed_sentence = ""
        options = ["#", "&", "§", "_", "+", "^"]
        for char in formatted_sentence:
            if char in options:
                reversed_sentence += " "
            else:
                reversed_sentence += char
        reversed_lower_sentence = reversed_sentence.lower()
        return reversed_lower_sentence[5:-4]

    def str_to_dna(self, message):
        '''
        Returns the dna sequence of a message.

            Parameters:
                    message (str): The message

            Returns:
                    dna (str): The dna sequence of the variable message

            Example:
                    message = "hi"
                    returns "CCATCCCACAACCCAGCCCACGGACGGCCCATCCCACATTCCAA"
        '''
        formatted_string = self.str_format(message)
        bin = self.str_to_binary(formatted_string)
        dna = self.binary_to_dna(bin)
        return dna

    def dna_to_str(self, dna):
        '''
        Returns the message contained in a dna sequence.

            Parameters:
                    dna (str): The dna sequence

            Returns:
                    message (str): The message of the variable dna

            Example:
                    dna = "CCATCCCACAACCCAGCCCACGGACGGCCCATCCCACATTCCAA"
                    returns "hi"
        '''
        reversed_bin = self.dna_to_binary(dna)
        reversed_formatted_string = self.binary_to_str(reversed_bin)
        reversed_string = self.str_reverse(reversed_formatted_string)
        return reversed_string
