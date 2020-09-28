import matplotlib.pyplot as plot
import numpy as np

from calculadora_imaginarios import *


def finalMatrix(matrix):
    row, column = len(matrix), len(matrix[0])
    for i in range(row):
        nRow = []
        for j in range(column):
            nRow.append([(modulo(matrix[i][j]) ** 2), 0])
        matrix[i] = nRow
    return matrix


def quantumProbabilisticSystem(matrix, vectIni, clicks):
    if (clicks >= 0) and (type(clicks) is int):
        length = len(vectIni)
        copyMatrix = matrix[:]

        for x in range(clicks):
            matrix = multimatriz(matrix, copyMatrix)

        return finalMatrix(matrix)
    return -1


def multipleSlitQuantumExperiment(matrix, vectIni, clicks):
    return quantumProbabilisticSystem(matrix, vectIni, clicks)


def graphProbabilitiesVector(vector):
    data = len(vector)
    x = np.array([x for x in range(data)])
    y = np.array([round(vector[x][0] * 100, 2) for x in range(data)])

    plot.bar(x, y, color='g', align='center')
    plot.title('Probabilidades vector')
    plot.show()