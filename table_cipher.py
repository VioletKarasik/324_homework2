import math

def encrypt_tabular(text: str, key: str) -> str:
    """Шифрование табличным шифром с дополнением"""
    if not text or not key:
        return text
    
    # Удаляем пробелы и приводим к верхнему регистру
    cleaned_text = ''.join(c for c in text.upper() if c.isalpha())
    cols = len(key)
    rows = math.ceil(len(cleaned_text) / cols)
    padded = cleaned_text.ljust(rows * cols, 'X')
    
    # Создаем таблицу
    table = [list(padded[i*cols:(i+1)*cols]) for i in range(rows)]
    
    # Получаем порядок столбцов
    key_order = [i for i, _ in sorted(enumerate(key.upper()), key=lambda x: x[1])]
    
    # Читаем столбцы в новом порядке
    ciphertext = []
    for col in key_order:
        for row in range(rows):
            ciphertext.append(table[row][col])
    
    return ''.join(ciphertext)

def decrypt_tabular(ciphertext: str, key: str) -> str:
    """Дешифрование табличного шифра"""
    if not ciphertext or not key:
        return ciphertext
    
    cols = len(key)
    if len(ciphertext) % cols != 0:
        raise ValueError("Длина шифртекста должна быть кратна длине ключа")
    
    rows = len(ciphertext) // cols
    
    # Получаем порядок столбцов как при шифровании
    key_order = [i for i, _ in sorted(enumerate(key.upper()), key=lambda x: x[1])]
    
    # Восстанавливаем таблицу
    table = [[None for _ in range(cols)] for _ in range(rows)]
    index = 0
    
    for col in key_order:
        for row in range(rows):
            table[row][col] = ciphertext[index]
            index += 1
    
    # Читаем таблицу построчно и удаляем дополнение
    plaintext = ''.join(''.join(row) for row in table)
    return plaintext.rstrip('X')