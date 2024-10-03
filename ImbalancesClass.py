from NodeClass import Node
import numpy


class Imbalances():

    @staticmethod
    def get_imbalances_s(nodes: [Node], y_matrix: numpy.ndarray) -> list:
        node_count = len(nodes)
        imbalances_s = []
        for i in range(node_count):
            s_power = None
            if nodes[i].type_node == 0:
                s_power = complex(0, 0)
            elif nodes[i].type_node == 1:
                s_power = -nodes[i].s_power
            else:
                s_power = nodes[i].s_power
            p1 = -s_power.real
            p2 = -y_matrix[i, i].real*abs(nodes[i].voltage)**2
            p3 = 0
            p4 = 0
            q1 = -s_power.imag
            q2 = y_matrix[i, i].imag*abs(nodes[i].voltage)**2
            q3 = 0
            q4 = 0
            for j in range(node_count):
                if j != i:
                    p3 += y_matrix[i, j].real*nodes[j].voltage.real+y_matrix[i, j].imag*nodes[j].voltage.imag
                    p4 += -y_matrix[i, j].imag*nodes[j].voltage.real+y_matrix[i, j].real*nodes[j].voltage.imag
                    q3 += -y_matrix[i, j].imag*nodes[j].voltage.real+y_matrix[i, j].real*nodes[j].voltage.imag
                    q4 += y_matrix[i, j].imag*nodes[j].voltage.imag+y_matrix[i, j].real*nodes[j].voltage.real
            p3 = - nodes[i].voltage.real*p3
            p4 = - nodes[i].voltage.imag*p4
            q3 = - nodes[i].voltage.real*q3
            q4 = nodes[i].voltage.imag*q4
            imbalances_s.append(complex(p1+p2+p3+p4, q1+q2+q3+q4))
        
        return imbalances_s