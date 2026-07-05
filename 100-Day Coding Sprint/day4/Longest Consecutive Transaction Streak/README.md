# 🚀 Longest Consecutive Transaction Streak

An optimal solution to find the longest sequence of consecutive integers in an unsorted array in $\mathcal{O}(n)$ time and $\mathcal{O}(n)$ space.

---

## 💡 The $\mathcal{O}(n)$ Approach (Hash Set)

Instead of ordering the elements, this approach utilizes a **Hash Set** to store all transaction IDs. A set provides **$\mathcal{O}(1)$ constant-time lookups**, allowing the algorithm to instantly check whether a specific number exists.

To achieve a true linear runtime where each element is visited at most a couple of times, the algorithm uses a crucial optimization: **it only initiates a streak count if the current number represents the absolute beginning of a sequence.**

### How It Works:
1. **Deduplicate & Index:** Convert the input array `nums` into a set. This removes duplicates and prepares the elements for fast lookups.
2. **Identify Sequence Starters:** Iterate through the unique numbers in the set. For each number `num`, check if `num - 1` is present.
   * If `num - 1` **exists**, `num` belongs to the middle of an ongoing sequence. Skip it immediately.
   * If `num - 1` **does not exist**, `num` is verified as the **start** of a brand-new sequence.
3. **Scan and Count:** Only when a valid starter is identified, a nested `while` loop checks sequentially for `num + 1`, `num + 2`, and so on, keeping track of the current streak's length.
4. **Track the Maximum:** Update the global maximum streak counter if the current sequence length exceeds the previous record.

### Complexity Analysis:
* **Time Complexity:** $\mathcal{O}(n)$ — Even though there is a nested `while` loop inside a `for` loop, the inner loop only fires for the *first* element of any consecutive streak. As a result, each transaction ID is processed at most twice across the entire execution.
* **Space Complexity:** $\mathcal{O}(n)$ — Required to maintain the unique numbers within the Hash Set.

---

## 🚫 Why Not Via Sorting?

While sorting the array in ascending order seems like an intuitive first step to align consecutive numbers, it is fundamentally flawed for this problem due to strict performance boundaries:

1. **Violates the Time Constraints:** The problem explicitly demands an **$\mathcal{O}(n)$ time complexity**. Comparison-based sorting algorithms (such as Timsort used by Python's native `.sort()` or `sorted()`) operate at **$\mathcal{O}(n \log n)$** time. For large datasets (e.g., $n = 10^5$), an $\mathcal{O}(n \log n)$ approach triggers millions of extra operations, resulting in a **Time Limit Exceeded (TLE)** failure on strict evaluation platforms.
2. **Unnecessary Computational Overhead:** Sorting forces the system to fully organize and rearrange every single independent partition of the array relative to each other. Because the objective only requires finding the *length* of adjacent sequential chains—regardless of where they sit globally—sorting the entire list introduces massive, wasted computational effort.
