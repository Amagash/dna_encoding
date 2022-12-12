from src.main import *
from src.utils.conversion import Conversion

cipher = {
    'A': '00',
    'C': '01',
    'G': '10',
    'T': '11',
    '00': 'A',
    '01': 'C',
    '10': 'G',
    '11': 'T'
}

conversion = Conversion()


def test_str_format():
    assert conversion.str_format("This is a secret message!") == "STARTThis IS#a&secrEt§meSsAgE!STOP"


def test_str_to_binary():
    assert conversion.str_to_binary(
        "HELLO WORLD !") == "01001000010001010100110001001100010011110010000001010111010011110101001001001100010001000010000000100001"

def test_binary_to_dna():
    assert conversion.binary_to_dna("00110110") == "ATCG"


def test_dna_to_binary():
    assert conversion.dna_to_binary("ATCG") == "00110110"


def test_binary_to_str():
    assert conversion.binary_to_str(
        "01001000010001010100110001001100010011110010000001010111010011110101001001001100010001000010000000100001") == "HELLO WORLD !"


def test_str_reverse():
    assert conversion.str_reverse(
        "STARTThis IS#a&secrEt§meSsAgE!STOP") == "this is a secret message!"


def test_str_to_dna():
    assert conversion.str_to_dna("This is a secret message!") == "CCATCCCACAACCCAGCCCACCCACGGACGGCCTATAGAACAGCCCATAGATCGACAGCGCTATCGCCCGATCTAGCACCCTCAGGCTCGTCCGCCCCATCTATCAACCGCTCACCAGACCCATCCCACATTCCAA"


def test_dna_to_str():
    assert conversion.dna_to_str("CCATCCCACAACCCAGCCCACCCACGGACGGCCTATAGAACAGCCCATAGATCGACAGCGCTATCGCCCGATCTAGCACCCTCAGGCTCGTCCGCCCCATCTATCAACCGCTCACCAGACCCATCCCACATTCCAA") == "this is a secret message!"
