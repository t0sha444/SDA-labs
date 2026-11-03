# Laboratorul 2 – Liste înlănțuite (Linked Lists)

**Disciplina:** Data Structures and Algorithms  
**Structuri de date:** Stack și Queue implementate cu liste înlănțuite  
**Limbaj implementare:** C  
**Limbaj probleme LeetCode:** Python 3

## Partea 1 – Implementarea Stack și Queue în C

Fișierul [`linked_lists.c`](linked_lists.c) conține implementări separate pentru Stack (LIFO) și Queue (FIFO), folosind noduri alocate dinamic.

Operații implementate:

- Stack: `push`, `pop`, `peek`, `is_empty`.
- Queue: `enqueue`, `dequeue`, `front`, `is_empty`.

Operațiile de extragere și inspectare verifică dacă structura este goală. Nodurile extrase sunt eliberate, iar la final sunt eliberate toate nodurile rămase.

Testele includ structuri goale, un singur element, mai multe elemente, golirea completă și adăugarea ulterioară a unui element. Pentru valorile `4`, `7`, `2`, Stack returnează `2`, `7`, `4`, iar Queue returnează `4`, `7`, `2`.

### Cum compilezi și rulezi

```bash
gcc -std=c11 -Wall -Wextra -pedantic linked_lists.c -o linked_lists
./linked_lists
```

## Partea 2 – Probleme LeetCode (Python 3)

| Nr. | Problemă | Link LeetCode | Fișier |
|---|---|---|---|
| 1 | 20. Valid Parentheses | [Deschide](https://leetcode.com/problems/valid-parentheses/) | [`20_valid_parentheses.py`](solutions/20_valid_parentheses.py) |
| 2 | 160. Intersection of Two Linked Lists | [Deschide](https://leetcode.com/problems/intersection-of-two-linked-lists/) | [`160_intersection_two_linked_lists.py`](solutions/160_intersection_two_linked_lists.py) |
| 3 | 206. Reverse Linked List | [Deschide](https://leetcode.com/problems/reverse-linked-list/) | [`206_reverse_linked_list.py`](solutions/206_reverse_linked_list.py) |

### 20. Valid Parentheses

Folosesc o stivă pentru parantezele de deschidere. La o paranteză de închidere verific dacă vârful stivei este perechea corespunzătoare. La final, șirul este valid numai dacă stiva este goală.

**Complexitate:** timp `O(n)`, spațiu `O(n)`.

### 160. Intersection of Two Linked Lists

Folosesc doi pointeri. Când unul ajunge la finalul listei, îl mut la începutul celeilalte liste. Astfel, ambii parcurg aceeași distanță totală, iar pointerii se întâlnesc la nodul comun sau la `None`.

**Complexitate:** timp `O(m + n)`, spațiu `O(1)`.

### 206. Reverse Linked List

Inversez legăturile dintre noduri folosind trei pointeri: `previous`, `current` și `next_node`.

**Complexitate:** timp `O(n)`, spațiu `O(1)`.

**Linkurile către submission-urile Accepted:** se adaugă după trimiterea soluțiilor din contul personal LeetCode. Linkurile de mai sus sunt paginile oficiale ale problemelor, nu submission-uri personale.

## Verificare

- Rulează programul C și verifică ordinea LIFO/FIFO din output.
- Pe LeetCode selectează Python3, folosește codul din fișierul problemei, apasă Run și apoi Submit.
- Adaugă în README linkurile personale ale submission-urilor după ce apar ca Accepted.
