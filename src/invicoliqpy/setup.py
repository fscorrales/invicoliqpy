import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['logo.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="logo.ico"
)

# SETUP CX FREEZE
setup(
    name = "invicoliqpy",
    version = "0.0.0.9000",
    description = '''Python QT app developed for salary settlement 
    at INVICO (Instituto de Vivienda de Corrientes). The database 
    is not provided with this package due to privacy reasons.
    ''',
    author = "Fernando S. Corrales",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
