import unittest
from DoubleSlit import *
import math


class classicalToQuantum(unittest.TestCase):
    def testMultipleSlitQuantumExperiment(self):
        #Matriz de adyacencia experimento doble rendija
        Matriz_Doble_Rendija = [
            [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [0, 0],
             [1, 0], [0, 0], [0, 0]],
            [[0, 0], [0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
            [[0, 0], [0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]

        #Vector que representa el estado inicial del sistema
        Estado_Inicial = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

        self.assertEqual(multipleSlitQuantumExperiment(Matriz_Doble_Rendija[:],
                                                       Estado_Inicial[:], 2),
                         [[[0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],
                          [[0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],
                          [[0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],
                          [[0.1666666666666667, 0], [0.3333333333333334, 0], [0.0, 0], [1.0, 0], [0.0, 0], [0.0, 0],
                           [0.0, 0], [0.0, 0]],
                          [[0.1666666666666667, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [1.0, 0], [0.0, 0],
                           [0.0, 0], [0.0, 0]],
                          [[0.0, 0], [0.3333333333333334, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [1.0, 0],
                           [0.0, 0], [0.0, 0]],
                          [[0.1666666666666667, 0], [0.0, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [0.0, 0],
                           [1.0, 0], [0.0, 0]],
                          [[0.1666666666666667, 0], [0.0, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [0.0, 0],
                           [0.0, 0], [1.0, 0]]])

        answ = accionmatrizvector(multipleSlitQuantumExperiment(Matriz_Doble_Rendija[:],
                                                                  Estado_Inicial[:], 2), Estado_Inicial)
        graphProbabilitiesVector(answ)


if __name__ == '__main__':
    unittest.main()