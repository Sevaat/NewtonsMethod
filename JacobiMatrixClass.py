import numpy
from NodeClass import Node


class JacobiMatrix():
    
    @staticmethod
    def get_jacobi_matrix(nodes: [Node], y_matrix: numpy.ndarray) -> numpy.ndarray:
        node_count = len(nodes)
        jacobi_matrix = []
        for i in range(node_count):
            if nodes[i].type_node != 0:
                dp_u = []
                dq_u = []
                for j in range(node_count):
                    if nodes[j].type_node != 0:
                        pur = 0
                        pui = 0
                        qur = 0
                        qui = 0
                        if i == j:
                            for k in range(node_count):
                                if k != j:
                                    pur += y_matrix[i, k].real*nodes[k].voltage.real+y_matrix[i, k].imag*nodes[k].voltage.imag
                                    pui += y_matrix[i, k].real*nodes[k].voltage.imag-y_matrix[i, k].imag*nodes[k].voltage.real
                                    qur += y_matrix[i, k].real*nodes[k].voltage.imag-y_matrix[i, k].imag*nodes[k].voltage.real
                                    qui += y_matrix[i, k].real*nodes[k].voltage.real+y_matrix[i, k].imag*nodes[k].voltage.imag
                            pur = -2*y_matrix[i, i].real*nodes[i].voltage.real-pur
                            pui = -2*y_matrix[i, i].real*nodes[i].voltage.imag-pui
                            qur = 2*y_matrix[i, i].imag*nodes[i].voltage.real-qur
                            qui = 2*y_matrix[i, i].imag*nodes[i].voltage.imag+qui
                        else:
                            pur = -y_matrix[i, j].real*nodes[j].voltage.real+y_matrix[i, j].imag*nodes[j].voltage.imag
                            pui = -y_matrix[i, j].imag*nodes[j].voltage.real-y_matrix[i, j].real*nodes[j].voltage.imag
                            qur = y_matrix[i, j].imag*nodes[j].voltage.real+y_matrix[i, j].real*nodes[j].voltage.imag
                            qui = -y_matrix[i, j].real*nodes[j].voltage.real+y_matrix[i, j].imag*nodes[j].voltage.imag
                        dp_u.append(pur)
                        dp_u.append(pui)
                        dq_u.append(qur)
                        dq_u.append(qui)
                jacobi_matrix.append(dp_u)
                jacobi_matrix.append(dq_u)
                
        return numpy.array(jacobi_matrix)