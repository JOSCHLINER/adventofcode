For Day Seventeen I couldn't come up with how to solve the general problem myself. I therefore looked up how other people
solved the problem and wrote the code. As it isn't really my code I don't think I should post the code in my repository 
as this I would take credit for work I didn't do. I used this [video guide](https://www.youtube.com/watch?v=2pDSooPLLkI)
by HyperNeutrino on YT which gives a rough explanation of the problem. Even though I don't feel comfortable sharing the
code, I still want to save how "I" solved it, Advent of Code is an learning experience after all, isn't it? 


# Star One
This problem can be solved using Dijkstra’s Algorithm. The way we do it is by having a priority que where the smallest
element always is on top, and by having a set for all the tiles we have visited, taking into account on how we have
visited them with the direction we are going and how often we have gone in that direction, to not loop around
indefinitely.
First we check if we can move further in the direction we are going by checking if we have moved in that direction three
or more times. If we can still move in that direction we add the next tile to our stack, with the heatloss counter and 
steps taken in the same direction adjusted.
Thereafter, we go to out left and right tile (from the current direction we are facing). We push the values of the next 
point on the que with the direction, heatmap and step counter adjusted.

This cycle continues until the priority que is empty, but as we always push new elements on top of it this will never
happen. We know that we have found the right answer if we come to the end tile, this is because we are using a priority
que, which means that the smallest value will always be on top.

# Star Two
This is almost the same code as Star One, the biggest difference is that before going left or right we first check if 
we have moved at least four steps in the direction we are currently facing. We also adjust the constraints for moving
forward to check if we have moved less or equal to ten steps in said direction. The last modification we have to
undertake is to check if we have moved at least for steps into one direction when coming onto the winning tile to
satisfy the problems constraints.
