import unittest
from table_cipher import encrypt_tabular, decrypt_tabular

class TestTabularCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        test_cases = [
            ("HELLO", "KEY", "EOHLL"),
            ("CRYPTO", "CODE", "CTYPRO"), 
            ("TEST", "A", "TEST"),
            ("SHORT", "LONGKEY", "SHORT")
        ]
        
        for text, key, expected in test_cases:
            encrypted = encrypt_tabular(text, key)
            self.assertEqual(encrypted, expected)
            self.assertEqual(decrypt_tabular(encrypted, key), text)
    
    def test_edge_cases(self):
        self.assertEqual(encrypt_tabular("", "KEY"), "")
        self.assertEqual(decrypt_tabular("", "KEY"), "")
        self.assertEqual(encrypt_tabular("A", "B"), "A")
        self.assertEqual(decrypt_tabular("A", "B"), "A")

if __name__ == "__main__":
    unittest.main()