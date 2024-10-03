import numpy
from NodeClass import Node


class LAESolver():
    
    @staticmethod
    def linear_algebraic_equation_solver(nodes: [Node], imbalances_s: list, jacobi_matrix: numpy.ndarray) -> list:
        delta = []
        for i, imb_s in enumerate(imbalances_s):
            if nodes[i].type_node != 0:
                delta.append(-imb_s.real)
                delta.append(-imb_s.imag)
        delta_voltage = numpy.linalg.solve(jacobi_matrix, delta)
        
        return [complex(delta_voltage[i], delta_voltage[i+1]) for i in range(0, len(delta_voltage), 2)]