# 389. Find the Difference (Easy)

> [LeetCode 389](https://leetcode.com/problems/find-the-difference/)

## Условение

Даны строки `s` и `t`. Строка `t` получена случайной перестановкой `s` и
добавлением одной буквы в случайную позицию. Вернуть добавленную букву.

**Примеры:**
- `s = "abcd", t = "abcde"` → `"e"`
- `s = "", t = "y"` → `"y"`

**Ограничения:** `0 <= s.length <= 1000`, `t.length == s.length + 1`,
строчные английские буквы.

## Решение

**Подсчёт частот.** Считаем частоты `s` через `Counter`. Проходим `t`:
первый символ с нулевым счётчиком — добавленный.

### Сложность
- **Время:** O(n).
- **Память:** O(k), k — размер алфавита (≤ 26).

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/389
pytest -v
```
