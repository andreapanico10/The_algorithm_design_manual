''' This is the first version of the TSP algorithm, nearest neighbor strategy
1.30: Implement the two TSP heuristics of Section 1.1 (page 5). 
Which of them gives better solutions in practice? 
Can you devise a heuristic that works better than both of them?'''
import numpy as np
import matplotlib.pyplot as plt

points = [[0,1], [10,10], [3,3], [7,2], [2,7], [4, 9] ] #Starting array
actual_point = points [0]

points.remove(actual_point)
ordered_points = []
ordered_points.append(actual_point)

counter = 0

while len(points) > 0: # while there are unvisited points
    distances = []
    for point in points: # Calculate Euclidean distances
        distances.append(np.linalg.norm(np.array(actual_point)-np.array(point)))
    i = np.argmin(distances)

    actual_point = points[i]
    counter +=1 

    points.remove(actual_point)
    ordered_points.append(actual_point)

#come back to the starting point
ordered_points.append(ordered_points[0])
# and add final distance
distances.append(np.linalg.norm(np.array(actual_point)-np.array(ordered_points[0])))

'''Execution Times without printing:
- between 0.115 and 0.147 seconds     '''

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

