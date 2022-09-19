import tkinter
from time import process_time_ns

import nearest


#? Faltan añadir mas algoritmos

#**Variables
ordenPoints = []
tam_circl = 10

dict_points = {}
letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"


#**Funciones
def draw_circle(event):
    x = event.x
    y = event.y
    
    if len(ordenPoints) == 0:
        canvas.create_oval(x, y, x+tam_circl, y+tam_circl, fill="red")
        canvas.create_text(x+2, y+tam_circl+5, text="Start", fill="black", font=('Helvetica 10 bold'))

    else:
        canvas.delete("end")
        canvas.create_oval(x, y, x+tam_circl, y+tam_circl)
        canvas.create_oval(x, y, x+tam_circl, y+tam_circl, fill="blue", tags="end")
        canvas.create_text(x+2, y+tam_circl+5, text="End", fill="black", font=('Helvetica 10 bold'), tags="end")

    ordenPoints.append((x+tam_circl/2, y+tam_circl/2))
    dict_points[f"Punto{len(ordenPoints)}"] = (x+tam_circl/2, y+tam_circl/2)

    puntos.config(text=f"Puntos: {len(ordenPoints)}")

def ordenRoute():
    distance = 0
    canvas.delete("linea")

    s_time = process_time_ns()

    for i in range(len(ordenPoints) -1):
        n1 = ordenPoints[i]; n2 = ordenPoints[i+1]
        canvas.create_line(n1, n2, tags="linea")

        x_dist = n1[0] - n2[0] if n1[0] - n2[0] >= 0 else (n1[0] - n2[0]) * -1
        y_dist = n1[1] - n2[1] if n1[1] - n2[1] >= 0 else (n1[1] - n2[1]) * -1
      
        distance += x_dist + y_dist

    p_time = process_time_ns()

    lab_distance.config(text=f"Distancia = {distance}")
    lab_time.config(text=f"Time = {p_time - s_time}")

def nearestRoute():
    distance = 0
    canvas.delete("linea")

    s_time = process_time_ns()

    points = ordenPoints.copy()
    NearestRoute_order = nearest.nearestBrute_route(points)

    for i in range(len(NearestRoute_order) -1):
        n1 = NearestRoute_order[i]; n2 = NearestRoute_order[i+1]
        canvas.create_line(n1, n2, tags="linea")
    
        x_dist = n1[0] - n2[0] if n1[0] - n2[0] >= 0 else (n1[0] - n2[0]) * -1
        y_dist = n1[1] - n2[1] if n1[1] - n2[1] >= 0 else (n1[1] - n2[1]) * -1

        distance += x_dist + y_dist
        
    p_time = process_time_ns()

    lab_distance.config(text=f"Distancia = {distance}")
    lab_time.config(text=f"Time = {s_time - p_time}")


def nearestShort():
    distance = 0
    canvas.delete("linea")

    s_time = process_time_ns()

    points = ordenPoints.copy()
    NearestRoute_order = nearest.nearestBrute_short(points)


    for i in range(len(NearestRoute_order) -1):
        n1 = NearestRoute_order[i]; n2 = NearestRoute_order[i+1]
        canvas.create_line(n1, n2, tags="linea")
    
        x_dist = n1[0] - n2[0] if n1[0] - n2[0] >= 0 else (n1[0] - n2[0]) * -1
        y_dist = n1[1] - n2[1] if n1[1] - n2[1] >= 0 else (n1[1] - n2[1]) * -1

        distance += x_dist + y_dist
        

    p_time = process_time_ns()

    lab_distance.config(text=f"Distancia = {distance}")
    lab_time.config(text=f"Time = {s_time - p_time}")

def nearestWave():
    distance = 0
    canvas.delete("linea")

    s_time = process_time_ns()

    points = ordenPoints.copy()
    NearestRoute_order = nearest.nearestWeave_short(points, int(nearestWave_i.get()))


    for i in range(len(NearestRoute_order) -1):
        n1 = NearestRoute_order[i]; n2 = NearestRoute_order[i+1]
        canvas.create_line(n1, n2, tags="linea")
    
        x_dist = n1[0] - n2[0] if n1[0] - n2[0] >= 0 else (n1[0] - n2[0]) * -1
        y_dist = n1[1] - n2[1] if n1[1] - n2[1] >= 0 else (n1[1] - n2[1]) * -1

        distance += x_dist + y_dist
        
    p_time = process_time_ns()

    lab_distance.config(text=f"Distancia = {distance}")
    lab_time.config(text=f"Time = {s_time - p_time }")


def clean():
    global ordenPoints
    ordenPoints = []
    canvas.delete("all")
    lab_distance.config(text="Distancia = 0")
    puntos.config(text="Puntos = 0")
    lab_time.config(text=f"Time = 0")

def clean_linea():
    canvas.delete("linea")
    lab_distance.config(text="Distancia = 0")
    lab_time.config(text=f"Time = 0")


#**Main
win = tkinter.Tk()
win.title("Follow the points")



puntos = tkinter.Label(win, text="Puntos = 0")
puntos.grid(row=0, column=2)

lab_time = tkinter.Label(win, text="Time = 0")
lab_time.grid(row=0, column=3)

lab_distance = tkinter.Label(win, text="Distancia = 0")
lab_distance.grid(row=0, column=4)


orden_b = tkinter.Button(win, text="Orden", command=ordenRoute)
orden_b.grid(row=1, column=0)

nearest_b = tkinter.Button(win, text="Nearest", command=nearestRoute)
nearest_b.grid(row=2, column=0)

nearestR_b = tkinter.Button(win, text="Nearest Short", command=nearestShort)
nearestR_b.grid(row=4, column=0)

nearestWave_b = tkinter.Button(win, text="Nearest Wave", command=nearestWave)
nearestWave_b.grid(row=5, column=0)

nearestWave_i = tkinter.Scale(win, from_=1, to_=600, orient="horizontal", length=80)
nearestWave_i.grid(row=6, column=0)

clean_b = tkinter.Button(win, text="Limpiar\nLineas", command=clean_linea)
clean_b.grid(column=0, row=9)

clean_b = tkinter.Button(win, text="Limpiar", command=clean)
clean_b.grid(column=0, row=10)

canvas = tkinter.Canvas(win, height=300, width=600, bd=5, relief=tkinter.GROOVE, cursor="crosshair")
canvas.grid(row=1, column=2, columnspan=3, rowspan=10)

canvas.bind("<Button-1>", draw_circle)





win.mainloop()
