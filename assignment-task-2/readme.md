# Python Data Structure Analysis
## Disclaimer
AI has not been used in the creation fo this task.

## Assignment Task 2
### Task:
implement the code specified in the Week 8 - Numpy and Task 2 lecture. See recording for more details.

### Dependancies
    NumPy<br>
    PyGame

### Requirements
Make the astroids move in a random direction (astroid.py)

Have the ship follow the cursor, with cursor distance affecting the speed (ship.py)

Always have the ship pointing at the cursor (utils.py)

## Programmer Notes
**DO NOT CHANGE ANYTHING OUTSIDE OF THE __init__ and update() LOOP**

## Working Process
For the first requirement, the changes to the script were overall easy and minimal. Firstly, there needed to be a new static variable for each asteroid which stored the direction it would be heading, using a NumPy array for the x and y values. As I am working with a float instead of an integer, I had to do a little searching for how to get a random float. 

After a quick couple of google searches, I discovered random. Uniform(). This allowed me to get the X and Y values needed. Afterwards, it was a simple addition between the self.pos and the X, Y direction.

Moving onto the second requirement, this is where things started to get more complicated for me. This is wholly because I have never worked in PyGame before. Thankfully for this I do not need to understand the entirety of the module, just how the mouse works.  

Upon learning how to use pygame.mouse.get_pos(), I immediately used it to extract the X and Y coords into two variables. I then realised that the mouse position was already fed into the function through the mouse_pos parameter. Therefore, I modified my small amount of code to account for it. I then added two lines of code (ln 28 + 29), which would update the position of the ship every update() cycle.  

When running this code, I ran into an issue. The ship would move in one direction but would never stop. I realised that this was because the angle between the mouse and ship was never updated. When looking through ways of updating the angle using NumPy, a function called arctan2. While my reasoning may sound quite simplistic, I mostly chose this as it creates a tangent arc between two vectors. Also sin and cos were being used in the movement. This is not the soundest logic, and it was a wild guess, it did pay off. 

However, when re-running the code, it did act strangely, as I got the sin and cos mixed up. I then tried several combinations of the two, until I found one which worked. After fixing this error, I had one more problem; jittering movement.  

This is where I really started to struggle, as I could not figure out how to stop the jitter. After perusing the internet for about 30 mins, looking at several different projects, I noticed that a common fix was using an if statement finding the straight line created by the distance variable. After looking at how to do this was much easier now and the math.hypot()'s formula was the shorthand version of exactly what I needed.  

Now all I needed to do was in the case that the movement inside an if clause, which checked whether the "straight line" had a distance greater than 0. If it does, then move the ship. This completely solved the jittering issue.
 
Now for the next part all I needed to do was have the speed adjust based on the distance from the mouse. The further away the mouse is, the faster the ship moves and the opposite being true too. This was by far the easiest feature of the second part, as all I had to do was multiply the "straight line" value by a modifier to get the new speed value. This worked; however, it took several attempts to get the speed exactly right, eventually settling on a 0.05 multiplier. 

For the final part of this task, I need to have the ship perpetually point at the mouse. To do this, I need to calculate the angle between the cursor's position and the ship's position. Most of this has already been done, meaning I just need to fill in the code for the rotate() function in utils.py. This was incredibly easy, as we had previously been taught how to rotate two vectors. For more on that, you can look at `other-files\week_7-Linear_Algebra_2\linear algebra 2.ipynb` in section 3b. 

Now it was at this point that I realised something was going wrong with the rotation. When rotating, the ship would very rarely face the cursor, and it would only rotate some of the time. It turns out, when calculating the ArcTan2(), I had forgotten that it calculates all the angles counterclockwise. To rectify this, I added NumPy.pi to the ArcTan2() result, which fixed the rotational issue. The way in which it solves this issue is that instead of calculating the inverse angle, which is what ArcTan2() was doing, by adding pi it again inverts the angle again, giving the desired angle. 
