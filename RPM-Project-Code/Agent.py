# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageChops
import numpy as np
import pandas as pd

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def prepare_dataset(self, problem):
        if problem.problemType = '2x2':
            A = Image.open(problem.figures["A"].visualFilename)
            B = Image.open(problem.figures["B"].visualFilename)
            C = Image.open(problem.figures["C"].visualFilename)
            one = Image.open(problem.figures["1"].visualFilename)
            two = Image.open(problem.figures["2"].visualFilename)
            three = Image.open(problem.figures["3"].visualFilename)
            four = Image.open(problem.figures["4"].visualFilename)
            five = Image.open(problem.figures["5"].visualFilename)
            six = Image.open(problem.figures["6"].visualFilename)

            A = np.array(A)
            B = np.array(B)
            C = np.array(C)
            one = np.array(one)
            two = np.array(two)
            three = np.array(three)
            four = np.array(four)
            five = np.array(five)
            six = np.array(six)
            return {'problem_name': problem.problemName,
                    'correct_answer': problem.correctAnswer,
                    'given': [A, B, C],
                    'choices': [one, two, three, four, five, six]}

        elif problem.problemType = '3x3':
            A = Image.open(problem.figures["A"].visualFilename)
            B = Image.open(problem.figures["B"].visualFilename)
            C = Image.open(problem.figures["C"].visualFilename)
            D = Image.open(problem.figures["D"].visualFilename)
            E = Image.open(problem.figures["E"].visualFilename)
            F = Image.open(problem.figures["F"].visualFilename)
            G = Image.open(problem.figures["G"].visualFilename)
            H = Image.open(problem.figures["H"].visualFilename)

            one = Image.open(problem.figures["1"].visualFilename)
            two = Image.open(problem.figures["2"].visualFilename)
            three = Image.open(problem.figures["3"].visualFilename)
            four = Image.open(problem.figures["4"].visualFilename)
            five = Image.open(problem.figures["5"].visualFilename)
            six = Image.open(problem.figures["6"].visualFilename)
            seven = Image.open(problem.figures["7"].visualFilename)
            eight = Image.open(problem.figures["8"].visualFilename)

            A = np.array(A)
            B = np.array(B)
            C = np.array(C)
            D = np.array(D)
            E = np.array(E)
            F = np.array(F)
            G = np.array(G)
            H = np.array(H)

            one = np.array(one)
            two = np.array(two)
            three = np.array(three)
            four = np.array(four)
            five = np.array(five)
            six = np.array(six)
            seven = np.array(seven)
            eight = np.array(eight)

            return {'problem_name': problem.problemName,
                    'correct_answer': problem.correctAnswer,
                    'given': [A, B, C, D, E, F, G, H],
                    'choices': [one, two, three, four, five, six, seven, eight]}
        else:
            print("Error: Problem {}: type not recognized".format(problem.problemName))
            return -1

    def Solve(self, problem):
        if problem.problemType == "2x2":
            return self.solve2x2(problem)
        elif problem.problemType == "3x3":
            return self.solve3x3(problem)
        else:
            print("Error: Problem type not recognized")
            return -1

    ### Set of transformation functions ###

    def solve2x2(self, problem):
        # Get the visual representations of the figures
        A = Image.open(problem.figures["A"].visualFilename)
        B = Image.open(problem.figures["B"].visualFilename)
        C = Image.open(problem.figures["C"].visualFilename)
        one = Image.open(problem.figures["1"].visualFilename)
        two = Image.open(problem.figures["2"].visualFilename)
        three = Image.open(problem.figures["3"].visualFilename)
        four = Image.open(problem.figures["4"].visualFilename)
        five = Image.open(problem.figures["5"].visualFilename)
        six = Image.open(problem.figures["6"].visualFilename)

        # Convert the images to numpy arrays
        A = np.array(A)
        B = np.array(B)
        C = np.array(C)
        one = np.array(one)
        two = np.array(two)
        three = np.array(three)
        four = np.array(four)
        five = np.array(five)
        six = np.array(six)

        ### Check for a horizontal flip ###
        # Get the difference between A and B
        diffAB = np.subtract(A, B)
        diffAC = np.subtract(A, C)

        # Iterate through choices to find the one that matches the difference between A and B
        for i in range(1, 7):
            # Get the current choice
            choice = Image.open(problem.figures[str(i)].visualFilename)
            choice = np.array(choice)

            # Get the difference between A and the current choice
            diffCi = np.subtract(C, choice)
            diffBi = np.subtract(B, choice)

            # If the difference between A and the current choice matches the difference between A and B, return the current choice
            if np.array_equal(diffAB, diffCi) or np.array_equal(diffAC, diffBi):
                return i

        # If no choice matches the difference between A and B, return 1
        return 1

    def solve3x3(self, problem):
        return 1

    def print(self, problem):
        print("Solving: " + problem.name)
        print("Problem Type: " + problem.problemType)
        print("Has Visual: " + str(problem.hasVisual))
        print("Has Verbal: " + str(problem.hasVerbal))
        print("")

        if problem.hasVerbal:
            print("Verbal:")
            print("  A: " + problem.figures["A"].visualFilename)
            print("  B: " + problem.figures["B"].visualFilename)
            print("  C: " + problem.figures["C"].visualFilename)
            print("  1: " + problem.figures["1"].visualFilename)
            print("  2: " + problem.figures["2"].visualFilename)
            print("  3: " + problem.figures["3"].visualFilename)
            print("  4: " + problem.figures["4"].visualFilename)
            print("  5: " + problem.figures["5"].visualFilename)
            print("  6: " + problem.figures["6"].visualFilename)
            print("")

            print("Answer: " + problem.correctAnswer)
            print("")

            print("Verbal:")
            print("  A: " + problem.figures["A"].visualFilename)
            print("  B: " + problem.figures["B"].visualFilename)
            print("  C: " + problem.figures["C"].visualFilename)
            print("  1: " + problem.figures["1"].visualFilename)
            print("  2: " + problem.figures["2"].visualFilename)
            print("  3: " + problem.figures["3"].visualFilename)
            print("  4: " + problem.figures["4"].visualFilename)
            print("  5: " + problem.figures["5"].visualFilename)
            print("  6: " + problem.figures["6"].visualFilename)
            print("")

            print("Answer: " + problem.correctAnswer)
            print("")

        return -1