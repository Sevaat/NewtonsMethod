from BranchClass import Branch
from NodeClass import Node
import numpy


class IncidentMatrix():
    
    @staticmethod
    def get_incident_matrix(branches: [Branch], nodes: [Node]) -> numpy.ndarray:
        incident_matrix = numpy.zeros((len(nodes), len(branches)))
        for i, branch in enumerate(branches):
            number_node = [None, None]
            for j, node in enumerate(nodes):
                if branch.node_s == node.name:
                    number_node[0] = j
                if branch.node_e == node.name:
                    number_node[1] = j
            incident_matrix[number_node[0], i] = 1
            incident_matrix[number_node[1], i] = -1
        
        return incident_matrix