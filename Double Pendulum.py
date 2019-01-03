import tkinter as tk
from tkinter import *
import time

r1 = 125;
r2 = 125;
m1 = 10;
m2 = 10;
a1 = 0;
a2 = 0;
a1_v = 0;
a2_v = 0;
g = 1;

##visual.scene.title = 'Pendulum'
##visual.scene.height = visual.scene.width = 800
##pivot = array([0,0,0]) 		# pivot position of pendulum
##visual.scene.center = pivot	                   # graphics cente

tk = Tk()
canvas = Canvas(tk, width = 500, height = 300)
tk.title("Double Pendulum")
canvas.pack()


sx = 250
sy = 100

##x1 = r1 * sin(a1)
##y1 = r1 * cos(a1)
##
##x2 = x1 + r2 * sin(a2)
##y2 = y1 + r2 * cos(a2)

line1 = canvas.create_line(sx, 10, sx, sy)

ball = canvas.create_oval(sx-m1/2, sy-m1/2, sx+m1/2, sy+m1/2, fill='black')

line1 = canvas.create_line(sx, sy-m1/2, sx, 200)

ball2 = canvas.create_oval(sx - m2/2, 200 - m2/2, sx + m2/2, 200 + m2/2, fill='black')


for i in range(100):
    canvas.move(ball, 0, 0)
    canvas.move(ball2, 0, 0)
    tk.update()
    time.sleep(0.01)

##for i in range(100):
##    canvas.move(ball2, 0, 0)
##    tk.update()
##    time.sleep(0.01)

tk.mainloop()

##px2 = -1;
##py2 = -1;
##cx, cy;

##let buffer;

##function setup() {
##  createCanvas(500, 300);
##  pixelDensity(1);
##  a1 = PI / 2;
##  a2 = PI / 2;
##  cx = width / 2;
##  cy = 50;
##  buffer = createGraphics(width, height);
##  buffer.background(175);
##  buffer.translate(cx, cy);
##}

##function draw() {
##  background(175);
##  imageMode(CORNER);
##  image(buffer, 0, 0, width, height);

##num1 = -g * (2 * m1 + m2) * sin(a1);
##num2 = -m2 * g * sin(a1 - 2 * a2);
##num3 = -2 * sin(a1 - a2) * m2;
##num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * cos(a1 - a2);
##den = r1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2));
##a1_a = (num1 + num2 + num3 * num4) / den;
##
##num1 = 2 * sin(a1 - a2);
##num2 = (a1_v * a1_v * r1 * (m1 + m2));
##num3 = g * (m1 + m2) * cos(a1);
##num4 = a2_v * a2_v * r2 * m2 * cos(a1 - a2);
##den = r2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2));
##a2_a = (num1 * (num2 + num3 + num4)) / den;

##  translate(cx, cy);
##  stroke(0);
##  strokeWeight(2);

##x1 = r1 * sin(a1);
##y1 = r1 * cos(a1);
##
##x2 = x1 + r2 * sin(a2);
##y2 = y1 + r2 * cos(a2);
##
##line(0, 0, x1, y1);
##fill(0);
##ellipse(x1, y1, m1, m1);
##
##line(x1, y1, x2, y2);
##fill(0);
##ellipse(x2, y2, m2, m2);
##
##a1_v += a1_a;
##a2_v += a2_a;
##a1 += a1_v;
##a2 += a2_v;

##  // a1_v *= 0.99;
##  // a2_v *= 0.99;

##  buffer.stroke(0);
##  if (frameCount > 1) {
##    buffer.line(px2, py2, x2, y2);
##  }
##
##  px2 = x2;
##  py2 = y2;
##}
