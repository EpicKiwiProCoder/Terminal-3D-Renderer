import numpy as np
import math, os, time

letters = "#$~.j+"

def rotateZ(original, a):
    rotateZ = np.array([[math.cos(a), math.sin(a), 0], 
                     [-math.sin(a), math.cos(a), 0],
                     [0,0,1]])
    return np.matmul(rotateZ, original)

def rotateY(original, a):
    rotateY = np.array([[math.cos(a), 0, math.sin(a)], 
                     [0, 1, 0],
                     [-math.sin(a), 0, math.cos(a)]])
    return np.matmul(rotateY, original)

def rotateX(original, a):
    rotateX = np.array([[1, 0, 0], 
                     [0, math.cos(a), -math.sin(a)],
                     [0, math.sin(a), math.cos(a)]])
    return np.matmul(rotateX, original)

def rotatePoints(points, x, y, z):
    rotated = []
    for point in points:
        zRot = rotateZ(point, math.radians(z))
        yRot = rotateY(zRot, math.radians(y))
        xRot = rotateX(yRot, math.radians(x))
        rotated.append(xRot)
    return rotated

def contains(array, given):
    isTrue = False
    for current in array:
        isTrue = np.array_equal(current, given) or isTrue
    return isTrue


def forwardFacing(vertex):
    val = (float(vertex[1][1] - vertex[0][1]) * (vertex[2][0] - vertex[1][0])) - \
           (float(vertex[1][0] - vertex[0][0]) * (vertex[2][1] - vertex[1][1]))
    if (round(val,2) < 0):
        return True
    elif (round(val,2) >= 0):
        return False

def area(coord1, coord2, coord3):
    return abs((coord1[0] * (coord2[1] - coord3[1]) + coord2[0] * (coord3[1] -           coord1[1]) + coord3[0] * (coord1[1] - coord2[1])) / 2.0)

def inside(coordinate, points):
    letterIndex = 0
    for indecies in vertecies:
        vertex = ( points[indecies[0]], points[indecies[1]], points[indecies[2]])
        if forwardFacing(vertex): #  == forwardFacing(vertex)
            A = area( vertex[0],  vertex[1],  vertex[2])
            A1 = area(coordinate,  vertex[1],  vertex[2])
            A2 = area( vertex[0], coordinate,  vertex[2])
            A3 = area( vertex[0],  vertex[1], coordinate)
            if round(A, 3) == round(A1 + A2 + A3, 3):
                return letters[int(letterIndex)]
        letterIndex += 0.5
    return " "

points = [np.array([-1,-1,1]), 
          np.array([1,-1,1]), 
          np.array([1,1,1]), 
          np.array([-1,1,1]), 
          np.array([-1,-1,-1]), 
          np.array([1,-1,-1]), 
          np.array([1,1,-1]), 
          np.array([-1,1,-1])]
vertecies = [(0,1,2), (2,3,0), # front
             (5,4,7), (7,6,5), # back
             (4,5,1), (1,0,4), # top
             (3,2,6), (6,7,3), # bottom 
             (4,0,3), (3,7,4),
             (1,5,6), (6,2,1)
            ] 

for i in range(1000):
    startTime = time.time()
    rotatedPoints = rotatePoints(points, i, i*10, i*10)
    #time.sleep(.1)
    valueTable = []
    for x in np.arange(-1.6, 1.6, 0.2):
        row = []
        for y in np.arange(-1.6, 1.6, 0.1):
            row.append(inside(np.array([round(x,2), round(y,2)]), rotatedPoints))
            
        row.append("\n")
        valueTable.append(row)
    os.system('clear')
    for row in valueTable:
        for letter in row:
            print(letter, end="")
    elapsedTime = time.time() - startTime
    print(f"{round(1/elapsedTime, 1)} FPS")
