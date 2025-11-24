import numpy as np


def centroid(p1x, p1y, p2x, p2y, p3x, p3y, m1, m2, m3):
    
    
    positions = np.array([[p1x, p2x, p3x],
                          [p2x, p2y, p3y]]) #2D
    
    masses = np.array([m1, m2, m3]) #1D
    
    tot_mass = np.sum(masses)
    
    cx = np.sum(positions[0,:] * masses) / tot_mass   # 1.rowu çekiyor [0,:]
    cy = np.sum(positions[1,:] * masses) / tot_mass   # 2.rowu çekiyor [1,:]
    
    return tot_mass, cx, cy

test = centroid(1,1,0,1,1,0,3,4,100)