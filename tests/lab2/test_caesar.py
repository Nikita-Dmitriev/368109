import unittest
from src.lab2.caesar import encrypt_caesar
from src.lab2.caesar import decrypt_caesar

class TestCaesar(unittest.TestCase):
    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar('python'), 'sbwkrq')
        self.assertEqual(encrypt_caesar('PYTHON'), 'SBWKRQ')
        self.assertEqual(encrypt_caesar('Python'), 'Sbwkrq')
        self.assertEqual(encrypt_caesar('Python3.5'), 'Sbwkrq3.5')
        self.assertEqual(encrypt_caesar(''), '')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar('sbwkrq'), 'python')
        self.assertEqual(decrypt_caesar('SBWKRQ'), 'PYTHON')
        self.assertEqual(decrypt_caesar('Sbwkrq'), 'Python')
        self.assertEqual(decrypt_caesar('Sbwkrq3.5'), 'Python3.5')
        self.assertEqual(decrypt_caesar(''), '')