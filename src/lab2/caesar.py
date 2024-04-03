def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
    if char.isalpha():  # идем дальше только если символ является буквой
        if char.isupper():  # условие, чтобы в дальнейшем не выпасть из заглавных или строчных букв
            start_position = ord('A')
        else:
            start_position = ord('a')
        ciphertext += chr((ord(char) + shift - start_position) % 26 + start_position) # сдвигаем символ на указаный shift и добавляем в вывод
    else:
        ciphertext += char  # если символ не буква, оставляем как есть
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():  # проверка на базу шифрования
                start_position = ord('A')
            else:
                start_position = ord('a')
            plaintext += chr((ord(char) - start_position - shift) % 26 + start_position # сдвигаем символ к исходному и добавляем в вывод
        else:
            plaintext += char
    return plaintext
