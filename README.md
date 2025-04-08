# 324_homework2
# Табличный шифр

Реализация табличного шифра на Python с использованием перестановки столбцов.

## Описание алгоритма

Алгоритм работает в несколько этапов:

1. **Подготовка ключа**:
   - Ключ сортируется по алфавиту
   - Определяется порядок столбцов на основе исходных позиций символов ключа

2. **Шифрование**:
   - Текст записывается в таблицу построчно
   - При необходимости дополняется символом 'X'
   - Столбцы переставляются согласно порядку ключа
   - Шифртекст формируется чтением столбцов сверху вниз

3. **Дешифрование**:
   - Шифртекст разбивается на столбцы
   - Таблица восстанавливается в обратном порядке
   - Исходный текст читается построчно

## Особенности реализации

- Автоматическая обработка текста любой длины
- Поддержка ключей любой длины
- Фильтрация не-алфавитных символов
- Дополнение текста символами 'X' при необходимости
- Подробные тесты всех функций

## Использование

### Базовые операции

```python
from table_cipher import encrypt_tabular, decrypt_tabular

# Encrypting
ciphertext = encrypt_tabular("SECRET MESSAGE", "KEY")  # Returns 'EEEASRMSECTSG'

# Decrypting 
plaintext = decrypt_tabular('EEEASRMSECTSG', "KEY")  # Returns 'SECRET MESSAGE'
```
## Требования
- Python 3.x

## Установка
Установка не требуется. Просто склонируйте репозиторий или загрузите файлы.

## Использование

### Командная строка
Запустите скрипт напрямую: python -m unittest test_table_cipher.py

### Структура проекта
- table_cipher.py - основная реализация алгоритма
- test_table_cipher.py - набор тестов
