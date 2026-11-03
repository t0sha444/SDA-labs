# Laboratorul 3 – Recursion, Merge și Merge Sort

**Limbaj:** Python 3  
**Probleme:** LeetCode 1342, 88 și 912

Acest laborator are trei exerciții, în ordinea cerută în materialul oficial. Codul este în directorul `solutions/`, iar testele locale sunt în `test_solutions.py`.

## 1. Recursion – 1342. Number of Steps to Reduce a Number to Zero

[Deschide problema pe LeetCode](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)  
Fișier: [`solutions/1342_number_of_steps.py`](solutions/1342_number_of_steps.py)

Soluția este recursivă. Cazul de bază este `num == 0`, iar funcția returnează `0`, deoarece nu mai este necesar niciun pas. Pentru un număr par, apelăm funcția cu `num // 2`; pentru unul impar, cu `num - 1`. Adăugăm `1` pentru operația efectuată în apelul curent.

### Trace pentru 14

```text
numberOfSteps(14)
14 este par -> 1 + numberOfSteps(7)
7 este impar -> 1 + numberOfSteps(6)
6 este par -> 1 + numberOfSteps(3)
3 este impar -> 1 + numberOfSteps(2)
2 este par -> 1 + numberOfSteps(1)
1 este impar -> 1 + numberOfSteps(0)
0 este cazul de bază -> 0

Rezultat: 6 pași
```

Fiecare apel primește un număr mai mic decât cel anterior, iar numărul rămâne nenegativ. Prin urmare, apelurile ajung la `0`. Timp: `O(log n)`. Spațiu suplimentar: `O(log n)` pentru apelurile active de pe stiva de recursivitate.

Teste: `0 -> 0`, `1 -> 1`, `8 -> 4` (par), `7 -> 5` (impar), `14 -> 6`.

## 2. Guided warm-up – 88. Merge Sorted Array

[Deschide problema pe LeetCode](https://leetcode.com/problems/merge-sorted-array/)  
Fișier: [`solutions/88_merge_sorted_array.py`](solutions/88_merge_sorted_array.py)

Ambele porțiuni de intrare sunt deja sortate. Scriem rezultatul direct în `nums1`, începând din capătul listei. Comparăm ultimele valori nefolosite și scriem valoarea mai mare în ultima poziție liberă. Continuăm spre stânga și copiem la final elementele rămase din `nums2`.

### Trace pentru exemplul cerut

```text
nums1 = [2, 5, 6, 0, 0, 0], m = 3
nums2 = [1, 2, 4],          n = 3

Comparație 6 și 4 -> scriem 6 la index 5: [2, 5, 6, 0, 0, 6]
Comparație 5 și 4 -> scriem 5 la index 4: [2, 5, 6, 0, 5, 6]
Comparație 2 și 4 -> scriem 4 la index 3: [2, 5, 6, 4, 5, 6]
Comparație 2 și 2 -> scriem 2 din nums2 la index 2: [2, 5, 2, 4, 5, 6]
Comparație 2 și 1 -> scriem 2 din nums1 la index 1: [2, 2, 2, 4, 5, 6]
Copiem 1 din nums2 la index 0: [1, 2, 2, 4, 5, 6]
```

Scrierea din spate nu suprascrie valori `nums1` care încă nu au fost citite: poziția de ieșire este la dreapta pozițiilor de intrare rămase. Timp: `O(m + n)`. Spațiu suplimentar: `O(1)`, deoarece modificăm `nums1` și folosim doar câțiva indici.

Teste: `m = 0`, `n = 0`, valori egale și valori de intrare egale cu zero sunt incluse în testele locale.

## 3. Merge Sort – 912. Sort an Array

[Deschide problema pe LeetCode](https://leetcode.com/problems/sort-an-array/)  
Fișier: [`solutions/912_sort_an_array.py`](solutions/912_sort_an_array.py)

Nu folosim funcțiile built-in de sortare. Cazul de bază este o porțiune cu zero sau un element; aceasta este deja sortată. Împărțim intervalul în două jumătăți, le sortăm recursiv și apoi interclasăm valorile într-un buffer temporar reutilizat.

### Trace pentru `[6, 2, 5, 2, 1]`

```text
Împărțire:
[6, 2, 5, 2, 1]
├── [6, 2, 5]
│   ├── [6]
│   └── [2, 5] -> [2] + [5] -> [2, 5]
│   Rezultat: [2, 5, 6]
└── [2, 1] -> [2] + [1] -> [1, 2]

Interclasare finală:
[2, 5, 6] + [1, 2] -> [1, 2, 2, 5, 6]
```

Ambele jumătăți trebuie să fie sortate pentru ca la fiecare comparație să putem lua cel mai mic element nefolosit dintre cele două capete curente. Fiecare apel împarte un interval în intervale mai mici, până ajunge la cel mult un element.

La fiecare nivel al recursivității se procesează în total `O(n)` elemente, iar numărul nivelurilor este `O(log n)`, deci timpul este `O(n log n)`. Bufferul reutilizat ocupă `O(n)`, iar stiva de apeluri active `O(log n)`; spațiul suplimentar total este `O(n)`.

Testele locale includ un element, valori negative, duplicate, listă deja sortată, listă sortată invers și o listă cu lungime impară. Verificăm și că valorile și numărul aparițiilor lor se păstrează.

## Verificare locală

Din folderul `lab3`, rulează:

```bash
python test_solutions.py
```

Pentru LeetCode, selectează **Python3**, copiază codul din fișierul problemei, apasă **Run**, apoi **Submit**. Linkurile de mai sus sunt paginile problemelor; linkurile personale către submission-urile `Accepted` trebuie copiate din contul LeetCode după trimitere și pot fi adăugate aici.

## Linkuri submission-uri Accepted

- 1342: de completat după Submit.
- 88: de completat după Submit.
- 912: de completat după Submit.
