def cipher(text, shift, encrypt=True):
    """"
    The Caesar Cipher is one of the simplest and most widely known encryption techniques. 
    In short, each letter is replaced by a letter some fixed number of positions down the alphabet. 
    Apparently, Julius Caesar used it in his private correspondence.

    Parameters
    -----------
    text : Text to be encrypted
    shift : number of positions down the alphabet to be shifted
    encrypt : takes in boolean values, encrypt = True to encrypt
    Returns encrypted or decrypted text
    --------
    Examples
    ---------
    >>> cipher('Apple', 5)
    'fuuqj'
    >>> cipher('fuuqj', 5, encrypt=False)
    'apple'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text