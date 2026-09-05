# 392. Is Subsequence (Easy)

> [LeetCode 392](https://leetcode.com/problems/is-subsequence/)

## Условение

Даны строки `s` и `t`. Вернуть `true`, если `s` — подпоследовательность `t`
(можно удалить символы из `t`, но не менять порядок).

**Примеры:**
- `s = "abc", t = "ahbgdc"` → `true`
- `s = "axc", t = "ahbgdc"` → `false`

**Ограничения:** `0 <= s.length <= 100`, `0 <= t.length <= 10^4`,
строчные английские буквы.

## Решение

**Итератор с `all`.** Создаём итератор по `t`. Для каждого символа `s`
проверяем `ch in it` — это продвигает итератор до следующего вхождения `ch`.
Если все найдены — `true`. Идиоматичный Python, короткозамкнутый.

### Сложность
- **Время:** O(|t|) — один проход по `t`.
- **Память:** O(1).

## Файлы
- [`solution.py`](solution.py) — решение.
- [`test_solution.py`](test_solution.py) — pytest-тесты.

## Запуск тестов

```bash
cd ZooCode/Leetcode/Strings/Easy/392
pytest -v
```
