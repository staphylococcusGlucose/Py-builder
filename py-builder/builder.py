from compile_lists import *
from os import *

def COMPILE(COMPILER, FLAG, FILE) :
    cmd = COMPILER+' '+FLAG+' -c '+FILE+'.C'
    system(cmd)

def build(COMPILER, FLAG, OBJS):
    cmd = COMPILER+' '+FLAG+' '+OBJS+'-O '+PROGRAM
    system(cmd)
    
objs = ''
for i in FILES:
    COMPILE(COMPILER_NAME, FLAGS, i)
    objs = objs + i+'.o '

build(COMPILER_NAME, FLAGS, objs)