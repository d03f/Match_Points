import tkinter
import nearest

win = tkinter.Tk()
win.geometry("500x600")

tkinter.Label(win, text="Follow the points")
print("hola")


points = [(2, 3), (-8, -9), (10, 11)]
start = [(0,0)]
#nearest = nearest_point(start, points)
#print(nearest)
points = start + points

print(nearest.nearestBrute_route(points))

win.mainloop()