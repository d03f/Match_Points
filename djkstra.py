

def nearestWave(point, points, dist):
    x1, y1 = point
    nearPoints = []
    distan = dist

    while True:
        for point in points:
            nowX, nowY = point
            x_bool = False; y_bool = False

            x_dist = x1 - nowX if x1 - nowX > 0 else (x1 - nowX) * -1
            y_dist = y1 - nowY if y1 - nowY > 0 else (y1 - nowY) * -1

            if x_dist < distan: x_bool = True
            if y_dist < distan: y_bool = True

            if x_bool and y_bool:
                nearPoints.append(point)
        if len(nearPoints) == 0: distan += dist
        else:break
    

    return nearPoints


def dijkstra(puntos, dicst_points, index_dijkstra):
    punts = puntos.copy()
    print(punts)
    start = punts.pop[0]
    end = dicst_points[-1][1]
    print(end)

    orden_result = []


    while orden_result[-1] != end:
        pass



index_dijkstra = {}

dict = {'Punto1': (1, 1), 'Punto2': (2, 4), 
'Punto3': (5, 8), 'Punto4': (9, 10)}

dict_dj = {'Punto1': (None, None), 'Punto2': (None, None), 
'Punto3': (None, None), 'Punto4': (None, None)}

puntos = [(1,1), (2,4), (5,8), (9, 19)]


x = dijkstra(puntos, dict, dict_dj)