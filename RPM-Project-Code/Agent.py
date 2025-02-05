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
from enum import Enum
import cv2
from ProblemSet import ProblemSet

DEBUG = 0

def l2distance(np_image1, np_image2):
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
        return np.rot90(np_image, k = int(angle/90))

    def suggest_transformation(self, np_image1, np_image2):
        # Compare the two images and suggest a transformation
        res = ()
        min_distance = float('inf')
        for trans in Transformation:
            if trans == Transformation.rotate:
                for angle in [90, 180, 270]:
                    _d = l2distance(self._rotate(np_image1, angle), np_image2)
                    if _d < min_distance:
                        min_distance = _d
                        res = (TransformationSuggester._rotate, {'angle': angle})
            elif trans == Transformation.flip:
                for axis in [0, 1]:
                    _d = l2distance(self._flip(np_image1, axis), np_image2)
                    if _d < min_distance:
                        min_distance = _d
                        res = (TransformationSuggester._flip, {'axis': axis})
            else:
                pass
        return res

    def apply_transformation(self, np_image, func_trans, *args):
        res_image = func_trans(self, np_image, **args[0])
        # Image.fromarray(res_image).save('transformed.png')
        return res_image



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

    def getIdealImage(self, problem):
        # Get the ideal image from the problem
        images = self.dataset_from_problem(problem)
        if problem.problemType == '2x2':
            t = TransformationSuggester()
            self.ops['AB']['action'] = t.suggest_transformation(images['A'], images['B'])
            self.ops['AC']['action'] = t.suggest_transformation(images['A'], images['C'])
            idealImages = []
            idealImages.append(t.apply_transformation(images['C'], self.ops['AB']['action'][0], self.ops['AB']['action'][1]))
            idealImages.append(t.apply_transformation(images['B'], self.ops['AC']['action'][0], self.ops['AC']['action'][1]))
            # [Image.fromarray(idealImages[_]).save('idealImage_%s.png' % _ ) for _ in range(len(idealImages))]
            return idealImages
    def find_best_match(self, problem, idealImages):
        # Find the best match
        best_matches = []
        images = self.dataset_from_problem(problem)
        min_distance = float('inf')
        #distances = [l2distance(idealImages[0], images[str(i)]) + l2distance(idealImages[1], images[str(i)]) for i in range(1, 7)]
        distances = [l2distance( images[str(i)],idealImages[0]) + l2distance( images[str(i)],idealImages[1]) for i in
                     range(1, 7)]

        #print("%s: Distances %s" % (problem.name, distances))
        best_matches = sorted(range(1, len(distances)+1), key=lambda i: distances[i-1])
        print("%s: Best matches %s" % (problem.name, best_matches))
        return best_matches

    def Solve(self, problem):
        # Your code goes here
        if problem.problemType == '3x3':
            return 1
        # get the ideal image
        goalImages = self.getIdealImage(problem)
        # find the best match
        best_matches = self.find_best_match(problem, goalImages)
        return best_matches[0]


    def dataset_from_problem(self, problem):
        if problem.problemType == '2x2':
            A = cv2.imread(problem.figures["A"].visualFilename, cv2.IMREAD_GRAYSCALE)
            B = cv2.imread(problem.figures["B"].visualFilename, cv2.IMREAD_GRAYSCALE)
            C = cv2.imread(problem.figures["C"].visualFilename, cv2.IMREAD_GRAYSCALE)
            one = cv2.imread(problem.figures["1"].visualFilename, cv2.IMREAD_GRAYSCALE)
            two = cv2.imread(problem.figures["2"].visualFilename, cv2.IMREAD_GRAYSCALE)
            three = cv2.imread(problem.figures["3"].visualFilename, cv2.IMREAD_GRAYSCALE)
            four = cv2.imread(problem.figures["4"].visualFilename, cv2.IMREAD_GRAYSCALE)
            five = cv2.imread(problem.figures["5"].visualFilename, cv2.IMREAD_GRAYSCALE)
            six = cv2.imread(problem.figures["6"].visualFilename, cv2.IMREAD_GRAYSCALE)
            return {'problem_name': problem.name,
                    'A': A, 'B': B, 'C': C,
                    '1': one, '2': two, '3': three, '4': four, '5': five, '6': six}

        elif problem.problemType == '3x3':
            A = cv2.imread(problem.figures["A"].visualFilename, cv2.IMREAD_GRAYSCALE)
            B = cv2.imread(problem.figures["B"].visualFilename, cv2.IMREAD_GRAYSCALE)
            C = cv2.imread(problem.figures["C"].visualFilename, cv2.IMREAD_GRAYSCALE)
            D = cv2.imread(problem.figures["D"].visualFilename, cv2.IMREAD_GRAYSCALE)
            E = cv2.imread(problem.figures["E"].visualFilename, cv2.IMREAD_GRAYSCALE)
            F = cv2.imread(problem.figures["F"].visualFilename, cv2.IMREAD_GRAYSCALE)
            G = cv2.imread(problem.figures["G"].visualFilename, cv2.IMREAD_GRAYSCALE)
            H = cv2.imread(problem.figures["H"].visualFilename, cv2.IMREAD_GRAYSCALE)
            one = cv2.imread(problem.figures["1"].visualFilename, cv2.IMREAD_GRAYSCALE)
            two = cv2.imread(problem.figures["2"].visualFilename, cv2.IMREAD_GRAYSCALE)
            three = cv2.imread(problem.figures["3"].visualFilename, cv2.IMREAD_GRAYSCALE)
            four = cv2.imread(problem.figures["4"].visualFilename, cv2.IMREAD_GRAYSCALE)
            five = cv2.imread(problem.figures["5"].visualFilename, cv2.IMREAD_GRAYSCALE)
            six = cv2.imread(problem.figures["6"].visualFilename, cv2.IMREAD_GRAYSCALE)
            seven = cv2.imread(problem.figures["7"].visualFilename, cv2.IMREAD_GRAYSCALE)
            eight = cv2.imread(problem.figures["8"].visualFilename, cv2.IMREAD_GRAYSCALE)
            return {'problem_name': problem.name,
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
    problem = problem_set.problems[3]
    ans = agent.Solve(problem)
    print("Done")