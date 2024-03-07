import numpy as np
import __Screen


Display = __Screen.Screen()

while(True):
    homeChoice = Display.home() #display main menu and store the choice
    if homeChoice == 1: #user chooses addition
        while(True):
            additionChoice = Display.matrixAddition()
            if additionChoice == 1:
                Display.additionScreen()
            else:
                break
    elif homeChoice == 2: #user chooses subtraction
        while(True):
            subtractionChoice = Display.matrixSubtraction()
            if subtractionChoice == 1:
                Display.subtractionScreen()
            else:
                break
    elif homeChoice == 3: #user chooses scalar multiplication
        while(True):
            scMultiplicationChoice = Display.matrixScMultiplication()
            if scMultiplicationChoice == 1:
                Display.scMultiplicationScreen()
            else:
                break
    elif homeChoice == 4: #user chooses matrix multiplication
        while(True):
            multiplicationChoice = Display.matrixMultiplication()
            if multiplicationChoice == 1:
                Display.multiplicationScreen()
            else:
                break
    elif homeChoice == 5: #user chooses matrix transposition
        while(True):
            transpositionChoice = Display.matrixTransposition()
            if transpositionChoice == 1:
                Display.TranspositionScreen()
            else:
                break
    elif homeChoice == 6: #user chooses to calculate determinant
        while(True):
            determinantChoice = Display.matrixDeterminant()
            if determinantChoice == 1:
                Display.determinantScreen()
            else:
                break
    elif homeChoice == 7: #user chooses to find inverse matrix
        while(True):
            inverseChoice = Display.matrixInverse()
            if inverseChoice == 1:
                Display.inverseScreen()
            else:
                break
    elif homeChoice == 0: #user chooses to exit the program
        break
