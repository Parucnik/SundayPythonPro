from turtle import *

t = Turtle()
scr = t.getscreen()
# print(help(register_shape))
scr.addshape('hero.png', ((10,10), (-10,10), (-10,-10), (10, -10)))

print(scr.getshapes())
t.shape('hero.png')
mainloop()
