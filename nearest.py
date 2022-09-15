import random


def distance(x1, y1, x2, y2):
    x_dist = x1 - x2 if x1 - x2 > 0 else (x1 - x2) * -1
    y_dist = y1 - y2 if y1 - y2 > 0 else (y1 - y2) * -1

    return x_dist, y_dist

def nearestWave(point, points, dist):
    x1, y1 = point
    nearPoints = []
    distan = dist

    while True:
        for point in points:
            nowX, nowY = point
            x_bool = False; y_bool = False

            if x1 - nowX < distan and x1 - nowX > -distan:
                x_bool = True
            if y1 - nowY < distan and y1 - nowY > -distan:
                y_bool = True
            
            if x_bool and y_bool:
                nearPoints.append(point)

        if len(nearPoints) == 0: distan += dist
        else:break
    

    return random.choice(nearPoints)

        


def nearestBrute_Point(start, points):
    min_dist = None
    min_point = None
    for point in points:
        
        dist_x, dist_y = distance(start[0], start[1], point[0], point[1])
        dist_total = dist_x + dist_y
        if min_dist == None or dist_total < min_dist: min_dist = dist_total; min_point = point

    return min_point

def nearestBrute_route(points):
    p_left = points.copy()
    order = [p_left.pop(0)]
    end = p_left.pop(-1)
    
    for i in range(len(points) - 1):
        next = nearestBrute_Point(order[i], p_left)
        try:p_left.remove(next)
        except:break
        order.append(next)

    order.append(end)
    return order


def nearestBrute_short(points):
    p_left = points.copy()
    order = [p_left.pop(0)]
    end = p_left[-1]
    
    for i in range(len(points)):
        next = nearestBrute_Point(order[i], p_left)
        p_left.remove(next)
        order.append(next)
        if next == end:
            break
    
    return order

def nearestWeave_short(points, dist):
    p_left = points.copy()
    order = [p_left.pop(0)]
    end = p_left[-1]    

    for i in range(len(points)):    
        next = nearestWave(order[i], p_left, dist)
        p_left.remove(next)    

        order.append(next)
        if next == end:
            break
    
    return order 

def bruteForce(points):
    pass

#? How to
#points = [(2, 3), (-8, -9), (2, 3)]
#start = [(0,0)]
#route = nearestBrute_route(start + points)
#print(route)

