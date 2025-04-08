import unittest
from table_cipher import encrypt_tabular, decrypt_tabular

class TestTabularCipher(unittest.TestCase):
    def test_basic_encryption_decryption(self):
        test_cases = [
            ("HELLO", "KEY", "EOHLLX", "HELLO"),
            ("CRYPTO", "CODE", "CTYXPXRO", "CRYPTO"),
            ("TEST", "A", "TEST", "TEST"),
            ("SHORT", "LONGKEY", "XRTSOHX", "SHORT")
        ]
        
        for text, key, exp_enc, exp_dec in test_cases:
            encrypted = encrypt_tabular(text, key)
            self.assertEqual(encrypted, exp_enc)
            self.assertEqual(decrypt_tabular(encrypted, key), exp_dec)
    
    def test_with_spaces_and_special_chars(self):
        cases = [
            ("HELLO WORLD!", "KEY", "EORXHLODLWLX", "HELLOWORLD"),
            ("DATA-SCIENCE", "CODE", "DSNTIEAEXACC", "DATASCIENCE")
        ]
        
        for text, key, exp_enc, exp_dec in cases:
            encrypted = encrypt_tabular(text, key)
            self.assertEqual(encrypted, exp_enc)
            self.assertEqual(decrypt_tabular(encrypted, key), exp_dec)
    
    def test_edge_cases(self):
        # Пустые строки
        self.assertEqual(encrypt_tabular("", "KEY"), "")
        self.assertEqual(decrypt_tabular("", "KEY"), "")
        
        # Один символ
        self.assertEqual(decrypt_tabular("AX", "B"), "A")
    
    def test_padding_handling(self):
        # Проверка дополнения
        encrypted = encrypt_tabular("ODD", "EVEN")
        self.assertEqual(len(encrypted), 4)
        self.assertTrue('X' in encrypted)
        self.assertEqual(decrypt_tabular(encrypted, "EVEN"), "ODD")
    
    def test_invalid_input(self):
        # Неверный тип данных
        with self.assertRaises(TypeError):
            encrypt_tabular(123, "KEY")
        with self.assertRaises(TypeError):
            decrypt_tabular("TEXT", 123)

if __name__ == "__main__":
    unittest.main()