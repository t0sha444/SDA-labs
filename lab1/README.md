# Laboratorul 1 – Array-uri

**Disciplina:** Data Structures and Algorithms  
**Limbaj:** Python 3  
**Temă:** Array-uri și parcurgerea listelor

## Probleme rezolvate

| Nr. | Problemă | Link LeetCode | Fișier |
|---|---|---|---|
| 1 | 1480. Running Sum of 1d Array | [Deschide problema](https://leetcode.com/problems/running-sum-of-1d-array/) | [`solutions/1480_running_sum.py`](solutions/1480_running_sum.py) |
| 2 | 27. Remove Element | [Deschide problema](https://leetcode.com/problems/remove-element/) | [`solutions/27_remove_element.py`](solutions/27_remove_element.py) |

## 1. Running Sum of 1d Array

Parcurg lista de la stânga la dreapta și adun fiecare element la suma precedentă. După fiecare adunare, salvez suma în lista `result`.

**Exemplu:** `nums = [1, 2, 3, 4]` → `[1, 3, 6, 10]`  
**Complexitate:** timp `O(n)`, spațiu suplimentar `O(n)`.

Soluție: [1480_running_sum.py](solutions/1480_running_sum.py)

**Link către submission-ul acceptat:** se adaugă după Submit în LeetCode.

## 2. Remove Element

Parcurg lista și copiez la început doar elementele diferite de `val`. Variabila `k` indică poziția în care va fi copiat următorul element păstrat. La final, metoda returnează numărul elementelor păstrate.

**Exemplu:** `nums = [3, 2, 2, 3]`, `val = 3` → `k = 2`, iar primele două elemente sunt `[2, 2]`.  
**Complexitate:** timp `O(n)`, spațiu suplimentar `O(1)`.

Soluție: [27_remove_element.py](solutions/27_remove_element.py)

**Link către submission-ul acceptat:** se adaugă după Submit în LeetCode.

## Verificare pe LeetCode

1. Deschide linkul problemei.
2. Selectează **Python3**.
3. Copiază codul din fișierul corespunzător.
4. Apasă **Run** pentru testare.
5. Apasă **Submit** și verifică rezultatul **Accepted**.
6. Copiază linkul submission-ului din contul tău LeetCode și adaugă-l mai sus.

> Linkurile din tabel duc la paginile oficiale ale problemelor. Linkurile individuale ale submission-urilor apar după ce trimiți soluțiile din contul tău LeetCode; acestea nu pot fi generate în locul tău.
