import unittest
from projectCipher import caesar

class TestSum(unittest.TestCase):
    def test_encode(self):
        plain_text = 'Subutilizai'
        cipher_text = '-YFYXMPM3EM'

        self.assertEqual(caesar(plain_text, shift=30, direction="encode"), cipher_text)

    def test_decode(self):
        plain_text  = 'rejeitam'
        cipher_text = '&2726(Y!'

        self.assertEqual(caesar(cipher_text, shift=50, direction="decode"), plain_text)
