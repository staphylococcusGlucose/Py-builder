import os
from compile_lists import *
from os import system

def COMPILE(compiler, flag, file):
    source_file = file + '.c'
    obj_file = os.path.basename(file) + '.o'  # foo.o, main.o
    cmd = f"{compiler} {flag} -c {source_file} -o {obj_file}"
    print(f"[COMPILE] {cmd}")
    system(cmd)
    return obj_file

def build(compiler, flag, obj_list, output):
    cmd = f"{compiler} {flag} {' '.join(obj_list)} -o {output}"
    print(f"[LINK] {cmd}")
    system(cmd)

# main build process
obj_files = []
for file in FILES:
    obj = COMPILE(COMPILER_NAME, FLAGS, file)
    obj_files.append(obj)

build(COMPILER_NAME, FLAGS, obj_files, PROGRAM)
