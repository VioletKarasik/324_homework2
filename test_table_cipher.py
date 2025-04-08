import unittest
from table_cipher import EnhancedTableCipher

class TestEnhancedTableCipher(unittest.TestCase):
    def test_encrypt_decrypt_roundtrip_basic(self):
        cipher = EnhancedTableCipher("ZEBRA")
        plaintext = "HELLO WORLD"
        encrypted = cipher.encrypt(plaintext)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, "HELLOWORLD")

    def test_encrypt_decrypt_with_padding(self):
        cipher = EnhancedTableCipher("KEY")
        plaintext = "TESTING"
        encrypted = cipher.encrypt(plaintext)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, "TESTING")

    def test_encrypt_decrypt_lowercase(self):
        cipher = EnhancedTableCipher("simple")
        plaintext = "encrypt me please"
        encrypted = cipher.encrypt(plaintext)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, "ENCRYPTMEPLEASE")

    def test_decrypt_with_padding_xs(self):
        cipher = EnhancedTableCipher("ABC")
        plaintext = "FOO"
        encrypted = cipher.encrypt(plaintext)  # Might pad with 'X'
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, "FOO")

    def test_empty_plaintext(self):
        cipher = EnhancedTableCipher("KEY")
        self.assertEqual(cipher.encrypt(""), "")
        self.assertEqual(cipher.decrypt(""), "")

    def test_invalid_key(self):
        with self.assertRaises(ValueError):
            EnhancedTableCipher("")

    def test_invalid_decrypt_length(self):
        cipher = EnhancedTableCipher("LONGKEY")
        with self.assertRaises(ValueError):
            cipher.decrypt("TOOSHORT")

if __name__ == "__main__":
    unittest.main()