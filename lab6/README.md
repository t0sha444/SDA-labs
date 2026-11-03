# Laboratorul 6 – Binary Search Trees, DFS și BFS

**Limbaj:** Python 3  
**Probleme LeetCode:** 701 (Medium), 94 (Easy), 102 (Medium)

Laboratorul are trei exerciții. Primul cere construirea locală a unui BST și rezolvarea problemei LeetCode 701. Al doilea cere DFS inorder, iar al treilea BFS pe niveluri. Funcțiile reutilizabile pentru testarea locală sunt în `algorithms/binary_search_tree.py`; soluțiile LeetCode sunt în `solutions/`.

## 1. Build a Binary Search Tree – 701. Insert into a Binary Search Tree

[Deschide problema LeetCode 701](https://leetcode.com/problems/insert-into-a-binary-search-tree/)  
Implementare locală: [`../algorithms/binary_search_tree.py`](../algorithms/binary_search_tree.py)  
Soluție LeetCode: [`solutions/701_insert_into_bst.py`](solutions/701_insert_into_bst.py)

Un nod păstrează valoarea și referințele `left` și `right`. Pentru o valoare nouă, comparăm cu nodul curent: dacă este mai mică mergem la stânga, dacă este mai mare mergem la dreapta. Când găsim o legătură `None`, creăm frunza. Funcția returnează rădăcina subarborelui, iar apelantul salvează rezultatul în legătura copilului potrivit. În versiunea locală, duplicatele nu schimbă arborele, conform cerinței.

### Construirea arborelui din cerință

Valori inserate: `[4, 2, 7, 1, 3, 6, 9]`.

```text
1) insert 4: rădăcina este 4

2) insert 2: 2 < 4, mergem stânga
    4
   /
  2

3) insert 7: 7 > 4, mergem dreapta
    4
   / \
  2   7

4) insert 1: 1 < 4, apoi 1 < 2, devine copilul stâng al lui 2
      4
     / \
    2   7
   /
  1

5) insert 3: 3 < 4, apoi 3 > 2, devine copilul drept al lui 2
      4
     / \
    2   7
   / \
  1   3

6) insert 6: 6 > 4, apoi 6 < 7, devine copilul stâng al lui 7
      4
     / \
    2   7
   / \ /
  1  3 6

7) insert 9: 9 > 4, apoi 9 > 7, devine copilul drept al lui 7
        4
       / \
      2   7
     / \ / \
    1  3 6  9
```

### Predicție și inserarea valorii 5

Într-un arbore nou construit cu valorile din exemplu, traseul este `4 -> 7 -> 6`. Deoarece `5 < 6`, noul nod devine copilul stâng al lui `6`.

### Complexitate

- O inserare: `O(h + 1)` timp, unde `h` este înălțimea arborelui măsurată în muchii.
- Inserarea a `n` valori într-un BST dezechilibrat poate costa `O(n^2)`, de exemplu la intrarea sortată `[1, 2, 3, 4]`.
- Dacă arborele rămâne echilibrat la construire, inserările costă `O(log n)` fiecare, deci totalul este `O(n log n)`.
- Nodurile ocupă `O(n)` spațiu. Inserarea recursivă folosește încă `O(h + 1)` spațiu pe stiva de apeluri.

## 2. DFS – 94. Binary Tree Inorder Traversal

[Deschide problema LeetCode 94](https://leetcode.com/problems/binary-tree-inorder-traversal/)  
Implementare locală: [`../algorithms/binary_search_tree.py`](../algorithms/binary_search_tree.py), funcția `inorder`  
Soluție LeetCode: [`solutions/94_binary_tree_inorder_traversal.py`](solutions/94_binary_tree_inorder_traversal.py)

Inorder înseamnă: vizităm subarborele stâng, adăugăm valoarea nodului curent, apoi vizităm subarborele drept. Folosim o singură listă `result`, comună tuturor apelurilor recursive; nu construim liste separate pentru fiecare subarbore.

### Trace DFS pentru BST-ul din Problema 1

```text
start 4
  start 2
    start 1
      left None -> return
      add 1
      right None -> return
    return 1
    add 2
    start 3
      left None -> return
      add 3
      right None -> return
    return 3
  return 2
add 4
  start 7
    start 6
      left None -> return
      add 6
      right None -> return
    return 6
  add 7
    start 9
      left None -> return
      add 9
      right None -> return
    return 9
  return 7
return 4

Rezultat: [1, 2, 3, 4, 6, 7, 9]
```

Primul apel nu adaugă valoarea rădăcinii la început: mai întâi parcurge tot subarborele stâng.

### Un arbore binar care NU este BST

```text
    2
   / \
  1   3
 /
4

Inorder: [4, 1, 2, 3]
```

Algoritmul urmează doar legăturile arborelui. Nu sortează valorile. Inorder este sortat pentru un BST valid, deoarece toate valorile din stânga sunt mai mici, iar cele din dreapta sunt mai mari. Pentru un arbore binar obișnuit, această proprietate nu este garantată.

Fiecare nod este adăugat exact o dată: apelul procesează stânga, nodul curent și dreapta, iar un arbore finit fără cicluri are doar subarbori mai mici până la `None`. Timpul este `O(n)`, deoarece fiecare nod este vizitat o singură dată. Stiva recursivă folosește `O(h + 1)` spațiu, iar lista rezultat folosește `O(n)`.

Teste locale: arbore gol, un nod, lanț doar la stânga, lanț doar la dreapta și arborele care nu este BST de mai sus.

## 3. BFS – 102. Binary Tree Level Order Traversal

[Deschide problema LeetCode 102](https://leetcode.com/problems/binary-tree-level-order-traversal/)  
Implementare locală: [`../algorithms/binary_search_tree.py`](../algorithms/binary_search_tree.py), funcția `level_order`  
Soluție LeetCode: [`solutions/102_binary_tree_level_order_traversal.py`](solutions/102_binary_tree_level_order_traversal.py)

BFS folosește o coadă FIFO (`collections.deque`). La începutul fiecărui nivel memorăm `level_size = len(queue)`, apoi scoatem exact atâtea noduri. Pentru fiecare nod adăugăm întâi copilul stâng, apoi copilul drept. Nodurile adăugate în timpul nivelului curent vor fi procesate abia la nivelul următor.

### Trace BFS pentru BST-ul din Problema 1

| Nivel | Coada la început | Noduri eliminate | Rezultat nivel |
|---|---|---|---|
| 0 | `[4]` | `4` | `[4]` |
| 1 | `[2, 7]` | `2`, apoi `7` | `[2, 7]` |
| 2 | `[1, 3, 6, 9]` | `1`, `3`, `6`, `9` | `[1, 3, 6, 9]` |

Coada detaliată după fiecare eliminare și adăugare:

```text
Start: [4]
remove 4; add 2, 7       -> [2, 7]
remove 2; add 1, 3       -> [7, 1, 3]
remove 7; add 6, 9       -> [1, 3, 6, 9]
remove 1                 -> [3, 6, 9]
remove 3                 -> [6, 9]
remove 6                 -> [9]
remove 9                 -> []

Rezultat: [[4], [2, 7], [1, 3, 6, 9]]
```

Salvăm mărimea nivelului înainte de a adăuga copii ca să nu îi procesăm din greșeală în același nivel. FIFO și adăugarea copilului stâng înaintea celui drept păstrează ordinea de la stânga la dreapta. Fiecare nod intră și iese din coadă exact o dată, deci timpul este `O(n)`.

Spațiu de lucru pentru coadă: `O(w)`, unde `w` este numărul maxim de noduri de pe un nivel (coada poate conține părți din două niveluri adiacente). Listele rezultat ocupă separat `O(n)` spațiu. Un arbore gol produce `[]`; arborele non-BST de mai sus produce `[[2], [1, 3], [4]]`.

## Verificare locală

Din directorul principal al repository-ului, rulează:

```bash
python -m unittest lab6.test_trees -v
```

Testele verifică inserarea BST (inclusiv valori negative, duplicate și intrare sortată), inserarea valorii `5`, soluțiile LeetCode cu noduri de tipul așteptat, arbori goi, arbori cu un singur nod, lanțuri și faptul că traversările nu modifică legăturile nodurilor.

## Linkuri LeetCode și submission-uri

- [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) – linkul este pagina problemei; adaugă linkul personal după `Accepted`.
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) – linkul este pagina problemei; adaugă linkul personal după `Accepted`.
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) – linkul este pagina problemei; adaugă linkul personal după `Accepted`.
