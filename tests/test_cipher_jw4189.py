from cipher_jw4189 import cipher_jw4189
import pytest

@pytest.fixture
def example_text():
    sample_shift_3=[ ("Apple","Dssoh"),
                     ("apple","dssoh"),
                     ("APPLE","DSSOH"),
                     ("Mary lives in New York.","PduB olyhv lq Qhz brun.")
                   ]
    return sample_shift_3

@pytest.mark.parametrize("sample_text_index", [0,1,2,3])
def test_cipher_expanded(example_text, sample_text_index): #example_text is a list of tuples
    result=cipher_jw4189.cipher(example_text[sample_text_index][0], 3)
    assert result == example_text[sample_text_index][1]