
 ╦ Graph-Based Problems

1. Traversal / Shortest Path
 BFS for unweighted
 Dijkstra for weighted
 Floyd-Warshall for all-pairs

2. Components / Cycles
 DFS for discovery
 Union-Find for cycle detection

3. Topological Ordering
 Kahn’s Algorithm or DFS + Stack

4. Optimizations
 Kruskal or Prim for MST
 Tarjan’s Algorithm for bridges / articulation points

—— —— —— —— ———— —— —— —— ———— —— —— —— ———— —— —— —— ———— —— —— —— ———— —— —— —— ———— —— —— —— ———— —— —— —— ——— ———— —— —— —— ———— —— —— —— ————


 ╦ Linked List-Based Problems

1. Cycle / Midpoint detection
→ Fast and Slow Pointers

2. Modifications
→ Reverse using prev/curr/next
→ Use Dummy Node for clean insertions

 ╦ Trie-Based Problems (NEW!)

1. Prefix matching / Autocomplete?
→ Use Trie (each node = 1 char, stores path of words)

2. Word search / Dictionary filters?
→ Trie with flags (end of word) and optimized traversal

3. Large input of dictionary words + query set?
→ Preprocess dictionary into a Trie, query each in O(length)

4. Replace / Filter words from sentences?
→ Use a Prefix Trie for fast lookups or filtering

 ╦ Array / String-Based Problems

1. Is the array sorted?
→ Yes → Use:

 Binary Search
 Two Pointers
 Prefix Sum

→ No → Dig into the problem intent.

2. What's the goal?

 Max/Min/Count/Paths? → Dynamic Programming
 Independent Greedy choices? → Try Greedy, prove correctness
 Check if solution exists? → Use DFS, Backtracking, or Binary Search on Answer

3. Special patterns:

 String manipulation? → Stack, Deque, HashMap
 Character-level matching or prefixes? → Trie, Rolling Hash
 Repeated values / unique items? → HashMap, Set
 Subarray sums / windows? → Sliding Window, Two Pointers
 Frequent min/max values? → Heap, Monotonic Queue, Segment Tree

 ╦ Graph-Based Problems

1. Traversal / Shortest Path

 BFS for unweighted
 Dijkstra for weighted
 Floyd-Warshall for all-pairs

2. Components / Cycles

 DFS for discovery
 Union-Find for cycle detection

3. Topological Ordering

 Kahn’s Algorithm or DFS + Stack

4. Optimizations

 Kruskal or Prim for MST
 Tarjan’s Algorithm for bridges / articulation points

  Tree Based Problems
1. Traversals / Queries

 DFS (pre/in/postorder) for recursion

 BFS for level-order or LCA

2. Divide and Conquer?

 Use Postorder DFS

3. Ordered Data or Balancing?

 Use Binary Search Tree or AVL / Red-Black Tree

 Segment Trees or Fenwick Trees for range queries

So, When you get a problem, ask:

What’s the input type?

What’s the desired output?

What kind of decisions am I making?

If you recognize the structure + intent, you’re already halfway there.