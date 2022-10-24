from src.main import dna_to_binary, binary_to_dna


def test_dna_to_binary():
    assert dna_to_binary("ATCG") == "00110110"   

def test_binary_to_dna():
    assert binary_to_dna("00110110") == "ATCG"
