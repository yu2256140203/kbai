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
from enum import Enum
import cv2
from ProblemSet import ProblemSet


def l2distance(self, np_image1, np_image2):
    return np.linalg.norm(np_image1 - np_image2)
class Shape(Enum):
    triangle = 1,
    rectangle = 2,
    circle = 3,
    hexagon = 4

class Transformation(Enum):
    fill = 1,
    delete = 2,
    add = 3,
    change = 4
    flip = 5,
    rotate = 6

class TransformationSuggester:
    def __init__(self):
        pass

    def _flip(self, np_image, axis = 0):
        return np.flip(np_image, axis)
    def _fill(self, np_image, color = 0):
        return np_image.fill(color)

    def _rotate(self, np_image, angle = 90):
        return np.rotate(np_image, angle)

    def suggest_transformation(self, np_image1, np_image2):
        # Compare the two images and suggest a transformation
        res = ()
        min_distance = float('inf')
        for trans in Transformation:
            if trans == Transformation.rotate:
                for angle in [0, 90, 180, 270]:
                    _d = l2distance(self._rotate(np_image1, angle), np_image2)
                    if _d < min_distance:
                        min_distance = _d
                        res = (TransformationSuggester._rotate, {'angle': angle})
            elif trans == Transformation.flip:
                for axis in [0, 1]:
                    np_image1_d = l2distance(self._flip(np_image1, axis), np_image2)
                    if _d < min_distance:
                        min_distance = _d
                        res = (TransformationSuggester._flip, {'axis': axis})
            else:
                pass
        return res

    def apply_transformation(self, np_image, func_trans, *args):
        np_image = func_trans(np_image, *args)
        return np_image



class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        self.attr = {'A': {'shape': None},
                     'B': {'shape': None},
                     'C': {'shape': None},
                     '1': {'shape': None},
                     '2': {'shape': None},
                     '3': {'shape': None},
                     '4': {'shape': None},
                     '5': {'shape': None},
                     '6': {'shape': None}}

        self.ops = {'AB': {'action': None},
                      'AC': {'action': None}}
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
        images = self.dataset_from_problem(problem)
        if problem.problemType == '2x2':
            t = TransformationSuggester()
            self.ops['AB']['action'] = t.suggest_transformation(images['A'], images['B'])
            self.ops['AC']['action'] = t.suggest_transformation(images['A'], images['C'])
            idealImages = []
            idealImages.append(t.apply_transformation(images['C'], self.ops['AB']['action'][0], self.ops['AB']['action'][1]))
            idealImages.append(t.apply_transformation(images['B'], self.ops['AC']['action'][0], self.ops['AC']['action'][1]))



        return -1

    def dataset_from_problem(self, problem):
        if problem.problemType == '2x2':
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

            return {'problem_name': problem.name,
                    'correct_answer': problem.correctAnswer,
                    'A': A, 'B': B, 'C': C,
                    '1': one, '2': two, '3': three, '4': four, '5': five, '6': six}

        elif problem.problemType == '3x3':
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

            return {'problem_name': problem.name,
                    'correct_answer': problem.correctAnswer,
                    'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H,
                    '1': one, '2': two, '3': three, '4': four, '5': five, '6': six, '7': seven, '8': eight}
        else:
            print("Error: Problem {}: type not recognized".format(problem.name))
            return -1


    def detect_shape(self, image):
        # Convert to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        shapes = []  # This will store the detected shapes
        for cnt in contours:
            # Approximate the contour to simplify it
            epsilon = 0.01 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            # Example: classify shapes based on the number of vertices (simplified)
            if len(approx) == 3:
                shapes.append('triangle')
            elif len(approx) == 4:
                shapes.append('rectangle')
            # Add more shape classifications as needed
        return shapes




if __name__ == "__main__":
    agent = Agent()
    problem_set = ProblemSet("Basic Problems B")
    problem = problem_set.problems[1]
    agent.solve(problem)
    print("Done")