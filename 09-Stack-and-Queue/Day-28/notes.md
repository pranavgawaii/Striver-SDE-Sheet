# Day 28

## Stock Span Problem

### Key Idea
Maintain a stack of pairs `(price, span)`. When a new price comes in, while the stack is not empty and the top price is less than or equal to the new price, pop from the stack and add the popped span to the current span. Finally, push the new `(price, span)` and return the span.

### Pattern
Monotonic Stack

### Complexity
Time: O(N) where N is the number of calls to `next`, because each price is pushed and popped at most once.
Space: O(N) for the stack.

### Revision Note
Storing the span explicitly with the price in the stack avoids needing to keep track of absolute indices, making it perfect for streaming data (like an online algorithm).

## Maximum of Minimums for Every Window Size

### Key Idea
For each element, find the index of the next smaller element on the left and right using monotonic stacks. This tells us the maximum window size where the current element is the minimum. We create an array `ans` where `ans[length]` stores the max element. We then fill in the gaps by iterating backwards: `ans[i] = max(ans[i], ans[i+1])`.

### Pattern
Monotonic Stack (Next/Previous Smaller Element)

### Complexity
Time: O(N)
Space: O(N)

### Revision Note
The backward iteration `ans[i] = max(ans[i], ans[i+1])` is the crucial step. If an element is the maximum of minimums for a window of size `K`, it is also a valid candidate for any window of size less than `K`.

## Celebrity Problem

### Key Idea
Push all people into a stack. Pop two people `a` and `b`. If `a` knows `b`, `a` cannot be a celebrity, so push `b` back. If `a` doesn't know `b`, `b` cannot be a celebrity, so push `a` back. Repeat until one person is left. This is the potential candidate. Verify the candidate by checking if they know no one and everyone knows them.

### Pattern
Stack (Elimination)

### Complexity
Time: O(N)
Space: O(N) for the stack (can be optimized to O(1) using two pointers)

### Revision Note
This is a classic elimination tournament. Every query eliminates exactly one person from being the celebrity, reducing the search space from N to 1 in exactly N-1 queries.
