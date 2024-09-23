### Insertion Sort

A procedure called insertion-sort which takes as a parameter an array A[1..n] containing the sequence of length `n` that
is to be sorted. In the code n of element is denoted by A.length. The algorithm sorts the input number in place. It
rearranges the number within the array A, with at most a constant number of them stored outside the array at any time. 
The input array A contains the sorted output sequence when the INSERTION-SORT procedure is finished.

#### Pseudocode
```
insertion-sort(A)
    for j = 2 to A.length
        key = A[j]
        // Insert A[j] into the sequence A[1..j-1]
        i = j - 1
        while i > 0 and A[i] > key
            A[i + 1] = A[i]
            i = i -1
        A[i + 1] = key
```

#### Loop invariants and the correctness of insertion sort
The above pseudocode shows how this algorithm works for `A = {5,2,4,6,1,3}`. The index `j` indicate the current 
card being inserted into the hand. A the beginning of each iteration of the for loop, which is indexed by j,
the subarray consisting of of element A[j + 1..n] correspond to the pile of cards on the table.

#### Exercises
#### 2.1 - 1
1. Using the above pseudocode as a model, illustrate the operation of INSERTION-SORT on the array `a = {31, 41, 59, 26, 41, 58}`
`A = {31, 41, 59, 26, 41, 58}`
Pick 59 and use
2. Rewrite the INSERTION-SORT procedure to sort into non-increasing instead of non-decreasing order.
```commandline
TODO: Refactor
insertion-sort(A)
    for j = 2 to A.length
        key = A[j]
        // Insert A[j] into the sequence A[1..j-1]
        i = j - 1
        while i > 0 and A[i] > key
            A[i + 1] = A[i]
            i = i -1
        A[i + 1] = key
```
#### 2.1 - 3
_Consider the searching problem:_
**Input:** A sequence of n  numbers A = {a1,a2,...,an} and a value `v`.<br/>
**Output:** An index i such that v = A[i] or the special value NIL if v does not appear in `A`.
Write pseudocode for linear search, which scans through the sequence, looking for v. Using the loop variant, 
prove that your algorithm is correct.  Make sure that your loop invariant fulfils the three necessary properties.<br/>

```commandline
linear_search(A, v)
    for i = 0 to A.length -1
        if A[i] == v
            return i
    return NIL
```
##### Proofs
**Initialisation:** The target `v` is not found before the loop starts.<br/>
**Maintenance:** A[i], A[i+1], A[i+2] and so on is compared with the target and if any of them match, then the target has been found. Otherwise, its not found.<br/>
**Termination** Finally, if the the list item match the target `v` then we have found the target and so the loop ends. Otherwise, the target was not found.<br/>