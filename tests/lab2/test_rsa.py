import unittest
from src.lab2.rsa import encrypt
from src.lab2.rsa import decrypt
from src.lab2.rsa import generate_keypair

class TestRSA(unittest.TestCase):
    def testRsa(self):
        pub, priv = generate_keypair(11,13)
        self.assertEqual(decrypt(pub,encrypt(priv,'Vurdalak')),'Vurdalak')
        self.assertEqual(decrypt(pub, encrypt(priv, 'Vlad Tereshenko')), 'Vlad Tereshenko')
        self.assertEqual(decrypt(pub, encrypt(priv, 'GETSEx//1')), 'GETSEx//1')
        self.assertEqual(decrypt(pub, encrypt(priv, 'ALICEabvgd')), 'ALICEabvgd')
        self.assertEqual(decrypt(pub, encrypt(priv, 'PRIVATEmessage')), 'PRIVATEmessage')