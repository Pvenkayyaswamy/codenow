# Top K Frequent Transactions (Bucket Sort)

## Problem Description

You are building an analytics module for a fintech platform that tracks transaction patterns.

Each transaction is represented by an integer ID. Given an integer array `nums` representing transaction IDs and an integer `k`, return the **k most frequently occurring transaction IDs** from the dataset.

The answer can be returned in **any order**.

---

## Constraints

- `1 <= n <= 10^5` (where `n` is the number of transactions)
- `1 <= k <= number of unique elements`
- The algorithm must perform **better than O(n log n)**.

---

# Why Bucket Sort?

There are three common approaches to solve this problem.

## 1. Brute Force / Sorting Approach — O(n log n)

### How it works
1. Count frequencies using a hash map.
2. Convert the map into a list of `(element, frequency)` pairs.
3. Sort the list in descending order based on frequency.
4. Return the first `k` elements.

### Why not?

Sorting requires **O(n log n)** time, which violates the problem constraint requiring a solution better than **O(n log n)**.

---

## 2. Heap / Priority Queue Approach — O(n log k)

### How it works
1. Count frequencies using a hash map.
2. Maintain a **Min-Heap** of size `k`.
3. Push each element into the heap.
4. Remove the smallest frequency whenever the heap size exceeds `k`.

### Why not?

Although this is efficient, heap operations still introduce a logarithmic factor (`log k`), making the complexity **O(n log k)**.

---

## 3. Bucket Sort (Optimal) — O(n) ⭐

### How it works

Instead of sorting elements, use their frequency as an index.

Since no element can appear more than `n` times, create an array of buckets where:

- Bucket index = frequency
- Bucket value = list of numbers having that frequency

This completely avoids sorting and heap operations.

### Why it wins

- No sorting
- No heap maintenance
- Linear time complexity
- Meets the required constraint

---

# Step-by-Step Algorithm

### Step 1: Count Frequencies

Traverse the array and count how many times each transaction ID appears using a hash map.

Example:

```python
count = {
    1:3,
    2:2,
    3:1
}
```

---

### Step 2: Create Buckets

Create an array of empty lists.

The index of each list represents a frequency.

Maximum possible frequency is `len(nums)`.

```python
buk = [[] for _ in range(len(nums)+1)]
```

---

### Step 3: Populate Buckets

Place each number into the bucket corresponding to its frequency.

Example:

```
Frequency : Numbers

1 -> [3]
2 -> [2]
3 -> [1]
```

---

### Step 4: Collect Top K Elements

Traverse the bucket array **from highest frequency to lowest frequency**.

Whenever a number is found:

- Add it to the result.
- Stop immediately once `k` elements are collected.


---

# Line-by-Line Explanation

### `count = {}`

Creates an empty dictionary to store the frequency of each transaction ID.

---

### `count[num] = count.get(num, 0) + 1`

- Retrieves the current frequency of `num`.
- If it doesn't exist, defaults to `0`.
- Increments the frequency by `1`.

---

### `buk = [[] for _ in range(len(nums)+1)]`

Creates an array of empty lists.

If there are `6` elements in the input, it creates `7` buckets:

```
Index:
0 1 2 3 4 5 6
```

Index represents the frequency.

---

### `buk[fre].append(num)`

Places the transaction ID into the bucket corresponding to its frequency.

Example:

If `1` appears `3` times,

```
buk[3] = [1]
```

---

### `for i in range(len(buk)-1, 0, -1):`

Iterates through the buckets in reverse order.

This ensures higher frequencies are processed before lower frequencies.

---

### `for num in buk[i]:`

Iterates over every number inside the current frequency bucket.

---

### `res.append(num)`

Adds the number to the final answer.

---

### `if len(res) == k:`

As soon as `k` elements are collected, immediately return the result.

This avoids unnecessary traversal.

---

# Complexity Analysis

## Time Complexity — O(n)

- Building the frequency map → **O(n)**
- Filling the buckets → **O(n)**
- Traversing buckets → **O(n)** (worst case)

Overall:

```
O(n) + O(n) + O(n) = O(n)
```

---

## Space Complexity — O(n)

Additional memory used:

- Frequency Hash Map → **O(n)**
- Bucket Array → **O(n)**

Overall:

```
O(n)
```

---

# Key Takeaways

- Use a **Hash Map** to count frequencies.
- Use **Bucket Sort** instead of sorting elements.
- Bucket index represents the frequency.
- Traverse buckets from highest frequency to lowest.
- Stop immediately after collecting `k` elements.
- Achieves the required **O(n)** time complexity, making it more efficient than sorting (`O(n log n)`) or heap-based (`O(n log k)`) approaches.
