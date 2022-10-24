def dna_to_binary(dna):
    binary = ''
    cipher = {
        'A': '00',
        'C': '01',
        'G': '10',
        'T': '11'
    }
    for base in dna.upper():
        binary += cipher[base]
    return binary


def binary_to_dna(binary):
    dna = ''
    cipher = {
        '00': 'A',
        '01': 'C',
        '10': 'G',
        '11': 'T'
    }

    for i in range(0, len(binary), 2):
        bits = binary[i:i+2]
        dna += cipher[bits]
    return dna



def str_to_binary(sentence):
    binary = ''
    for char in sentence:
        bin_char = format(ord(char), 'b')
        if len(bin_char) < 8:
            bin_char = ("0" * (8-len(bin_char))) + bin_char
        binary = binary + bin_char
    return binary


def binary_to_str(binary):
    sentence = ''
    for i in range(0, len(binary), 8):
        sentence += chr(int(binary[i:i+8], 2))
    return sentence


def str_to_dna(sentence):
    binary = str_to_binary(sentence)
    dna = binary_to_dna(binary)
    return dna

