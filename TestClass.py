import unittest
from SystemClass import System
from NodeClass import Node
import NodeClass
from IncidentMatrixClass import IncidentMatrix
from BranchClass import Branch
import numpy
from YMatrixClass import YMatrix
from ImbalancesClass import Imbalances
from JacobiMatrixClass import JacobiMatrix
from LAESolverClass import LAESolver
from NewtonsMethodClass import NewtonsMethod


class DataTest():
    def get_data_test():
        system = System(220, 0.001)
        node_0 = Node(0, 124, 31.08, 2)
        node_0.initial_voltage(system)
        node_0.number = 0
        node_1 = Node(1, 96, 19.49, 2)
        node_1.initial_voltage(system)
        node_1.number = 1
        node_2 = Node(2, 104, 34.18, 2)
        node_2.initial_voltage(system)
        node_2.number = 2
        node_3 = Node(3, 106, 21.52, 1)
        node_3.initial_voltage(system)
        node_3.number = 3
        node_4 = Node(4, float('inf'), float('inf'), 0)
        node_4.initial_voltage(system)
        node_4.number = 4
        nodes = [node_0, node_1, node_2, node_3, node_4]
        branch_0 = Branch(3, 4, 4.9, 18.41, 5.42e-05)
        branch_1 = Branch(0, 4, 3.71, 22.39, 7.11e-05)
        branch_2 = Branch(0, 1, 4.2, 19.41, 5.91e-5)
        branch_3 = Branch(1, 4, 6.81, 31.49, 9.58e-5)
        branch_4 = Branch(2, 3, 2.73, 16.48, 2.09e-4)
        branch_5 = Branch(1, 2, 5.37, 20.16, 5.94e-5)
        branches = [branch_0, branch_1, branch_2, branch_3, branch_4, branch_5]
        
        return (system, nodes, branches)

class NodeClassTest(unittest.TestCase):
    def test_get_initial_values_1(self):
        system, nodes, branches = DataTest.get_data_test()
        node = nodes[0]
        node.initial_voltage(system)
        result = node.voltage
        expected_result = complex(220, 0)
        self.assertEqual(result, expected_result)
        
    def test_get_initial_values_2(self):
        system, nodes, branches = DataTest.get_data_test()
        node = nodes[4]
        node.initial_voltage(system)
        result = node.voltage
        expected_result = complex(220*1.1, 0)
        self.assertEqual(result, expected_result)
        
    def test_voltage_correction_1(self):
        system, nodes, branches = DataTest.get_data_test()
        y_matrix = YMatrix.get_y_matrix(branches, nodes)
        imbalances_s = Imbalances.get_imbalances_s(nodes, y_matrix)
        jacobi_matrix = JacobiMatrix.get_jacobi_matrix(nodes, y_matrix)
        delta_voltage = LAESolver.linear_algebraic_equation_solver(nodes, imbalances_s, jacobi_matrix)
        NodeClass.voltage_correction(nodes, delta_voltage)
        result = nodes[0].voltage
        expected_result = complex(239.93023631210755, 10.92175024143926)
        self.assertEqual(str(result), str(expected_result))
        
    def test_voltage_correction_2(self):
        system, nodes, branches = DataTest.get_data_test()
        y_matrix = YMatrix.get_y_matrix(branches, nodes)
        imbalances_s = Imbalances.get_imbalances_s(nodes, y_matrix)
        jacobi_matrix = JacobiMatrix.get_jacobi_matrix(nodes, y_matrix)
        delta_voltage = LAESolver.linear_algebraic_equation_solver(nodes, imbalances_s, jacobi_matrix)
        NodeClass.voltage_correction(nodes, delta_voltage)
        result = nodes[4].voltage
        expected_result = complex(242.00000000000003, 0)
        self.assertEqual(str(result), str(expected_result))

class IncidentMatrixClassTest(unittest.TestCase):
    def test_get_incident_matrix(self):
        system, nodes, branches = DataTest.get_data_test()
        result = IncidentMatrix.get_incident_matrix(branches, nodes)
        expected_result = numpy.array([[0., 1., 1., 0., 0., 0.], [0., 0., -1., 1., 0., 1.], [0., 0., 0., 0., 1., -1.], [1., 0., 0., 0., -1., 0.], [-1., -1., 0., -1., 0., 0.]])
        self.assertEqual(str(result), str(expected_result))
        
class YMatrixClassTest(unittest.TestCase):
    def test_get_y_matrix(self):
        system, nodes, branches = DataTest.get_data_test()
        result = YMatrix.get_y_matrix(branches, nodes)
        expected_result = complex(0.01785222629729499, -0.09255457728066185)
        self.assertEqual(str(result[0, 0]), str(expected_result))
        
class ImbalanceClassTest(unittest.TestCase):
    def test_get_imbalances_s(self):
        system, nodes, branches = DataTest.get_data_test()
        y_matrix = YMatrix.get_y_matrix(branches, nodes)
        result = Imbalances.get_imbalances_s(nodes, y_matrix)[0]
        expected_result = complex(-89.13836205206144, 185.61307451599623)
        self.assertEqual(str(result), str(expected_result))
        
class JacobiMatrixClassTest(unittest.TestCase):
    def test_get_jacobi_matrix(self):
        system, nodes, branches = DataTest.get_data_test()
        y_matrix = YMatrix.get_y_matrix(branches, nodes)
        result = JacobiMatrix.get_jacobi_matrix(nodes, y_matrix)[0, 0]
        expected_result = -3.769027794732449
        self.assertEqual(str(result), str(expected_result))
        
class LAESolverClassTest(unittest.TestCase):
    def test_linear_algebraic_equation_solver(self):
        system, nodes, branches = DataTest.get_data_test()
        y_matrix = YMatrix.get_y_matrix(branches, nodes)
        imbalances_s = Imbalances.get_imbalances_s(nodes, y_matrix)
        jacobi_matrix = JacobiMatrix.get_jacobi_matrix(nodes, y_matrix)
        result = LAESolver.linear_algebraic_equation_solver(nodes, imbalances_s, jacobi_matrix)[0]
        expected_result = complex(19.930236312107564, 10.92175024143926)
        self.assertEqual(str(result), str(expected_result))
        
class NewtonsMethodClassTest(unittest.TestCase):
    def test_solver(self):
        system, nodes, branches = DataTest.get_data_test()
        result = NewtonsMethod.solver(system, nodes, branches)[2]
        expected_result = complex(0.8664596057460869, 4.795282106922916)
        self.assertEqual(str(result), str(expected_result))
        
if __name__ == '__main__':
    unittest.main()