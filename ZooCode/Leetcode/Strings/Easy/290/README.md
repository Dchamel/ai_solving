# 290. Word Pattern (Easy)

> [LeetCode 290](https://leetcode.com/problems/word-pattern/)

## Условение

Дан `pattern` (строка букв) и строка `s` (слова через пробел). Вернуть `true`,
если `s` следует тому же шаблону, что и `pattern`: биективное соответствие
между буквами и словами.

**Примеры:**
- `pattern = "abba", s = "dog cat cat dog"` → `true`
- `pattern = "abba", s = "dog cat cat fish"` → `false`
- `pattern = "aaaa", s = "dog cat cat dog"` → `false`

**Ограничения:** `1 <= pattern.length <= 300`, `pattern` — строчные английские
буквы, `s` — строчные английские слова через одиночные пробелы.

## Решение

**Биекция через два словаря.** Разбиваем `s` на слова; если количество не
совпадает с длиной `pattern` — `false`. Идём по парам `(буква, слово)`,
поддерживая словари `char→word` и `word→char`. При конфликте — `false`.

### Сложность
- **Время:** O(n + m), n — длина pattern, m — длина s.
- **Память:** O(k), k — количество уникальных пар.

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/290
pytest -v
```
