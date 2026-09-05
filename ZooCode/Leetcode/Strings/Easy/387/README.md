# 387. First Unique Character in a String (Easy)

> [LeetCode 387](https://leetcode.com/problems/first-unique-character-in-a-string/)

## Условение

Дана строка `s`. Найти первый неповторяющийся символ и вернуть его индекс.
Если такого нет — вернуть `-1`.

**Примеры:**
- `s = "leetcode"` → `0` (l)
- `s = "loveleetcode"` → `2` (v)
- `s = "aabb"` → `-1`

**Ограничения:** `1 <= s.length <= 10^5`, строчные английские буквы.

## Решение

**Два прохода.** Первый — подсчёт частот через `Counter`. Второй — поиск
первого символа с частотой 1.

### Сложность
- **Время:** O(n).
- **Память:** O(k), k — размер алфавита (≤ 26).

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/387
pytest -v
```
