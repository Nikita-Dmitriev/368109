import unittest
from src.lab2.vigenere import encrypt_vigenere, decrypt_vigenere

class TestVigenere(unittest.TestCase):
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(encrypt_vigenere("KJHKHDJAHDJA", "NIKITA"), "XRRSADWIRLCA")

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")
        self.assertEqual(decrypt_vigenere("XRRSADWIRLCA", "NIKITA"), "KJHKHDJAHDJA")


if __name__ == '__main__':
    unittest.main()