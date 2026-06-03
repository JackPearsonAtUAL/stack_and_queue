# Python Data Structure Analysis
## Assignment Task 1: Linear data structure
**Task:** The first of three tasks to be submitted for the final assessment will be introduced in this session. We will use the first hour to provide explanation and requirements of the task and for you to work on a preliminary version of it.

Implement a Priority Queue according to the stated requirements using the starter project provided.

**Objectives:** Implement the specified programme in code

## Programmer Notes
I havent done any sorting algorithm since I was doing GCSE Com Sci, so I needed a refresher. I did thi by looking at w3schools's Python DSA section on sorting algorithms (https://www.w3schools.com/python/python_dsa.asp). Then I went to google to figure out which ones were stable sorting algorithms, as I did not want to run the risks involved with unstable sorts.

Variation 1 is based on a bubble sort. It's implamentation was very straight forward. I used the w3school's lesson on it as an aid. I am aware that bubble sorts, while one of the easiest to implament, they are also one of the most inefficeint algorithms. However becuase this data set is so small, the lack of efficiency is not very noticeale. I also came to the conclusion that the code can't be made any more compact or more efficient for this sorting algorithm, as it is so short and changing the way it handles data would no longer make it a bubble sort.


Variation 2 is based on an insertion sort. Now we're getting slightly more efficient, albeit not by much. While in editor it looks more efficient, due to the smaller amount of code that a bubble sort, it unfortunately runs into the same practical issue as the bubble sort. Whilst good for small and partially sorted data sets, it is very inefficient in larger data lists. 

I wanted to wait until I talked about both my bubble and insertion sort algorithms, before talking about why they're inefficient. Bubble sorts are inefficient due to their excess use of swapping values, taking up a lot of read/write actions, which can also result in caching mistakes in newer hardware. Meanwhile insertion sorts in the worst case senario have to look at every piece of data agin each time an inseretion takes place. While it takes less write actions than bubble sort, it take a lot of read actionss, which gets expanentially more the larger the data set.

Variation 3 is based on a counting sort. A counting sort is more efficient than bubble and insertion sorts, with it being able to handle larger data sets. That being said it will still suffer in larger data groups, as it will have to hold a lot of nested lists.

Variation 4 is based on a merge sort. This is by far the most complex sort algorithm I have done o far. I genuinely had not a single clue what to do with it. Typically a merge sort wil only take into consideration one sorting value. This is typically fince, however Upon implamenting and running it, I realised there was an issue. While it did sort the data by priority value, it did not put them in the order required by the main.py script. 

This meant that each value would have to be sortd by value, then al items with the same value would need to be soreted alphabetically. However this also causes another issue, as main.py will instert new values while in the middle of getting values. This means that when adding a new value, the list can't be sorted. Whilst that will work for this assignment, it may not be practical in real world uses, but that part od the code is easy to adapt. Overall this issue is most likely minor, as it pertains to this specific data list and retrival. 

Out of the four algorithms I've implamented, the merge algorithm is by far the most efficient. While it has taken roughtly double the number of lines it tookto make the bubble and inisertion sort, it's efficiency is far greater. Out of all the sorting algorithms it is the fastest and excells at both smaller and larger data sets. The algorithm itself is easily parallelizable, meanig it interact well with modern multi core CPUs, boosting its efficiency. Moreover, its diveide and conquer mothodology allows it to perform external sorting, which is where the current data exceeds the main memory's limit, as it can manage data between different memory stores. 


