# 28. Find the Index of the First Occurrence in a String (Easy)

> [LeetCode 28](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Условение

Даны строки `haystack` и `needle`. Вернуть индекс первого вхождения `needle`
в `haystack`, или `-1`, если `needle` не является частью `haystack`.

**Примеры:**
- `haystack = "sadbutsad", needle = "sad"` → `0`
- `haystack = "leetcode", needle = "leeto"` → `-1`

**Ограничения:** `1 <= haystack.length, needle.length <= 10^4`.

## Решение

**Прямой поиск (наивный).** Для каждой стартовой позиции `i` в `haystack`
проверяем срез `haystack[i:i+m]` на равенство `needle`. При первом совпадении
возвращаем `i`.

> Для Easy этого достаточно. Для больших данных эффективнее алгоритм KMP
> (O(n+m)), но здесь ограничения малы.

### Сложность
- **Время:** O(n·m) в худшем случае.
- **Память:** O(m) на срез (можно свести к O(1) посимвольным сравнением).

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/28
pytest -v
```
