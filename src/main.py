from utils.conversion import Conversion

def main():
    conversion = Conversion()

    dna = "CACGCTCCCGTGAGAACGCGCGACCGATCTCAAGAAATGGAGAACTATCTCCCGGCCTCACGCCAGAATGAAAGAACGCACGTTCGTGAGTAAGAACGTAAGCTCAGCCGTGCTATCTCACGGCCTCACTCCCTCAAGAACCAACGACCTATCTCACGCCCTCCCTAGAGAACTAACGTTCTATCTATTGGACGCACGCCAGAACTCCCGTGAGAACTCGCGGCCGCTCGTGCGTTCGAGCGTACGCCAGAACTACCTCCAGCTCGGCCGTAAGAACGTACGCCCTCCCTAGAGAACGCCCTATCTCAAGAACGGCCGTCCTAACGTTCTATCTATCGGCCGAGCGTACGCCAGAACGCACGCCAGAACTAGCGCCCTCGCGCCCGTGCGCACTAGCGCCAGAAAGAC"

    binary = conversion.dna_to_binary(dna)
    print("BINARY: ", binary)
    secret = conversion.binary_to_str(binary)
    print("SECRET: ***")
    # print("SECRET: ", secret)

    new_dna = conversion.str_to_dna(secret)
    print("NEW DNA: ", new_dna)
    retrieved_message = conversion.dna_to_str(new_dna)
    print("RETRIEVED MESSAGE: ***")
    # print("RETRIEVED MESSAGE: ", retrieved_message)


if __name__ == '__main__':
    main()
