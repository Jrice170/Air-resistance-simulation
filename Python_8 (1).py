# Joseph Rice
# python 8 air resistance
# 4/12/2018
from __future__ import division
from visual import *
from math import *
from visual.graph import *
scene.width = 2000
scene.height = 1000
## base unit meters

#inital conditions
def feet_to_meters(feet):
    return feet*0.305

floor = box(pos=vector(0,1,0),length=1,width=1,height=0.1,color=color.orange,\
            material=materials.wood)
floor2 = box(pos=vector(0,0,0),length=5,width=20,height=0.01,make_trail=True,color=color.cyan)
floor3 = box(pos=vector(0,1,0),length=200,width=100,height=0.001,color=color.green)
statium = box(pos=vector(feet_to_meters(400),20,0),length=5,width=40,height=40,color=color.red)
##Base_ball_cannon = cylinder(pos=vector(0,1,0),axis=vector(0.5*cos(radians(45)),0.5*sin(radians(45)),0),radius=0.005,color=color.cyan,\
##                            )
Bass_ball = sphere(pos=vector(0,1,0),radius=0.035,color=color.red,make_trail=True,mass=155e-3,trail_type='points')
Speed_i = 44 #m/s
angle = 45 
Momentum_i = Bass_ball.mass*vector(cos(radians(angle)),sin(radians(angle)),0)*Speed_i
q = 1.3 # kg/m**3 density of the air 
c = 0.35 # Drag coefficient 
A = pi*Bass_ball.radius**2 # m**2
Graph1 = gdisplay(x=0,y=0,width=600,height=150,title="Kinetic Energy 'orange'; Graviational Kinetic Energy 'Red'; Total energy 'green' ",\
                  xtitle="Distance relative to earth (m)",ytitle="Energy (J)",foreground=color.white,background=color.black) 
K = gcurve(color=color.orange)
u = gcurve(color=color.red)
C = gcurve(color=color.green)

# print statements
print("The speed of the ball when hit: ", '\n',Speed_i, 'm/s')
print("velocity vector:", '\n', Momentum_i/Bass_ball.mass, '\n',"angle= " ,angle,  " degrees")



def force_air(c,q,A,V):
    """ C Drag coeffcient; q density of air; A cross sectional Area; V velocity;"""
    vhat = V/mag(V)
    F_air = 0.5*c*A*q*mag(V)**2*(-vhat)
    return F_air
def percent(value,value2):
    """returns a percent value"""
    top,botton=abs(value-value2),(value+value2)/2
    percent = top/botton*100
    return abs(percent)

Delta_t = 0.01 # seconds 
t_i = 0 # seconds

# update Statements 
while True:
    rate(100)
    F_grav = Bass_ball.mass * vector(0,-9.8,0)
    V = Momentum_i/Bass_ball.mass
    Fair = force_air(c,q,A,V)
    F_net = F_grav + Fair
    Momentum_i = Momentum_i + F_net*Delta_t
    Bass_ball.pos = Bass_ball.pos + (Momentum_i/Bass_ball.mass)*Delta_t
    floor2.pos.x = Bass_ball.pos.x
    Distance = Bass_ball.pos.y 
    PE  = Bass_ball.mass*9.8*Distance
    KE = 0.5*Bass_ball.mass*mag(Momentum_i/Bass_ball.mass)**2
    K.plot( pos=(t_i,KE) )
    u.plot( pos=(t_i,PE) )
    C.plot( pos=(t_i,KE+PE))
    t_i += Delta_t
    if Bass_ball.pos.y <= 0:
        break
print('Percent Difference',percent(198.5,Bass_ball.pos.x))
print('The distance X-direction ', Bass_ball.pos.x, 'meters')
