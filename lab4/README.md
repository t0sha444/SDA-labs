# Laboratorul 4 – Quicksort și Binary Search

**Limbaj:** Python 3  
**Cerințe locale:** Quicksort recursiv cu partiționare in-place  
**Probleme LeetCode:** 704 și 35

Funcțiile reutilizabile sunt păstrate în directorul comun [`algorithms/`](../algorithms/), conform cerinței laboratorului. Testele și explicațiile acestui laborator sunt în `lab4/`.

## 1. Sarcină locală – Quicksort

Fișier: [`algorithms/quicksort.py`](../algorithms/quicksort.py)

### Partiționare

Funcția `partition(values, lo, hi)` lucrează pe intervalul semi-deschis `[lo, hi)`. Pivotul este întotdeauna `values[lo]`. `boundary` începe la `lo`; pentru fiecare valoare strict mai mică decât pivotul, incrementăm limita și schimbăm valorile de la `boundary` și `scan`. La final schimbăm pivotul cu valoarea de la `boundary` și returnăm poziția sa.

După partiționare, toate valorile din stânga pivotului sunt `< pivot`, iar toate valorile din dreapta sunt `>= pivot`. Cele două părți nu sunt neapărat sortate încă.

### Trace cerut: `[6, 2, 5, 2, 1]`

```text
Apel quicksort([0, 5))
Pivot 6. Scanăm 2, 5, 2, 1; toate sunt < 6.
După schimbul final pivotului: [1, 2, 5, 2, 6], p = 4
Apeluri: [0, 4) și [5, 5)

Apel quicksort([0, 4))
Pivot 1. Nicio valoare nu este < 1.
Rezultat: [1, 2, 5, 2, 6], p = 0
Apeluri: [0, 0) și [1, 4)

Apel quicksort([1, 4))
Pivot 2. Valorile 5 și 2 nu sunt < 2.
Rezultat: [1, 2, 5, 2, 6], p = 1
Apeluri: [1, 1) și [2, 4)

Apel quicksort([2, 4))
Pivot 5. Valoarea 2 este < 5; o mutăm înaintea pivotului.
Rezultat final: [1, 2, 2, 5, 6], p = 3
Apeluri: [2, 3) și [4, 4)
```

Fiecare apel recursiv sortează un interval care exclude pivotul fixat. Intervalele sunt mai mici decât cel inițial, deci ajung la zero sau un element, cazul de bază. Dacă am include pivotul în apeluri, am putea repeta același interval și nu am garanta progresul.

### Complexitate

- Partiționarea unui interval de `k` elemente face `k - 1` comparații: `O(k)` timp.
- Partiții echilibrate: `O(n log n)` timp și `O(log n)` spațiu pentru apelurile active.
- Partiții foarte dezechilibrate: `O(n^2)` timp și `O(n)` spațiu pentru stiva recursivă.
- Partiționarea este in-place și nu folosește un buffer de dimensiunea listei, dar recursivitatea tot folosește memorie.

Pentru `[1, 2, 3, 4, 5]`, pivotul este mereu minimul din interval: `4 + 3 + 2 + 1 = 10` comparații. Pentru `[2, 2, 2, 2, 2]`, nicio valoare nu este strict mai mică decât pivotul, deci poziția pivotului rămâne la început: tot `4 + 3 + 2 + 1 = 10` comparații. Alegerea aleatorie a pivotului nu repară cazul cu toate valorile egale pentru această regulă strictă `<`.

### Comparație cu Merge Sort din Lab 3

Testele sortează copii separate ale aceleiași liste cu quicksort și cu implementarea Merge Sort din `lab3/solutions/912_sort_an_array.py`. Rezultatele și frecvența valorilor trebuie să coincidă.

Teste quicksort incluse: listă goală, un element, valori negative, duplicate, intrare sortată, invers sortată și toate valorile egale.

## 2. Binary Search – 704. Binary Search

[Deschide problema pe LeetCode](https://leetcode.com/problems/binary-search/)  
Fișier reutilizabil: [`algorithms/binary_search.py`](../algorithms/binary_search.py)  
Fișier LeetCode: [`solutions/704_binary_search.py`](solutions/704_binary_search.py)

Folosim intervalul `[lo, hi)`, inițial `[0, n)`. La fiecare pas calculăm `mid = lo + (hi - lo) // 2`. Dacă valoarea este prea mică, mutăm `lo = mid + 1`; dacă este prea mare, mutăm `hi = mid`. Intervalul se micșorează la fiecare pas, iar dacă devine gol returnăm `-1`.

### Trace pentru `values = [-1, 0, 3, 5, 9, 12]`

Căutare pentru `target = 9`:

| lo | hi | mid | values[mid] | Următorul interval |
|---:|---:|---:|---:|---|
| 0 | 6 | 3 | 5 | `[4, 6)` |
| 4 | 6 | 5 | 12 | `[4, 5)` |
| 4 | 5 | 4 | 9 | găsit la indexul 4 |

Căutare pentru `target = 2`:

| lo | hi | mid | values[mid] | Următorul interval |
|---:|---:|---:|---:|---|
| 0 | 6 | 3 | 5 | `[0, 3)` |
| 0 | 3 | 1 | 0 | `[2, 3)` |
| 2 | 3 | 2 | 3 | `[2, 2)` |

Intervalul devine gol, deci rezultatul este `-1`. O potrivire posibilă rămâne mereu în `[lo, hi)`; eliminăm doar jumătatea care nu poate conține ținta. Dacă am folosi `lo = mid`, când `hi = lo + 1`, `mid` poate fi egal cu `lo`, iar intervalul nu s-ar micșora, ceea ce poate crea o buclă infinită.

Complexitate: timp `O(log n)`, spațiu suplimentar `O(1)`.

## 3. Search Insert Position – 35

[Deschide problema pe LeetCode](https://leetcode.com/problems/search-insert-position/)  
Fișier reutilizabil: [`algorithms/binary_search.py`](../algorithms/binary_search.py)  
Fișier LeetCode: [`solutions/35_search_insert_position.py`](solutions/35_search_insert_position.py)

Această variantă caută prima poziție cu valoarea `>= target`. Dacă `values[mid] < target`, eliminăm jumătatea stângă prin `lo = mid + 1`. Altfel, păstrăm mijlocul ca posibil răspuns prin `hi = mid`. La final, `lo` este poziția de inserare.

| values | target | rezultat |
|---|---:|---:|
| `[1, 3, 5, 6]` | 5 | 2 |
| `[1, 3, 5, 6]` | 2 | 1 |
| `[1, 3, 5, 6]` | 0 | 0 |
| `[1, 3, 5, 6]` | 7 | 4 |
| `[8]` | 3 | 0 |
| `[]` | 3 | 0 |

Toate valorile înainte de poziția returnată sunt mai mici decât ținta; toate valorile de la acea poziție încolo sunt cel puțin egale cu ținta. Complexitate: timp `O(log n)`, spațiu suplimentar `O(1)`.

## Verificare locală

Din folderul repository-ului, rulează:

```bash
python -m unittest lab4.test_algorithms -v
```

Testele folosesc `sorted()` doar pentru a calcula rezultatul așteptat, nu în implementarea quicksort.

## Submission-uri LeetCode

Linkurile de mai sus sunt paginile problemelor. După ce trimiți soluțiile din contul personal și obții `Accepted`, adaugă aici linkurile submission-urilor:

- 704: de completat după Submit.
- 35: de completat după Submit.

## Exercițiu opțional

[905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) este opțional și nu este inclus în cerințele obligatorii ale acestui folder.
