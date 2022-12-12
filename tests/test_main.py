from src.main import *
from src.utils.conversion import Conversion


def test_str_format():
    assert str_format("aaaa        ") == "aAaA #&§_+^ "


def test_dna_to_binary():
    conversion = Conversion("ATCG")
    assert conversion.dna_to_binary() == "00110110"


def test_binary_to_dna():
    conversion = Conversion("ATCG")
    assert conversion.binary_to_dna("00110110") == "ATCG"


def test_str_to_binary():
    assert str_to_binary(
        "HELLO WORLD !") == "01001000010001010100110001001100010011110010000001010111010011110101001001001100010001000010000000100001"


def test_binary_to_str():
    assert binary_to_str(
        "01001000010001010100110001001100010011110010000001010111010011110101001001001100010001000010000000100001") == "HELLO WORLD !"
