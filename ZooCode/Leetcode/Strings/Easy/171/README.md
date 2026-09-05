# 171. Excel Sheet Column Number (Easy)

> [LeetCode 171](https://leetcode.com/problems/excel-sheet-column-number/)

## Условение

Дана строка `columnTitle` — название колонки Excel. Вернуть соответствующий
номер колонки.

| Колонка | Число |
|---------|-------|
| A       | 1     |
| AB      | 28    |
| ZY      | 701   |
| FXSHRXW | 2147483647 |

**Ограничения:** `1 <= columnTitle.length <= 7`, `columnTitle` состоит из
заглавных английских букв.

## Решение

**Горнерова схема по основанию 26.** Проходим строку слева направо:
`result = result * 26 + (буква - 'A' + 1)`. Каждая буква даёт значение 1..26.

### Сложность
- **Время:** O(n), n — длина строки.
- **Память:** O(1).

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/171
pytest -v
```
