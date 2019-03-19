from OpenGL.GL import*
from OpenGL.GLUT import *
import numpy as np
from math import*




def boly5(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    glBegin(GL_POLYGON)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glVertex(x3, y3)
    glVertex(x4, y4)
    glVertex(x5, y5)
    glEnd()


def boly7(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7):
    glBegin(GL_POLYGON)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glVertex(x3, y3)
    glVertex(x4, y4)
    glVertex(x5, y5)
    glVertex(x6, y6)
    glVertex(x7, y7)
    glEnd()


def boly4(x1, y1, x2, y2, x3, y3, x4, y4):
    glBegin(GL_POLYGON)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glVertex(x3, y3)
    glVertex(x4, y4)
    glEnd()


def lines(x1, y1,x2,y2):
    glBegin(GL_LINES)
    glVertex(x1, y1)
    glVertex(x2,y2)
    glEnd()


def line_loop(x1, y1, x2, y2, x3, y3, x4, y4):
    glBegin(GL_LINE_LOOP)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glVertex(x3, y3)
    glVertex(x4, y4)
    glEnd()


def line_loop7(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7):
    glBegin(GL_LINE_LOOP)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glVertex(x3, y3)
    glVertex(x4, y4)
    glVertex(x5, y5)
    glVertex(x6, y6)
    glVertex(x7, y7)
    glEnd()


def line_loop_5(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    glBegin(GL_LINE_LOOP)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glVertex(x3, y3)
    glVertex(x4, y4)
    glVertex(x5, y5)
    glEnd()


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(4)

    glColor3f(1,.7,.2)
    glTranslate(0, -.2, 0)
    boly4(.35, -.2, -.35, -.2, -.35, .65, .35, .65)
    boly4(.2, .65, -.2, .65, -.2, .75, .2, .75)
    boly4(.1, .75, -.1, .75, -.1, .85, .1, .85)
    glColor3f(.4,1,.7)
    boly4(.2, .43, .2, .65, -.2, .65, -.2, .43)
    glColor3f(0, 0, .5)
    lines(.35, .43, -.35, .43)
    lines(.2, .43, .2, .65)
    lines(-.2, .43, -.2, .65)
    lines(.2,.55,.35,.55)
    lines(-.2, .55, -.35, .55)
    glColor3f( .6,.6,.6  )
    boly5(.2, -.28, .2, -.43, .27, -.5, .35, -.5, .35, -.28)
    boly5(-.2, -.28, -.2, -.43, -.27, -.5, -.35, -.5, -.35, -.28)
    boly4(.4, -.35, .35, -.35, .35, -.45, .4, -.45)
    boly4(-.4, -.35, -.35, -.35, -.35, -.45, -.4, -.45)
    boly7(.35, -.2, .2, -.2, .2, -.28, .35, -.28, .4, -.2, .4, -.1, .35, -.1)
    boly7(-.35, -.2, -.2, -.2, -.2, -.28, -.35, -.28, -.4, -.2, -.4, -.1, -.35, -.1)
    boly4(-.6, -.6, -0.4, -.6, -.4, 0, -.6, 0)
    boly4(.6, -.6, 0.4, -.6, .4, 0, .6, 0)
    glColor3f(0, 0, 0.5)
    line_loop_5(-.2, -.28, -.2, -.43, -.27, -.5, -.35, -.5, -.35, -.28)
    line_loop_5(.2, -.28, .2, -.43, .27, -.5, .35, -.5, .35, -.28)
    line_loop(.6, -.6, 0.4, -.6, .4, 0, .6, 0)
    line_loop(-.6, -.6, -0.4, -.6, -.4, 0, -.6, 0)
    line_loop(.35, -.2, -.35, -.2, -.35, .65, .35, .65)
    lines(.4, -.2,.35, -.28)
    lines(.4, -.35,.35, -.35)
    lines(.4, -.35,.35, -.35)
    lines(.4, -.45,.35, -.45)
    lines(.2, -.28,.2, -.2)
    lines(-.4, -.2,-.35, -.28)
    lines(-.4, -.35,-.35, -.35)
    lines(-.4, -.45,-.35, -.45)
    lines(-.2, -.28,-.2, -.2)
    lines(.7, -.6,-.7, -.6)
    lines(-.4, -.1,-.35, -.1)
    lines(.4, -.1,.35, -.1)

    glColor3f(0, .8, .9)
    boly5(-.3, .25, -.19, .25, -.19, .18, -.26, .14, -.3, .14)
    boly5(.3, .25, .19, .25, .19, .18, .26, .14, .3, .14)
    boly5(-.3, .46, -.26, .46, -.19, .43, -.19, .35, -.3, .35)
    boly5(.3, .46, .26, .46, .19, .43, .19, .35, .3, .35)
    boly7(-.45, .17, -.42, .14, -.3, .14, -.3, .25, -.4, .25, -.4, .2, -.45, .2)
    boly7(.45, .17, .42, .14, .3, .14, .3, .25, .4, .25, .4, .2, .45, .2)
    boly7(-.45, .44, -.45, .4, -.4, .4, -.4, .35, -.3, .35, -.3, .46, -.42, .46)
    boly7(.45, .44, .45, .4, .4, .4, .4, .35, .3, .35, .3, .46, .42, .46)
    boly4(.45, .4, .45, .2, .4, .2, .4, .4)
    boly4(-.45, .4, -.45, .2, -.4, .2, -.4, .4)
    glBegin(GL_POLYGON)
    glColor3f(.4,.5,.8)
    glVertex(0, .85)
    glVertex(-.1, 1)
    glVertex(.1,1)
    glEnd()

    drawbolyCircle(.08, -.15, 1,.2,1,.8)
    drawbolyCircle(.08, .15, 1, .2, 1, .8)
    drawbolyCircle(.04, -.15, 1,.3,.4,.7)
    drawbolyCircle(.04, .15, 1,.3,.4,.7)

    glColor3f(0, 0, 0.5)
    line_loop7(.45, .44, .45, .4, .4, .4, .4, .35, .3, .35, .3, .46, .42, .46)
    line_loop7(-.45, .44, -.45, .4, -.4, .4, -.4, .35, -.3, .35, -.3, .46, -.42, .46)
    line_loop7(.45, .17, .42, .14, .3, .14, .3, .25, .4, .25, .4, .2, .45, .2)
    line_loop7(-.45, .17, -.42, .14, -.3, .14, -.3, .25, -.4, .25, -.4, .2, -.45, .2)
    line_loop(.45, .4, .45, .2, .4, .2, .4, .4)
    line_loop(-.45, .4, -.45, .2, -.4, .2, -.4, .4)
    line_loop_5(.3, .46, .26, .46, .19, .43, .19, .35, .3, .35)
    line_loop_5(-.3, .46, -.26, .46, -.19, .43, -.19, .35, -.3, .35)
    line_loop_5(.3, .25, .19, .25, .19, .18, .26, .14, .3, .14)
    line_loop_5(-.3, .25, -.19, .25, -.19, .18, -.26, .14, -.3, .14)
    line_loop(.2,.65,-.2,.65,-.2,.75,.2,.75)
    line_loop(.1,.75,-.1,.75,-.1,.85,.1,.85)
    lines(.2,-.7,.5,-.7)
    lines(-.2, -.7, -.5, -.7)
    lines(.1, -.77, -.1, -.77)
    lines(.1,-.1,.2,-.1)
    glColor3f(0,0,.1)
    for y in np.arange(0, .6, .05):
        lines(0.4, -y, .6, -y)
    for y in np.arange(0, .6, .05):
        lines(-0.4, -y, -.6, -y)

    drawCircle(.08, -.15, 1,0, 0, 0.5)
    drawCircle(.08, .15, 1,0, 0, 0.5)
    drawCircle(.04, -.15, 1,0, 0, 0.5)
    drawCircle(.04, .15, 1, 0, 0, 0.5)
    glFlush()


def drawCircle(r=.01, xc=0, yc=0, a=0, b=0, c=0):
    glColor3f(a, b, c)
    glBegin(GL_LINE_LOOP)
    for theta in np.arange(0, 2 * pi, .1):
        x = r*cos(theta)
        y = r*sin(theta)
        glVertex(x+xc, y+yc)

    glEnd()


def drawbolyCircle(r=.01, xc=0, yc=0,a=0,b=0,c=0):
    glColor3f( a,b,c)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .1):
        x = r*cos(theta)
        y = r*sin(theta)
        glVertex(x+xc, y+yc)

    glEnd()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 500)
glutCreateWindow(b"WALL E")
glutDisplayFunc(draw)
glutMainLoop()