import math
from typing import List, Union

def create_table(text: str, key: str, pad_char: str = 'X') -> List[List[str]]:
    """Создает таблицу для шифрования с дополнением"""
    cols = len(key)
    rows = math.ceil(len(text) / cols)
    padded_text = text.ljust(rows * cols, pad_char)
    return [list(padded_text[i*cols:(i+1)*cols]) for i in range(rows)]

def encrypt_tabular(text: Union[str, int], key: Union[str, int]) -> str:
    """Шифрует текст табличным шифром"""
    # Проверка типов
    if not isinstance(text, str) or not isinstance(key, str):
        raise TypeError("Текст и ключ должны быть строками")
    
    if not text or not key:
        return text
    
    # Очищаем текст от пробелов и приводим к верхнему регистру
    cleaned_text = ''.join(c.upper() for c in text if c.isalpha())
    if not cleaned_text:
        return ""
    
    table = create_table(cleaned_text, key)
    
    # Получаем порядок столбцов на основе ключа
    key_order = [i for i, _ in sorted(enumerate(key), key=lambda x: x[1])]
    
    # Читаем столбцы в порядке ключа
    ciphertext = []
    for col in key_order:
        for row in table:
            ciphertext.append(row[col])
    return ''.join(ciphertext)

def decrypt_tabular(ciphertext: Union[str, int], key: Union[str, int]) -> str:
    """Дешифрует текст табличным шифром"""
    # Проверка типов
    if not isinstance(ciphertext, str) or not isinstance(key, str):
        raise TypeError("Шифртекст и ключ должны быть строками")
    
    if not ciphertext or not key:
        return ciphertext
    
    cols = len(key)
    if len(ciphertext) % cols != 0:
        raise ValueError("Длина шифртекста должна быть кратна длине ключа")
    
    rows = len(ciphertext) // cols
    key_order = [i for i, _ in sorted(enumerate(key), key=lambda x: x[1])]
    
    # Восстанавливаем таблицу
    table = [[''] * cols for _ in range(rows)]
    index = 0
    
    for col in key_order:
        for row in range(rows):
            table[row][col] = ciphertext[index]
            index += 1
    
    # Читаем таблицу построчно и удаляем дополнение
    plaintext = ''.join([''.join(row) for row in table])
    return plaintext.rstrip('X')

if __name__ == "__main__":
    # Примеры использования
    samples = [
        ("ATTACK AT DAWN", "LEMON"),
        ("THE QUICK BROWN FOX", "KEY"),
        ("PYTHON IS AWESOME", "CODE"),
        ("KEEP IT SECRET", "LOCK"),
        ("FINAL TEST CASE", "TEST")
    ]
    
    print("🔐 Табличный шифр - Примеры работы")
    for i, (text, key) in enumerate(samples, 1):
        encrypted = encrypt_tabular(text, key)
        decrypted = decrypt_tabular(encrypted, key)
        
        print(f"\nПример {i}:")
        print(f"Оригинал:  {text}")
        print(f"Ключ:      {key}")
        print(f"Шифртекст: {encrypted}")
        print(f"Расшифровка: {decrypted}")