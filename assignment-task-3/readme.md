# Python Data Structure Analysis
## Disclaimer
AI has not been used in the creation fo this task.

## Assignment Task 3
### Task:
Implement Dijkstra's Algorithm in code

### Requirements
Using Dijkstra's Algorithm as a base, fill in the walk() function within graph.py. It must return the shortest possible path between the start and end target.

## Programmer Notes
For attempt 1, I decided to try and follow w3school's tutorial on Dijkstra's Algorithm. The tutorial can be found here: https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php 

In the tutorial, there are 2 parts; making a graph and implementing Dijkstra's Algorithm. As we have already been given a graph and told not to edit it, I will have to attempt to work around this. As previously stated this was attempt 1, which means it is not the final product. This is simply becuase I could not get the tutorial from w3schools to implament properly. 

To be fair, it's not a bad thing. They do towards the bottom of their tutorial include their code. That would most definitely count as plagarism. While I won't be using their tutorial to do this, I now understand Dijkstra's Algorithm a bit better. 

Moving onto attempt 2, I decided to look at the reccomended aid here: https://en.wikipedia.org/wiki/Dijkstra's_algorithm#:~:text=%5B17%5D-,Algorithm,-%5Bedit%5D

The reason I didn't do this first, is that the wikipedia's algorithm guide is honestly not very helpful. The wording is clunky and it's like reading a puzzle. Ppart of my issue was that I had trouble visuallising how sets worked. It also didn't help that I forgot that in sets data positions are randomised.

Suffice to say, attempt 2 didn't go much better. Before attempting this for a third time, I asked for a little help. My good friend and peer Ella-Rae Walden, who had done Com Sci at A-Level was somewhat familliar with the process of making this work. 

I asked her for a little help with explaining the steps of how to implament the required cod. I also requested that she didn't outright give me the answer, as that would not teach me anything. 

Therefore, she gave me the steps she used for her project, see ln44 - 56 in graph.py. Along with the suggestion to make the distance and previous variables into dictionaries for simpler referancing. Finally she said that while the given wikipedia aid for the main code wasn't good at explaining, she did say that the psuedo code for the path return was spot on.

Taking her much appreciated advidce, I began to the code, following her suggested steps. I created a new set named unvisited and stored all the vertex from the graph inside it, cloning the self.verteces variable. Next I created two dicitionaries, one to hold the unvisited variables and one to hold the already visited vertices and which vertex they were visited from.

Prior to this, I had made the distance and previous variables as lists. I belive that in previous attempts, this may have been where I went wrong. To fill these two dictionaries, I would have to use a for loop, as my usual methodology for filling lists and arrays wouldn't work here. I made sure to make every disance ininite and every piece of data in previous effectively empty, like who the wikipedia article instructs. Following that logic, I made the distance from start to start 0, as we are already there, therefore we don't have to travel.

Moving onto the bulk of the code, I had to make sure that the algorithm would loop though the entire unvisited set. This is easy to do, as whenever the code is done visiting a vetex, it is removed from unvisited and added to previous. Therefore making a while loop that runs until unvisitedd is empty works best here.

Inside the while loop, I needed to implament steps 3 - 5. Step 3 was sort, although it did take me a little bit into testing to realise that I needed to add the `and n in unvisited` condition inside the for loop, otherwise the code would look at previously visited vertices. That would result in the code potentially going back to the start, rather than moving forwards. 

Moving onto step 4, I now need to calcullate which neighbouring vertex is the closest (shortest distance from current vertex). However I first needed to make sure that the current vertex is the one we want to reach. If it is, the distance is stored and the while loop ends. Otherwise it'll check all the attached vertices inside the graph's adjacency list. After that, it will see if the vertex is in unvisited. When the neighbour is unvisited, check to see if this neighbour's distance is smaller than the current smallest. If it is smaller, that vertex will be the next visited, unless one of the other neighbours is even closer.

Once the neighbours have been checked and the next vertex has been selcted, the current node is now visited. That means it is removed from unvisited and put into previous.

Once every node has been checked or visited, it is time to calculate the path taken. The pseudocode given by the wikipedia article is the most concise way of doing this that I found. I don't think it is worth explaining here, as I put the pseudocode into the script while programming an kept it there. 

Agin I want to give some credit and thanks to Ella-Rae Walden for graciously giving some of her notes to me, whilst not telling me exactly what to do. 