
"""
This file contains the:
        different screen texts
        the prompts
        And returns the user choices in integer dtype
"""

import numpy as np
import ast

class Screen:
    def __init__(self):
        self.noneIntegerEnteryErrorMessage = "Error: Please enter an integer value."
        self.enteryOutsideExpectedDomainMessage = "Please Enter a valid option number"
        self.homeHeading = "Welcome to the Matrix Calculator"
        self.homeMenuOptions = '''
            \nChoose your desired opertion below:\n\n
            1. Addition (both marices must have the same number of rows and columns)\n
            2. Subtraction (both marices must have the same number of rows and columns)\n
            3. Scalar multiplication\n
            4. Matrix multiplication (columns of 1st matrix = rows of 2nd matrix)\n
            5. Transposition\n
            6. Determenant (the matrix must be a square matrix, nXn)\n
            7. Inverse (the matrix must be a square matrix, nXn)\n
            \n0. to exit'''
        self.selectionPrompt = '''
            \nThe nummber corresponding to your desired option is: '''
        
        self.matrixEnteringPrompt = "\nEnter your matrix below\n_______________________\n"

        self.matrixEntryInstruction = '''
            \nEnter the matrix elements in the following format:\n
            [[ row1-col1 , row1-col2 , row1-col3 , ... , row1-col(n) ],\n
             [ row2-col1 , row2-col2 , row2-col3 , ... , row2-col(n) ],\n
             [ row3-col1 , row3-col2 , row3-col3 , ... , row3-col(n) ],\n
             [   . -col1 ,   . -col2 ,  .  -col3 , ... ,  .  -col(n) ],\n
             [   . -col1 ,   . -col2 ,  .  -col3 , ... ,  .  -col(n) ],\n
             [   . -col1 ,   . -col2 ,  .  -col3 , ... ,  .  -col(n) ],\n
             [ rown-col1 , rown-col2 , rown-col3 , ... , rown-col(n) ]]\n'''
        self.wrongMatrixFormatEntry = "The matrix was entered in a wrong format"
        
        self.matrixAdditionHeader = "Matrix Addition Screen"
        self.matrixSubtractionHeader = "Matrix Subtraction Screen"
        self.matrixScMultiplicationHeader = "Matrix Scalar Multiplication Screen"
        self.matrixMultiplicationHeader = "Matrix Multiplication Screen"
        self.matrixTranspositionHeader = "Matrix Transposition Screen"
        self.matrixDeterminantHeader = "Matrix Determinant Screen"
        self.matrixInverseHeader = "Matrix Inverse Screen"


        self.matrixAdditionOptions = '''
            \nChoose your desired opertion below:\n\n
            1. Insert a matrix\n
            0. to to go back to main menu'''
        self.matrixSubtractionOptions = '''
            \nChoose your desired opertion below:\n\n
            1. Insert a matrix\n
            0. to to go back to main menu'''
        self.matrixScMultiplicationOptions = '''
            \nChoose your desired opertion below:\n\n
            1. Insert a matrix\n
            0. to to go back to main menu'''
        self.matrixMultiplicationOptions = '''
            \nChoose your desired opertion below:\n\n
            1. Insert a matrix\n
            0. to to go back to main menu'''
        self.matrixTranspositionOptions = '''
            \nChoose your desired opertion below:\n\n
            1. Insert a matrix\n
            0. to to go back to main menu'''
        self.matrixDeterminantOptions = '''
            \nChoose your desired opertion below:\n\n
            1. Insert a matrix\n
            0. to to go back to main menu'''
        self.matrixInverseOptions = '''
            \nChoose your desired opertion below:\n\n
            1. Insert a matrix\n
            0. to to go back to main menu'''


    def home(self):# home screen header - menu - returning user main menu choice
        for i in range(3):
            if i%2==0:
                for j in range(len(self.homeHeading)+6):
                    print("|", end="")
                print("")
            else:
                print("|| "+self.homeHeading+" ||")
        
        print(self.homeMenuOptions)
        for i in range(len(self.homeHeading)+6):
            print("_",end="")
        print("")

        while(True): #(input error handling) Preventing problematic inputs
            try:
                homeChoice = int(input(self.selectionPrompt))
                if homeChoice>=0 and homeChoice<=7:
                    break
                else:
                    print(self.enteryOutsideExpectedDomainMessage)  
            except ValueError:
                print(self.noneIntegerEnteryErrorMessage)
        return homeChoice


    def matrixAddition(self): #returns choice to Add or go back
        for i in range(3):
            if i%2==0:
                for j in range(len(self.matrixAdditionHeader)+6):
                    print("|", end="")
                print("")
            else:
                print("|| "+self.matrixAdditionHeader+" ||")
        print(self.matrixAdditionOptions)
        for i in range(len(self.matrixAdditionHeader)+6):
            print("_", end="")
        print("")
        while(True):
            try:
                additionChoice = int(input(self.selectionPrompt))
                if additionChoice==1 or additionChoice == 0:
                    break
                else:
                    print(self.enteryOutsideExpectedDomainMessage)
            except ValueError:
                print(self.noneIntegerEnteryErrorMessage)
        return additionChoice
    def matrixSubtraction(self):#returns choice to Subtract or go back
        for i in range(3):
            if i%2==0:
                for j in range(len(self.matrixSubtractionHeader)+6):
                    print("|", end="")
                print("")
            else:
                print("|| "+self.matrixSubtractionHeader+" ||")
        print(self.matrixSubtractionOptions)
        for i in range(len(self.matrixSubtractionHeader)+6):
            print("_", end="")
        print("")
        while(True):
            try:
                subtractionChoice = int(input(self.selectionPrompt))
                if subtractionChoice ==1 or subtractionChoice == 0:
                    break
                else:
                    print(self.enteryOutsideExpectedDomainMessage)
            except ValueError:
                print(self.noneIntegerEnteryErrorMessage)
        return subtractionChoice
    def matrixScMultiplication(self):#returns choice to scalar multiply or go back
        for i in range(3):
            if i%2==0:
                for j in range(len(self.matrixScMultiplicationHeader)+6):
                    print("|", end="")
                print("")
            else:
                print("|| "+self.matrixScMultiplicationHeader+" ||")
        print(self.matrixScMultiplicationOptions)
        for i in range(len(self.matrixScMultiplicationHeader)+6):
            print("_", end="")
        print("")
        while(True):
            try:
                scMultiplicationChoice = int(input(self.selectionPrompt))
                if scMultiplicationChoice ==1 or scMultiplicationChoice == 0:
                    break
                else:
                    print(self.enteryOutsideExpectedDomainMessage)
            except ValueError:
                print(self.noneIntegerEnteryErrorMessage)
        return scMultiplicationChoice
    def matrixMultiplication(self):#returns choice to multiply or go back
        for i in range(3):
            if i%2==0:
                for j in range(len(self.matrixMultiplicationHeader)+6):
                    print("|", end="")
                print("")
            else:
                print("|| "+self.matrixMultiplicationHeader+" ||")
        print(self.matrixMultiplicationOptions)
        for i in range(len(self.matrixMultiplicationHeader)+6):
            print("_", end="")
        print("")
        while(True):
            try:
                multiplicationChoice = int(input(self.selectionPrompt))
                if multiplicationChoice ==1 or multiplicationChoice == 0:
                    break
                else:
                    print(self.enteryOutsideExpectedDomainMessage)
            except ValueError:
                print(self.noneIntegerEnteryErrorMessage)
        return multiplicationChoice
    def matrixTransposition(self):#returns choice to transpose or go back
        for i in range(3):
            if i%2==0:
                for j in range(len(self.matrixTranspositionHeader)+6):
                    print("|", end="")
                print("")
            else:
                print("|| "+self.matrixTranspositionHeader+" ||")
        print(self.matrixTranspositionOptions)
        for i in range(len(self.matrixTranspositionHeader)+6):
            print("_", end="")
        print("")
        while(True):
            try:
                transpositionChoice = int(input(self.selectionPrompt))
                if transpositionChoice ==1 or transpositionChoice == 0:
                    break
                else:
                    print(self.enteryOutsideExpectedDomainMessage)
            except ValueError:
                print(self.noneIntegerEnteryErrorMessage)
        return transpositionChoice
    def matrixDeterminant(self):#returns choice to calculate determinant or go back
        for i in range(3):
            if i%2==0:
                for j in range(len(self.matrixDeterminantHeader)+6):
                    print("|", end="")
                print("")
            else:
                print("|| "+self.matrixDeterminantHeader+" ||")
        print(self.matrixDeterminantOptions)
        for i in range(len(self.matrixDeterminantHeader)+6):
            print("_", end="")
        print("")
        while(True):
            try:
                determinantChoice = int(input(self.selectionPrompt))
                if determinantChoice ==1 or determinantChoice == 0:
                    break
                else:
                    print(self.enteryOutsideExpectedDomainMessage)
            except ValueError:
                print(self.noneIntegerEnteryErrorMessage)
        return determinantChoice
    def matrixInverse(self):#returns choice to find the inverse or go back
        for i in range(3):
            if i%2==0:
                for j in range(len(self.matrixInverseHeader)+6):
                    print("|", end="")
                print("")
            else:
                print("|| "+self.matrixInverseHeader+" ||")
        print(self.matrixInverseOptions)
        for i in range(len(self.matrixInverseHeader)+6):
            print("_", end="")
        print("")
        while(True):
            try:
                inverseChoice = int(input(self.selectionPrompt))
                if inverseChoice ==1 or inverseChoice == 0:
                    break
                else:
                    print(self.enteryOutsideExpectedDomainMessage)
            except ValueError:
                print(self.noneIntegerEnteryErrorMessage)
        return inverseChoice


    def additionScreen(self):#matrix entry - operation - showing result
        while(True):
            matrixA = self.matrixInput()
            print("Matrix 1:\n",matrixA)
            matrixB = self.matrixInput()
            print("Matrix 2:\n",matrixB,"\n")
            if matrixA.shape == matrixB.shape:
                result = np.add(matrixA,matrixB)
                print("Result is:\n__________\n",result)
                break
            else:
                print("Those two matrices can't be addded.\nMake sure they have the same size")
    def subtractionScreen(self):#matrix entry - operation - showing result
        while(True):
            matrixA = self.matrixInput()
            print("Matrix 1:\n",matrixA)
            matrixB = self.matrixInput()
            print("Matrix 2:\n",matrixB,"\n")
            if matrixA.shape == matrixB.shape:
                result = np.subtract(matrixA,matrixB)
                print("Result is:\n__________\n",result)
                break
            else:
                print("Those two matrices can't be operated.\nMake sure they have the same size")
    def scMultiplicationScreen(self):#matrix entry - operation - showing result
        matrix = self.matrixInput()
        print("Matrix 1:\n",matrix)
        while(True):
            try:
                scalar = float(input("the scalar: "))
                result = scalar * matrix
                print("Result is:\n__________\n",result)
                break
            except:
                print("ERROR\nPlease make sure to enter a scalar value.")
    def multiplicationScreen(self):#matrix entry - operation - showing result
        while(True):
            matrixA = self.matrixInput()
            print("Matrix 1:\n",matrixA)
            matrixB = self.matrixInput()
            print("Matrix 2:\n",matrixB,"\n")
            if matrixA.shape[1] == matrixB.shape[0]:
                result = np.dot(matrixA,matrixB)
                print("Result is:\n__________\n",result)
                break
            else:
                print("Please make sure the columns of matrix 1 = rows of matrix 2")
    def TranspositionScreen(self):#matrix entry - operation - showing result
        matrixA = self.matrixInput()
        print("Original Matrix:\n",matrixA)
        result = matrixA.T
        print("\nTransposed:\n__________\n",result)
    def determinantScreen(self):#matrix entry - operation - showing result
        while(True):
            matrixA = self.matrixInput()
            print("Your matrix is:\n",matrixA)
            if matrixA.shape[0] == matrixA.shape[1]:
                result = np.linalg.det(matrixA)
                print("Determinant is:\n____________\n",result)
                break
            else:
                print("Please make sure to enter a square matrix. rows = columns")
    def inverseScreen(self):#matrix entry - operation - showing result
        while(True):
            matrixA = self.matrixInput()
            print("Your matrix is:\n",matrixA)
            if matrixA.shape[0] == matrixA.shape[1]:
                result = np.linalg.inv(matrixA)
                print("Inverse matrix is:\n________________\n",result)
                break
            else:
                print("Please make sure to enter a square matrix. rows = columns")

    def matrixInput(self):
        '''Returns a NumPy array matrix'''
        print(self.matrixEntryInstruction)
        while(True):
            userMatrixInput = input(self.matrixEnteringPrompt)
            try:
                # Convert input string to list of lists containing floats
                list_of_lists = ast.literal_eval(userMatrixInput)
                # Convert integers to floats
                for sublist in list_of_lists:
                    for i, value in enumerate(sublist):
                        sublist[i] = float(value)
                # pass the list of lists to np to create an array matrix
                matrix = np.array(list_of_lists)
                break
            except:
                print(self.wrongMatrixFormatEntry)
        return matrix
                    
            



"""_______________________________________________________________________________
TESTS
___________________________________________________________________________________"""
if __name__=="__main__":
    Screen = Screen()
    #Screen.home()
    #print(Screen.matrixInput())
    Screen.additionScreen()