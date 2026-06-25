# Day 25

## Balanced Parenthesis

### Key Idea
Use a stack to keep track of opening brackets. When encountering a closing bracket, check if the stack is non-empty and the top of the stack is the corresponding opening bracket. If it is, pop from the stack. Otherwise, return false. After iterating through the string, the stack should be empty.

### Pattern
Stack (LIFO tracking)

### Complexity
Time: O(N)
Space: O(N)

### Revision Note
A hash map mapping closing brackets to their opening counterparts makes the logic much cleaner than using multiple `if/elif` statements.

## Next Greater Element

### Key Idea
Iterate through the array backwards. Maintain a stack of elements seen so far. For the current element, pop elements from the stack that are smaller or equal to it, since they can no longer be the "next greater" for any elements coming before the current one. The top of the stack is now the next greater element. Push the current element to the stack.

### Pattern
Monotonic Stack

### Complexity
Time: O(N) because each element is pushed and popped at most once.
Space: O(N)

### Revision Note
A monotonic decreasing stack is the standard way to find the next greater element efficiently. Store the results in a hash map for O(1) lookups if querying multiple specific elements.

## Sort a Stack

### Key Idea
Use recursion. The base case for sorting is an empty stack. To sort, pop the top element, recursively sort the remaining stack, and then insert the popped element back into its correct sorted position using another recursive helper function.

### Pattern
Recursion (Implicit Stack)

### Complexity
Time: O(N^2) in the worst case
Space: O(N) for the recursion call stack

### Revision Note
The recursive approach elegantly avoids using an explicit temporary stack (though it uses the call stack). The `insert_sorted` function assumes the stack below it is already sorted.

## Day Takeaway
Stacks are perfect for problems involving matched pairs (parentheses), maintaining a monotonic sequence (next greater element), and reversing or ordering elements through recursive unwinding.
