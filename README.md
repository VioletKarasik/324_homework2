# 324_homework2
# Улучшенный табличный шифр

Реализация улучшенного табличного шифра на Python.

## Описание алгоритма

1. Ключ сортируется по алфавиту, и определяется порядок столбцов
2. Текст записывается в таблицу по строкам
3. Шифрование: чтение столбцов в порядке ключа сверху вниз
4. Дешифрование: обратный процесс с заполнением таблицы по столбцам

## Использование

```python
from table_cipher import EnhancedTableCipher

# Шифрование
cipher = EnhancedTableCipher("SECRETKEY")
encrypted = cipher.encrypt("Hello World")

# Дешифрование
decrypted = cipher.decrypt(encrypted)