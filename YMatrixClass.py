from BranchClass import Branch
from NodeClass import Node
import numpy
from IncidentMatrixClass import IncidentMatrix


class YMatrix():
    
    @staticmethod
    def get_y_matrix(branches: [Branch], nodes: [Node]) -> numpy.ndarray:
        y_matrix = numpy.array([1 / branch.z_resistance for branch in branches])
        incident_matrix = IncidentMatrix.get_incident_matrix(branches, nodes)
        y_matrix = numpy.dot(incident_matrix, numpy.diag(y_matrix))
        y_matrix = numpy.dot(y_matrix, incident_matrix.transpose())
        
        b_conductivity = []
        for i in range(len(nodes)):
            b = 0
            for j in range(len(nodes)):
                if incident_matrix[i, j] != 0.:
                    b += branches[j].b_conductivity
            b_conductivity.append(b)
        b_conductivity = [complex(0, b) for b in b_conductivity]
        b_conductivity = numpy.array(b_conductivity)
        b_conductivity = numpy.diag(b_conductivity)
        
        y_matrix = y_matrix + b_conductivity
        
        return y_matrix