# 243. Shortest Word Distance (Easy)

> [LeetCode 243](https://leetcode.com/problems/shortest-word-distance/)

## Условение

Дан массив строк `wordsDict` и две строки `word1` и `word2`, которые присутствуют
в массиве. Вернуть кратчайшее расстояние (по индексу) между любым вхождением
`word1` и любым вхождением `word2`.

**Примеры:**
- `wordsDict = ["practice","makes","perfect","coding","makes"], word1="coding", word2="practice"` → `3`
- `wordsDict = ["practice","makes","perfect","coding","makes"], word1="makes", word2="coding"` → `1`

**Ограничения:** `1 <= wordsDict.length <= 3*10^4`, `word1 != word2`.

## Решение

**Один проход с двумя указателями.** Запоминаем последние индексы `idx1` и
`idx2` для `word1` и `word2`. При каждом обновлении одного из них, если другой
уже встречался, обновляем минимум расстояния.

### Сложность
- **Время:** O(n).
- **Память:** O(1).

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/243
pytest -v
```
