import math

def create_table(text, key, pad_char='_'):
    """Создает таблицу с дополнением"""
    cols = len(key)
    rows = math.ceil(len(text) / cols)
    padded = text.ljust(rows * cols, pad_char)
    return [list(padded[i*cols:(i+1)*cols]) for i in range(rows)]

def encrypt_tabular(text, key):
    """Шифрование с сохранением дополнения"""
    if not text or not key:
        return text
    
    table = create_table(text, key)
    # Сортируем индексы столбцов по ключу
    key_order = [i for i, _ in sorted(enumerate(key), key=lambda x: x[1])]
    
    # Читаем столбцы в новом порядке
    ciphertext = []
    for col in key_order:
        for row in table:
            ciphertext.append(row[col])
    return ''.join(ciphertext)

def decrypt_tabular(ciphertext, key):
    """Дешифрование с обработкой дополнения"""
    if not ciphertext or not key:
        return ciphertext
    
    cols = len(key)
    if len(ciphertext) % cols != 0:
        raise ValueError("Invalid ciphertext length for given key")
    
    rows = len(ciphertext) // cols
    key_order = [i for i, _ in sorted(enumerate(key), key=lambda x: x[1])]
    
    # Восстанавливаем таблицу
    table = [[None]*cols for _ in range(rows)]
    index = 0
    
    # Заполняем столбцы в порядке шифрования
    for col in key_order:
        for row in range(rows):
            table[row][col] = ciphertext[index]
            index += 1
    
    # Читаем построчно и удаляем дополнение
    return ''.join(''.join(row) for row in table).rstrip('_')

if __name__ == "__main__":
    examples = [
        {"text": "HELLOENCRYPTION", "key": "KEY"},
        {"text": "THISISASECRETMESSAGE", "key": "SECRET"},
        {"text": "PYTHON", "key": "CIPHER"},
        {"text": "SHORT", "key": "VERYLONGKEY"},
        {"text": "ONE", "key": "A"},
    ]
    
    print("🔐 Improved Tabular Cipher")
    for i, ex in enumerate(examples, 1):
        enc = encrypt_tabular(ex["text"], ex["key"])
        dec = decrypt_tabular(enc, ex["key"])
        print(f"\nExample {i}:")
        print(f"Original: {ex['text']}")
        print(f"Key:     {ex['key']}")
        print(f"Encrypted: {enc}")
        print(f"Decrypted: {dec}")