import numpy as np

'''
#__Example__

Y = 5
g = 10
positions = np.array([(0,5),(0,4),(1,4),(2,3),(3,3),(4,2),
                  (4,1),(5,0)])
velocities = np.array([])

for i in range(0,8):
    velocities = np.append(velocities, np.sqrt(2*g*(Y - positions[i][1])))
    

delta_times = np.array([])
for i in range(0, 7):
    pos_change = np.sqrt((positions[i][0] - positions[i+1][0])**2 + (positions[i][1] - positions[i+1][1])**2)
    av_velocity = (velocities[i] + velocities[i+1])/2
    delta_times = np.append(delta_times, pos_change/av_velocity)

print(np.sum(delta_times))
'''

def time_taken(positions):
    Y = 8
    g = 10
    
    velocities = np.array([])

    path_length = np.size(positions)//2

    for i in range(0, path_length):
        velocities = np.append(velocities, np.sqrt(2*g*(Y - positions[i][1])))

    delta_times = np.array([])
    for i in range(0, path_length - 1):
        pos_change = np.sqrt((positions[i][0] - positions[i+1][0])**2 + (positions[i][1] - positions[i+1][1])**2)
        av_velocity = (velocities[i] + velocities[i+1])/2
        delta_times = np.append(delta_times, pos_change/av_velocity)
    
    print(np.sum(delta_times))

#__Question1__#

positions_1 = np.array([(0,8),(1,7),(2,7),(3,6),(3,5),
                        (4,5),(4,4),(5,4),(6,4),(6,3),
                        (6,2),(7,2),(8,2),(8,1),(8,0)])

#time_taken(positions_1) #Output of: 2.2857699492421855 seconds

#__Question2__#

positions_2 = np.array([(0,8),(0,7),(0,6),(1,6),(2,6),
                        (3,6),(3,5),(4,5),(5,4),(6,4),
                        (6,3),(7,2),(8,2),(8,1),(8,0)])

#time_taken(positions_2) #Output of: 2.160612738156833 seconds

W = np.array([[0,0,0,0,0,0,0,0,0],
             [1,4,3,5,2,5,5,2,5],
             [5,2,2,5,1,1,2,3,3],
             [3,4,3,3,4,5,2,2,5],
             [3,1,4,2,1,3,4,5,1],
             [3,3,3,5,1,1,5,2,4],
             [5,2,3,2,3,2,2,5,3],
             [3,2,2,3,1,4,3,2,2],
             [2,4,3,1,1,3,3,4,1]])

#Since time of path 2 < time of path 1 
for i in range(0, np.size(positions_1)//2):
    W[8-positions_1[i][1]][positions_1[i][0]] -= 1
    
for i in range(0, np.size(positions_2)//2):   
    W[8-positions_2[i][1]][positions_2[i][0]] += 1

#print(W)
'''
Updated Matrix:

[[0 0 0 0 0 0 0 0 0] : 8
 [2 3 2 5 2 5 5 2 5] : 7
 [6 3 3 5 1 1 2 3 3] : 6
 [3 4 3 3 4 5 2 2 5] : 5
 [3 1 4 2 0 3 4 5 1] : 4
 [3 3 3 5 1 1 5 2 4] : 3
 [5 2 3 2 3 2 1 5 3] : 2
 [3 2 2 3 1 4 3 2 2] : 1
 [2 4 3 1 1 3 3 4 1]] : 0
 '''
 
'''
positions_3 = np.array([(0,8),(1,7),(2,6),(3,6),(4,5),
                        (5,5),(6,4),(7,4),(8,3),(8,2),
                        (8,1),(8,0)])
'''
positions_3 = np.array([(0,8),(1,7),(1,6),(1,5),(2,4),
                        (3,3),(4,2),(5,1),(6,0),(7,0),
                        (8,0)])

#time_taken(positions_3) #Output of: 1.8113617557731199 seconds

#since 3 < 2 < 1
positions_1 = positions_2
positions_2 = positions_3

for i in range(0, np.size(positions_1)//2):
    W[8-positions_1[i][1]][positions_1[i][0]] -= 1
    
for i in range(0, np.size(positions_2)//2):   
    W[8-positions_2[i][1]][positions_2[i][0]] += 1

print(W)