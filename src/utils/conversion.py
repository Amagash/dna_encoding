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

    def str_format(self, sentence):
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
        return "START" + formatted_sentence + "STOP"

    def str_to_binary(self, sentence):
        binary = ''
        for char in sentence:
            bin_char = format(ord(char), 'b')
            if len(bin_char) < 8:
                bin_char = ("0" * (8-len(bin_char))) + bin_char
            binary = binary + bin_char
        return binary

    def binary_to_dna(self, binary):
        dna = ''
        for i in range(0, len(binary), 2):
            bits = binary[i:i+2]
            dna += self.cipher[bits]
        return dna


    def dna_to_binary(self, dna):
        binary = ''
        for base in dna.upper():
            binary += self.cipher[base]
        return binary
    

    def binary_to_str(self, binary):
        sentence = ''
        for i in range(0, len(binary), 8):
            sentence += chr(int(binary[i:i+8], 2))
        return sentence

    def str_reverse(self, formatted_sentence):
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
        formatted_string = self.str_format(message)
        bin = self.str_to_binary(formatted_string)
        dna = self.binary_to_dna(bin)
        return dna

    def dna_to_str(self, dna):
        reversed_bin = self.dna_to_binary(dna)
        reversed_formatted_string = self.binary_to_str(reversed_bin)
        reversed_string = self.str_reverse(reversed_formatted_string)
        return reversed_string
