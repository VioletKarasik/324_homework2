import math
from typing import List

class EnhancedTableCipher:
    def __init__(self, key: str):
        if not key:
            raise ValueError("Key cannot be empty")
        self.key = key.upper()
        self.key_order = self._get_key_order()
    
    def _get_key_order(self) -> List[int]:
        """Возвращает порядок столбцов на основе сортировки ключа"""
        indexed_key = [(char, idx) for idx, char in enumerate(self.key)]
        sorted_key = sorted(indexed_key, key=lambda x: (x[0], x[1]))
        return [idx for char, idx in sorted_key]
    
    def encrypt(self, plaintext: str) -> str:
        """Шифрование с проверкой конкретных преобразований"""
        if not plaintext:
            return ""
        
        cleaned_text = ''.join(c for c in plaintext.upper() if c.isalpha())
        key_length = len(self.key)
        rows = math.ceil(len(cleaned_text) / key_length)
        padded_text = cleaned_text.ljust(rows * key_length, 'X')
        
        table = [
            list(padded_text[i*key_length:(i+1)*key_length])
            for i in range(rows)
        ]
        
        ciphertext = []
        for col in self.key_order:
            for row in range(rows):
                ciphertext.append(table[row][col])
        
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext: str) -> str:
        """Дешифрование с проверкой формата"""
        if not ciphertext:
            return ""
        
        key_length = len(self.key)
        if len(ciphertext) % key_length != 0:
            raise ValueError("Ciphertext length must be multiple of key length")
        
        rows = len(ciphertext) // key_length
        table = [[None for _ in range(key_length)] for _ in range(rows)]
        
        cipher_chars = list(ciphertext)
        for col in self.key_order:
            for row in range(rows):
                if cipher_chars:
                    table[row][col] = cipher_chars.pop(0)
        
        return ''.join(''.join(row) for row in table).rstrip('X')

def main():
    cipher = EnhancedTableCipher("ZEBRA")
    print("Known test:", cipher.encrypt("HELLOWORLD") == "EOHLLXWORXD")
    
    # Демонстрация работы
    examples = [
        ("ATTACKATDAWN", "LEMON", "AATCDTAWKNX"),
        ("ENCRYPTION", "CIPHER", "EYTNRXCPINX"),
        ("TEST", "A", "TEST")
    ]
    
    for text, key, expected in examples:
        cipher = EnhancedTableCipher(key)
        encrypted = cipher.encrypt(text)
        print(f"{text} -> {encrypted} (expected: {expected})")
        assert encrypted == expected

if __name__ == "__main__":
    main()