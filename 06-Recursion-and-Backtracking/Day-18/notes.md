# Day 18

## Permutations of a String/Array

### Key Idea
Use backtracking to swap elements in place. Fix one element at the current index, recursively permute the rest of the array, and then swap back to restore the original state before moving to the next element.

### Pattern
Backtracking (In-place Swapping)

### Complexity
Time: O(N * N!)
Space: O(N) recursion stack

### Revision Note
In-place swapping is more space-efficient than passing around copies of arrays or using a `visited` boolean array.

## N Queens

### Key Idea
Place queens row by row. Use hash sets to track columns, main diagonals (`row - col`), and anti-diagonals (`row + col`) that are currently under attack to validate board states in O(1) time.

### Pattern
Backtracking (State Tracking via Hash Sets)

### Complexity
Time: O(N!)
Space: O(N) for board state and hash sets

### Revision Note
The mathematical property of diagonals is the secret here: `row - col` is constant for any main diagonal, and `row + col` is constant for any anti-diagonal.

## Sudoku Solver

### Key Idea
Iterate through the board. When an empty cell is found, try placing digits '1' through '9'. Use a validation function to check the current row, column, and 3x3 subgrid. Recursively solve; if successful, return true, else undo and backtrack.

### Pattern
Backtracking (2D Grid)

### Complexity
Time: O(9^(Empty Cells))
Space: O(81) recursion stack (effectively O(1))

### Revision Note
The nested `for` loops inside the recursive function return `True` when the board is completely filled. If no digit fits an empty cell, return `False` immediately to prune the branch.

## Day Takeaway
Classic backtracking often requires careful management of state (undoing modifications after the recursive call) and pruning invalid paths as early as possible.
