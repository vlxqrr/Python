import pytest

def Data(text: str, key: int) -> str:
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) + key - 97) % 26 + 97)

        else: 
            result += char
    return result
    
def test_defaultData():
    ciphered = Data("abc", 3)
    print(f"Zaszyfrowane abc -> {ciphered}")
    assert ciphered == "def"

def test_rangeData():
    ciphered = Data("xyz", 3)
    print(f"Zaszyfrowane xyz -> {ciphered}")
    assert ciphered == "abc"

def test_descData():
    ciphered = Data("def", -3)
    print(f"Zaszyfrowane ab cd -> {ciphered}")
    assert ciphered == "abc"

def test_isOutOfRangeData():
    ciphered = Data("abc", 29)
    print(f"Zaszyfrowane abc -> {ciphered}")
    assert ciphered == "def"

def test_spaceData():
    ciphered = Data("ab cd", 2)
    print(f"Zaszyfrowane ab cd -> {ciphered}")
    assert ciphered == "cd ef"

