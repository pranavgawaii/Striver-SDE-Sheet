# Day 15

## N Meetings in One Room

### Key Idea
Sort all meetings by their end times. Always pick the meeting that ends earliest because it leaves the maximum possible time for remaining meetings.

### Pattern
Greedy Algorithm (Interval Scheduling)

### Complexity
Time: O(N log N)
Space: O(N)

### Revision Note
Sorting by start time does not work; an early starting meeting might last very long and block many other possible shorter meetings.

## Minimum Number of Platforms Required for a Railway

### Key Idea
Sort arrival and departure times independently. Use two pointers to iterate through arrivals and departures, tracking concurrent trains to find the peak overlap.

### Pattern
Greedy Algorithm / Two Pointers

### Complexity
Time: O(N log N)
Space: O(1)

### Revision Note
You do not need to keep track of which train corresponds to which arrival/departure time. We only care about the count of trains at the station.

## Job Sequencing Problem

### Key Idea
Sort jobs descending by profit. For each job, try to schedule it as late as possible (starting from its deadline backwards to day 1) to save earlier slots for other jobs.

### Pattern
Greedy Algorithm

### Complexity
Time: O(N log N + N × max_deadline)
Space: O(max_deadline)

### Revision Note
Doing jobs on their exact deadline or as close to it as possible ensures maximal freedom for scheduling tighter-deadline jobs.

## Fractional Knapsack

### Key Idea
Compute the value-per-weight ratio for each item. Sort items descending by this ratio. Take as much as possible of the highest ratio items, eventually taking a fraction of an item if it doesn't fully fit.

### Pattern
Greedy Algorithm

### Complexity
Time: O(N log N)
Space: O(1)

### Revision Note
This greedy approach works optimally for fractional knapsack but fails for 0/1 knapsack, which requires Dynamic Programming.

## Day Takeaway
Greedy algorithms often rely heavily on sorting input data based on a strategic heuristic (e.g., end time, profit, or value ratio) to make locally optimal choices that guarantee global optimality.
