import os
from PIL import Image, ImageChops
import numpy as np
import pandas as pd
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

    def calculate_statistical_features(self, vector):
        # vector: a flattened relationship matrix
        # calculate the mean, std, skewness, kurtosis, and entropy of the vector
        mean = np.mean(vector)
        std = np.std(vector)
        skewness = np.mean((vector - mean) ** 3) / (std ** 3)

        return [mean, std, skewness]

    def vectorize(self, problem):
        # independent variable y: 1 being the correct answer, 0 being the incorrect answer
        # dependent variables:
        #    x_problem: problem-specific relationships represents by the 3 statistics
        #    x_choice: choice-specific relationships represents by the 3 statistics

        data = self.dataset_from_problem(problem)

        if problem.problemType == '2x2':
            ys = []
            x_problem = []
            x_choice = []

            for i in range(1, 7):
                y = data['correct_answer'] == i
                ys.append(y)
                xhs.append( (data['C'] - data[str(i)]).flatten() )
                xvs.append( (data['B'] - data[str(i)]).flatten() )


        elif problem.problemType == '3x3':
            ys = []
            re = []
            xvs = []

            for i in range(1, 9):
                y = data['correct_answer'] == i
                if y == 1:  # create 7x records of the correct answer to balance the dataset
                    for _ in range(7):
                        ys.append(y)
                        xhs.append((data['A'] - data['B']).flatten())
                        xhs.append((data['B'] - data['C']).flatten())
                        xhs.append((data['D'] - data['E']).flatten())
                        xhs.append((data['E'] - data['F']).flatten())
                        xhs.append((data['G'] - data['H']).flatten())

                        xvs.append((data['A'] - data['D']).flatten())
                        xvs.append((data['D'] - data['G']).flatten())
                        xvs.append((data['B'] - data['E']).flatten())
                        xvs.append((data['E'] - data['H']).flatten())
                        xvs.append((data['C'] - data['F']).flatten())

                        xhs.append( (data['H'] - data[str(i)]).flatten() )
                        xvs.append( (data['F'] - data[str(i)]).flatten() )
                else:
                    ys.append(y)
                    xhs.append((data['A'] - data['B']).flatten())
                    xhs.append((data['B'] - data['C']).flatten())
                    xhs.append((data['D'] - data['E']).flatten())
                    xhs.append((data['E'] - data['F']).flatten())
                    xhs.append((data['G'] - data['H']).flatten())

                    xvs.append((data['A'] - data['D']).flatten())
                    xvs.append((data['D'] - data['G']).flatten())
                    xvs.append((data['B'] - data['E']).flatten())
                    xvs.append((data['E'] - data['H']).flatten())
                    xvs.append((data['C'] - data['F']).flatten())

                    xhs.append( (data['H'] - data[str(i)]).flatten() )
                    xvs.append( (data['F'] - data[str(i)]).flatten() )
        else:
            print("Error: Problem {}: type not recognized".format(problem.problemName))
        xs_raw = np.vstack(xhs + xvs)
        xs = np.apply_along_axis(lambda x: self.calculate_statistical_features(x), axis = 1, arr=xs_raw)
        return (ys, xs)

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

        ys, xs = [], []
        for set in sets:
            for problem in set.problems:  # Your agent will solve one problem at a time.
                tmp = self.vectorize(problem)
                ys += tmp[0]
                xs.append( tmp[1] )
        xs = np.vstack(xs)
        df = pd.DataFrame(np.hstack(ys, xs), columns=['y', 'x_mean', 'x_variance', 'x_skewness', 'x_kurtosis', 'x_entropy'])
        df.to_csv("dataset.csv", index=False)

if __name__ == "__main__":
    generator = DataGenerator()
    generator.prepare_dataset()
    # solve()
    # grade()
