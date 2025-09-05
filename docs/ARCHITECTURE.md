# Architecture — Milestone 1

- **Trie** for prefix-based autocomplete
- **Heap** for top-k ranking by goals/points
- **HashMap** for exact O(1) lookups
- Complexity:
  - Insert: O(L) per word (L = length)
  - Autocomplete: O(P + R) (P = prefix length, R = number of results)
  - Top-K: O(N log K)
