# 344. Reverse String (Easy)

> [LeetCode 344](https://leetcode.com/problems/reverse-string/)

## Условение

Реверс строки in-place. Вход — список символов `s`, модифицировать его на
месте, не возвращая ничего.

**Примеры:**
- `s = ["h","e","l","l","o"]` → `["o","l","l","e","h"]`
- `s = ["H","a","n","n","a","h"]` → `["h","a","n","n","a","H"]`

**Ограничения:** `1 <= s.length <= 10^5`, `s[i]` — печатный ASCII.

## Решение

**Два указателя.** Меняем местами символы с концов, двигаясь к центру.

### Сложность
- **Время:** O(n).
- **Память:** O(1) (in-place).

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/344
pytest -v
```
