import os

from engine import Engine

os.chdir(os.path.dirname(__file__))

engine = Engine()
engine.iniciar()
