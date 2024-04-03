def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()   # переводим ключ в верхний регистр
    keyword_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(symbol) - ord('A') + shift) % 26 + ord('A'))
            keyword_index += 1
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()
    keyword_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            keyword_index += 1
        else:
            plaintext += char
    return plaintext
