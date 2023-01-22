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
    assert conversion.str_format("Hello world") == "STARTHelLo wOrldSTOP"
    assert conversion.str_format("This is a secret message!") == "STARTThis IS#a&secrEt§meSsAgE!STOP"


def test_str_to_binary():
    assert conversion.str_to_binary("HELLO WORLD !") == "01001000010001010100110001001100010011110010000001010111010011110101001001001100010001000010000000100001"
    assert conversion.str_to_binary("hi") == "0110100001101001"
    assert conversion.str_to_binary("START") == "0101001101010100010000010101001001010100"
    assert conversion.str_to_binary("STOP") == "01010011010101000100111101010000"

def test_binary_to_dna():
    assert conversion.binary_to_dna("00110110") == "ATCG"
    assert conversion.binary_to_dna("0110100001101001") == "CGGACGGC"
    assert conversion.binary_to_dna("0101001101010100010000010101001001010100") == "CCATCCCACAACCCAGCCCA"
    assert conversion.binary_to_dna("01010011010101000100111101010000") == "CCATCCCACATTCCAA"


def test_dna_to_binary():
    assert conversion.dna_to_binary("ATCG") == "00110110"
    assert conversion.dna_to_binary("CGGACGGC") == "0110100001101001"


def test_binary_to_str():
    assert conversion.binary_to_str("01001000010001010100110001001100010011110010000001010111010011110101001001001100010001000010000000100001") == "HELLO WORLD !"
    assert conversion.binary_to_str("0110100001101001") == "hi"

def test_str_reverse():
    assert conversion.str_reverse("STARTThis IS#a&secrEt§meSsAgE!STOP") == "this is a secret message!"


def test_str_to_dna():
    assert conversion.str_to_dna("This is a secret message!") == "CCATCCCACAACCCAGCCCACCCACGGACGGCCTATAGAACAGCCCATAGATCGACAGCGCTATCGCCCGATCTAGCACCCTCAGGCTCGTCCGCCCCATCTATCAACCGCTCACCAGACCCATCCCACATTCCAA"
    assert conversion.str_to_dna("hi") == "CCATCCCACAACCCAGCCCACGGACGGCCCATCCCACATTCCAA"


def test_dna_to_str():
    assert conversion.dna_to_str("CCATCCCACAACCCAGCCCACCCACGGACGGCCTATAGAACAGCCCATAGATCGACAGCGCTATCGCCCGATCTAGCACCCTCAGGCTCGTCCGCCCCATCTATCAACCGCTCACCAGACCCATCCCACATTCCAA") == "this is a secret message!"
    assert conversion.dna_to_str("CCATCCCACAACCCAGCCCACGGACGGCCCATCCCACATTCCAA") == "hi"