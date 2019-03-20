from squid import *
import sys

def light(color):
    
    light = Squid(18,23,24)
    light.set_color(color)
    always_true = True
    while always_true:
        always_true = True

if __name__ == "__main__":
    if sys.argv[1] == "GREEN":
        light(GREEN)
    elif sys.argv[1] == "RED":
        light(RED)
    elif sys.argv[1] == "WHITE":
        light(WHITE)
    elif sys.argv[1] == "BLUE":
        light(BLUE)
    elif sys.argv[1] == "YELLOW":
        light(YELLOW)
    elif sys.argv[1] == "PURPLE":
        light(PURPLE)
    elif sys.argv[1] == "CYAN":
        light(CYAN)
    else:
        print("Not a valid color name.")
