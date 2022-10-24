from src.main import *


def test_dna_to_binary():
    assert dna_to_binary("ATCG") == "00110110"
    assert dna_to_binary("atcg") == "00110110"


def test_binary_to_dna():
    assert binary_to_dna("00110110") == "ATCG"


def test_str_to_binary():
    assert str_to_binary(
        "HELLO WORLD !") == "01001000010001010100110001001100010011110010000001010111010011110101001001001100010001000010000000100001"


def test_binary_to_str():
    assert binary_to_str(
        "01001000010001010100110001001100010011110010000001010111010011110101001001001100010001000010000000100001") == "HELLO WORLD !"
