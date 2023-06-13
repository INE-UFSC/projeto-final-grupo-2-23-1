import pygame as pg
from math import cos, sin

def trajetoria_linear(dt, angulo, veloc_proj):
    dx = cos(angulo)*veloc_proj*dt
    dy = -sin(angulo)*veloc_proj*dt

    return pg.math.Vector2(dx, dy)