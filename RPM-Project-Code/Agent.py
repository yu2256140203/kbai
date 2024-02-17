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
import os
from PIL import Image, ImageChops
import numpy as np
import pandas as pd
from ProblemSet import ProblemSet


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

    def solve(self, problem):
        # Your code goes here
        return -1


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

