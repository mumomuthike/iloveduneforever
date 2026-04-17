import os
import math

def greet():
    print("Hello!")

x = None
y = "hello"
result = x + y  # Unsafe operation
for i in range(5):
    for j in range(3):
        for k in range(2):
            for l in range(2):  # Too many nested loops
                pass

def calculate():
    unused_var = 30

