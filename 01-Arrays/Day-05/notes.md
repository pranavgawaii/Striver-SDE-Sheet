# Day 5

## Search in a 2D Matrix

### Key Idea
Treat the sorted 2D matrix as a virtual 1D flattened array and run a standard binary search, calculating the row and column indexes on the fly.

### Pattern
Flattened coordinate binary search

### Complexity
Time: O(log (M * N))
Space: O(1)

### Revision Note
Map virtual 1D index `mid` to 2D coordinates with `r = mid // cols` and `c = mid % cols`.

## Pow(x,n)

### Key Idea
Calculate standard exponentiation by squaring the base product and halving the exponent iteratively to speed up powers.

### Pattern
Binary Exponentiation

### Complexity
Time: O(log N)
Space: O(1)

### Revision Note
Handle negative powers immediately by inverting the base (`x = 1 / x`) and taking the absolute value of `n`.

## Majority Element

### Key Idea
Iterate through the array maintaining a candidate element and a vote weight counter, shifting candidate values as weight hits zero.

### Pattern
Boyer-Moore Voting Algorithm

### Complexity
Time: O(N)
Space: O(1)

### Revision Note
Increment the vote weight if the value matches the candidate, else decrement, resetting the candidate when weight is zero.

## Day Takeaway
Logarithmic algorithms like binary search and binary exponentiation are critical for handling scaling constraints under minimal space conditions.
