# Python Data Structure Analysis
## Disclaimer
AI has not been used in the creation fo this task.

## Assignment Task 1: Linear data structure
**Task:** The first of three tasks to be submitted for the final assessment will be introduced in this session. We will use the first hour to provide explanation and requirements of the task and for you to work on a preliminary version of it.

Implement a Priority Queue according to the stated requirements using the starter project provided.

**Objectives:** Implement the specified programme in code

## Programmer Notes
Variation 1 is based on a bubble sort. Its implementation was very straight forward. I used the w3school's lesson on it as an aid. I am aware that bubble sorts, while one of the easiest to implement, they are also one of the most inefficient algorithms. However, because this data set is so small, the lack of efficiency is not very noticeable. I also concluded that the code cannot be made any more compact or more efficient for this sorting algorithm, as it is so short and changing the way it handles data would no longer make it a bubble sort. 

Variation 2 is based on an insertion sort. Now we are getting slightly more efficient, albeit not by much. While in editor it looks more efficient, due to the smaller amount of code that a bubble sort, it unfortunately runs into the same practical issue as the bubble sort. Whilst good for small and partially sorted data sets, it is very inefficient in larger data lists.  

I wanted to wait until I talked about both my bubble and insertion sort algorithms, before talking about why they are inefficient. Bubble sorts are inefficient due to their excess use of swapping values, taking up a lot of read/write actions, which can also result in caching mistakes in newer hardware. Meanwhile insertion sorts in the worst-case scenario must look at every piece of data again each time an insertion takes place. While it takes less write actions than bubble sort, it takes a lot of read actions, which gets exponentially more the larger the data set. 

Variation 3 is based on a counting sort. A counting sort is more efficient than bubble and insertion sorts, with it being able to handle larger data sets. That being said it will still suffer in larger data groups, as it will have to hold a lot of nested lists. 

Variation 4 is based on a merge sort. This is by far the most complex sort algorithm I have done so far. I genuinely had not a single clue what to do with it. Typically, a merge sort will only take into consideration one sorting value. This is typically fine however, upon implementing and running it, I realised there was an issue. While it did sort the data by priority value, it did not put them in the order required by the main.py script.  

This meant that each value would have to be sorted by value, then al items with the same value would need to be sorted alphabetically. However, this also causes another issue, as main.py will insert new values while in the middle of getting values. This means that when adding a new value, the list cannot be sorted. Whilst that will work for this assignment, it may not be practical in real world uses, but that part of the code is easy to adapt. Overall, this issue is most likely minor, as it pertains to this specific data list and retrieval.  

Out of the four algorithms I have implemented, the merge algorithm is by far the most efficient. While it has taken double the number of lines it took to make the bubble and insertion sort, its efficiency is far greater. Out of all the sorting algorithms it is the fastest and excels at both smaller and larger data sets. The algorithm itself is easily parallelizable, meaning it interacts well with modern multi core CPUs, boosting its efficiency. Moreover, its divide and conquer methodology allows it to perform external sorting, which is where the current data exceeds the main memory's limit, as it can manage data between different memory stores. 

 


