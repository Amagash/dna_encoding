def dna_to_binary(dna):
    binary = ''
    cipher = {
        'A': '00',
        'C': '01',
        'G': '10',
        'T': '11'
    }
    for base in dna:
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
    for i in range(len(binary)):
        if i % 2 == 0:
            bits = binary[i:i+2]
            dna += cipher[bits]
        i += 1
    print(dna)
    return dna


if __name__ == "__main__":
    binary_in = "00011011"
    dna = binary_to_dna(binary_in)
    print(dna)
