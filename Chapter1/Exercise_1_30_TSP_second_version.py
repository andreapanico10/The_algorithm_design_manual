''' This is the second version of the TSP algorithm, Closest pair strategy.
1.30: Implement the two TSP heuristics of Section 1.1 (page 5). 
Which of them gives better solutions in practice? 
Can you devise a heuristic that works better than both of them?

A different idea might repeatedly connect the closest pair of endpoints 
whose connection will not create a problem, such as premature termination of the cycle. 
Each vertex begins as its own single vertex chain. After merging everything together, 
we will end up with a single chain containing all the points in it. 
Connecting the final two endpoints gives us a cycle. At any step during the execution
of this closest-pair heuristic, we will have a set of single vertices and the end of
vertex-disjoint chains available to merge. In pseudocode:'''


# It doesn't work, come back after study graph theory#
import numpy as np
import matplotlib.pyplot as plt

points = [[0,1], [10,10], [3,3], [7,2], [2,7], [4, 9] ] #Starting array

all_distances = []
for i in range(len(points)):
    d = np.inf
    s = points[i]

    other_points = points.copy()
    other_points.remove(s)

    for t in other_points:
        if(np.linalg.norm(np.array(s)-np.array(t)) < d):
            d = np.linalg.norm(np.array(s)-np.array(t))
            print(s,t)
    all_distances.append(d)
print(sum(all_distances))
'''Execution Times without printing:
- between 0.115 and 0.147 seconds     

print('Total distance: {}'.format(np.round(sum(distances),2)))
plt.figure()
xs = [x[0] for x in ordered_points]
ys = [x[1] for x in ordered_points]
labels = np.arange(1,len(xs))

plt.plot(xs,ys)
plt.scatter(xs,ys, label=labels)

iter = 0
for x,y in zip(xs[:-1],ys[:-1]):

    label = "{:}".format(labels[iter])

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    iter += 1
plt.show()
'''

