import tkinter
import nearest


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

    else:canvas.create_oval(x, y, x+tam_circl, y+tam_circl).tag_add('last')

    ordenPoints.append((x+tam_circl/2, y+tam_circl/2))

def ordenRoute():
    for i in range(len(ordenPoints) -1):
        x1 = ordenPoints[i]; y1 = ordenPoints[i+1]
        x2 = ordenPoints[i]; y2 = ordenPoints[i]

        canvas.create_line(x1, y1, x2, y2)

def nearestRoute():
    pass

def clean():
    global ordenPoints
    ordenPoints = []
    canvas.delete("all")

#**Main
win = tkinter.Tk()

tkinter.Label(win, text="Follow the points").grid(row=0, column=3)

orden_b = tkinter.Button(win, text="Orden", command=ordenRoute)
orden_b.grid(row=2, column=0)

nearest_b = tkinter.Button(win, text="Nearest", command=nearestRoute)
nearest_b.grid(row=1, column=0)

clean_b = tkinter.Button(win, text="Limpiar", command=clean)
clean_b.grid(column=0, row=10)

canvas = tkinter.Canvas(win, height=300, width=600, bd=5, relief=tkinter.GROOVE)
canvas.grid(row=1, column=2, columnspan=3, rowspan=10)

canvas.bind("<Button-1>", draw_circle)





win.mainloop()