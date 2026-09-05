# 345. Reverse Vowels of a String (Easy)

> [LeetCode 345](https://leetcode.com/problems/reverse-vowels-of-a-string/)

## Условение

Дана строка `s`. Реверснуть только гласные буквы (a, e, i, o, u в обоих
регистрах) и вернуть результат.

**Примеры:**
- `s = "hello"` → `"holle"`
- `s = "leetcode"` → `"leotcede"`
- `s = "IceCreAm"` → `"AceCreIm"`

**Ограничения:** `1 <= s.length <= 3*10^5`, `s` — печатные ASCII.

## Решение

**Два указателя.** Левый и правый указатели двигаются навстречу, пропуская
согласные. При встрече двух гласных — меняем их местами.

### Сложность
- **Время:** O(n).
- **Память:** O(n) для списка символов (строка immutable в Python).

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/345
pytest -v
```
