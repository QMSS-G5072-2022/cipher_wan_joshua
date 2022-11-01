from cipher_jw4189 import cipher_jw4189
import pytest

def test_cipher():
    expected="Dssoh"
    result=cipher_jw4189.cipher("Apple",3)
    assert result == expected

def test_cipher_with_shift_as_string():
    with pytest.raises(AssertionError):
        cipher_jw4189.cipher("Apple","two")
