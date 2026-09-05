# 383. Ransom Note (Easy)

> [LeetCode 383](https://leetcode.com/problems/ransom-note/)

## Условение

Даны строки `ransomNote` и `magazine`. Вернуть `true`, если `ransomNote` можно
составить из букв `magazine` (каждая буква используется один раз).

**Примеры:**
- `ransomNote = "a", magazine = "b"` → `false`
- `ransomNote = "aa", magazine = "ab"` → `false`
- `ransomNote = "aa", magazine = "aab"` → `true`

**Ограничения:** `1 <= ransomNote.length, magazine.length <= 10^5`,
строчные английские буквы.

## Решение

**Подсчёт частот.** Считаем частоты букв в `magazine` через `Counter`. Для
каждой буквы `ransomNote` уменьшаем счётчик; если не хватает — `false`.

### Сложность
- **Время:** O(m + n).
- **Память:** O(k), k — размер алфавита (≤ 26).

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/383
pytest -v
```
