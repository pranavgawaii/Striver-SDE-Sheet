# Day 13

## Rotate a Linked List

### Key Idea
Find the length and tail, compute effective rotation `k % length`, then break the list at `length - k` position and re-link the tail to the original head.

### Pattern
Tail connection + split at offset

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Always reduce k modulo length first — without this, k larger than the list length causes unnecessary full rotations.

## Clone a LL with Random and Next Pointer

### Key Idea
Interleave cloned nodes between original nodes (A → A' → B → B'), assign random pointers using the interleaved structure, then separate the two lists.

### Pattern
In-place interleaving (3-pass)

### Complexity
Time: O(N)
Space: O(1) auxiliary (excluding the output list)

### Revision Note
The interleaving trick avoids a hash map by placing each clone directly after its original, so `curr.random.next` always points to the clone of `curr.random`.

## 3 Sum

### Key Idea
Sort the array, fix one element, then use two pointers on the remaining subarray to find pairs that sum to the negative of the fixed element. Skip duplicates at every level.

### Pattern
Sort + Two pointers

### Complexity
Time: O(N²)
Space: O(1) auxiliary

### Revision Note
Skip duplicates for the outer loop (`nums[i] == nums[i-1]`) and inner pointers (`nums[left] == nums[left+1]`) to avoid repeated triplets without using a set.

## Day Takeaway
Interleaving nodes is a powerful O(1) space technique for cloning complex linked structures, and the sort + two-pointer pattern reduces 3 Sum from O(N³) brute force to O(N²).
