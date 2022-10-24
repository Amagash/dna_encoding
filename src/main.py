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
