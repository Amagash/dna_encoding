from src.utils.conversion import Conversion


def main():
    conversion = Conversion()

    dna = "CCATCCCACAACCCAGCCCACCCACGGACGGCCTATAGAACAGCCCATAGATCGACAGCGCTATCGCCCGATCTAGCACCCTCAGGCTCGTCCGCCCCATCTATCAACCGCTCACCAGACCCATCCCACATTCCAA"
    retrieved_message = conversion.dna_to_str(dna)

    print("The DNA sequence: " + dna) 
    print("contains the secret message: " + retrieved_message)


if __name__ == '__main__':
    main()
