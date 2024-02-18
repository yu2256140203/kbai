import os
from PIL import Image, ImageChops
import numpy as np
import pandas as pd
import cv2
from ProblemSet import ProblemSet

def getNextLine(r):
    return r.readline().rstrip()

class DataGenerator:
    def __init__(self):
        pass

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

    def distance(self, npmatrix1, npmatrix2):
        # (L2 norm) distance between two matrices
        return np.linalg.norm(npmatrix1 - npmatrix2)

    def vectorize(self, problem):
        # independent variable y: 1 being the correct answer, 0 being the incorrect answer
        # dependent variables:
        #    x_problem: problem-specific relationships represents by the 3 statistics
        #    x_choice: choice-specific relationships represents by the 3 statistics
        res = []
        columns = ['problem_name', 'y', 'x']
        data = self.dataset_from_problem(problem)
        name = data['problem_name']

        if problem.problemType == '2x2':
            for i in range(1, 7):
                y = data['correct_answer'] == i
                x = self.distance(data['A'] - data['B'], data['C'] - data[str(i)] ) + \
                    self.distance(data['A'] - data['C'], data['B'] - data[str(i)] )
                if y == 1: # create 5x records of the correct answer to balance the dataset
                    res += [(name, y, x)] * 5
                else:
                    res += [(name, y, x)]

        elif problem.problemType == '3x3':
            pass
        else:
            print("Error: Problem {}: type not recognized".format(problem.problemName))
        df = pd.DataFrame(res, columns=columns)
        return df

    def prepare_dataset(self):
        sets = []  # The variable 'sets' stores multiple problem sets.
        # Each problem set comes from a different folder in /Problems/
        # Additional sets of problems will be used when grading projects.
        # You may also write your own problems.
        r = open(os.path.join("Problems", "ProblemSetList.txt"))  # ProblemSetList.txt lists the sets to solve.
        line = getNextLine(r)  # Sets will be solved in the order they appear in the file.
        while not line == "":  # You may modify ProblemSetList.txt for design and debugging.
            sets.append(ProblemSet(line))  # We will use a fresh copy of all problem sets when grading.
            line = getNextLine(r)

        df = pd.DataFrame(columns = ['y', 'x', 'x_std'])
        for set in sets:
            for problem in set.problems:  # Your agent will solve one problem at a time.
                _tmp = self.vectorize(problem)
                df = pd.concat([df, _tmp], ignore_index=True)
        df.to_csv("dataset.csv", index=False)

if __name__ == "__main__":
    generator = DataGenerator()
    generator.prepare_dataset()
    # solve()
    # grade()
