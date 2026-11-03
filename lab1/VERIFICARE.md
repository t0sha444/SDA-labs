# Verificare locală

Exemplele de mai jos pot fi folosite pentru o verificare rapidă înainte de trimiterea pe LeetCode.

## Problema 1480

```python
sol = Solution()
print(sol.runningSum([1, 2, 3, 4]))  # [1, 3, 6, 10]
```

## Problema 27

```python
sol = Solution()
nums = [3, 2, 2, 3]
k = sol.removeElement(nums, 3)
print(k)        # 2
print(nums[:k]) # [2, 2]
```

La problema 27, partea din listă după indexul `k - 1` nu contează, conform cerinței LeetCode.
