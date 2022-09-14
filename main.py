import tkinter
import nearest

#? Faltan añadir mas algoritmos

#**Variables
ordenPoints = []
tam_circl = 10

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
    puntos.config(text=f"Puntos: {len(ordenPoints)}")

def ordenRoute():
    distance = 0
    canvas.delete("linea")

    for i in range(len(ordenPoints) -1):
        x = ordenPoints[i]; y = ordenPoints[i+1]
        canvas.create_line(x, y, tags="linea")

        x_dist = x[0] - x[1] if x[0] - x[1] > 0 else (x[0] - x[1]) * -1
        y_dist = y[0] - y[1] if y[0] - y[1] > 0 else (y[0] - y[1]) * -1
        distance += x_dist + y_dist

        lab_distance.config(text=f"Disntancia = {distance}")

def nearestRoute():
    distance = 0
    canvas.delete("linea")

    points = ordenPoints.copy()
    NearestRoute_order = nearest.nearestBrute_route(points[0:-1])
    for i in range(len(NearestRoute_order) -1):
        x = NearestRoute_order[i]; y = NearestRoute_order[i+1]
        canvas.create_line(x, y, tags="linea")
    
        x_dist = x[0] - x[1] if x[0] - x[1] > 0 else (x[0] - x[1]) * -1
        y_dist = y[0] - y[1] if y[0] - y[1] > 0 else (y[0] - y[1]) * -1
        distance += x_dist + y_dist


    canvas.create_line(points[-1], NearestRoute_order[-1], tags="linea")


    lab_distance.config(text=f"Distancia = {distance}")



def clean():
    global ordenPoints
    ordenPoints = []
    canvas.delete("all")
    lab_distance.config(text="Distancia = 0")

def clean_linea():
    canvas.delete("linea")
    lab_distance.config(text="Distancia = 0")

#**Main
win = tkinter.Tk()
win.title("Follow the points")



puntos = tkinter.Label(win, text="Puntos = 0")
puntos.grid(row=0, column=2)

lab_distance = tkinter.Label(win, text="Distancia = 0")
lab_distance.grid(row=0, column=4)


orden_b = tkinter.Button(win, text="Orden", command=ordenRoute)
orden_b.grid(row=2, column=0)

nearest_b = tkinter.Button(win, text="Nearest", command=nearestRoute)
nearest_b.grid(row=1, column=0)

clean_b = tkinter.Button(win, text="Limpiar\nLineas", command=clean_linea)
clean_b.grid(column=0, row=9)

clean_b = tkinter.Button(win, text="Limpiar", command=clean)
clean_b.grid(column=0, row=10)

canvas = tkinter.Canvas(win, height=300, width=600, bd=5, relief=tkinter.GROOVE)
canvas.grid(row=1, column=2, columnspan=3, rowspan=10)

canvas.bind("<Button-1>", draw_circle)





win.mainloop()
