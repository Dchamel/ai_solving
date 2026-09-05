# 405. Convert a Number to Hexadecimal (Easy)

> [LeetCode 405](https://leetcode.com/problems/convert-a-number-to-hexadecimal/)

## Условение

Дано целое число `num`. Вернуть строку — его шестнадцатеричное представление.
Для отрицательных чисел использовать дополнительный код (32 бита).

**Примеры:**
- `num = 26` → `"1a"`
- `num = -1` → `"ffffffff"`

**Ограничения:** `-2^31 <= num <= 2^31 - 1`.

## Решение

**Побитовый сдвиг.** Для отрицательных чисел добавляем `2^32` (переход к
unsigned 32-bit). Затем извлекаем по 4 бита (`num & 0xF`) справа налево,
преобразуя в hex-цифру, пока число не обнулится.

### Сложность
- **Время:** O(log₁₆ num) — до 8 итераций для 32-бит.
- **Память:** O(log₁₆ num) для результата.

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/405
pytest -v
```
