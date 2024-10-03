from NodeClass import Node
from ImbalancesClass import Imbalances
from SystemClass import System
from NodeClass import Node
import NodeClass
from BranchClass import Branch
import BranchClass
from YMatrixClass import YMatrix
from JacobiMatrixClass import JacobiMatrix
from LAESolverClass import LAESolver
from VerificationClass import Verification


class NewtonsMethod():
    
    @staticmethod
    def solver(system: System, nodes: [Node], branches: [Branch], iterations = 100):
        y_matrix = YMatrix.get_y_matrix(branches, nodes)
        for i in range(0, 100):
            imbalances_s = Imbalances.get_imbalances_s(nodes, y_matrix)
            if not Verification.get_next_iteration(nodes, imbalances_s, system):
                nodes_data = NodeClass.output_nodes(nodes)
                branches = BranchClass.power_losses(branches, nodes)
                branches_data = BranchClass.output_branches(branches)
                system.loss_calculation(branches)
                s_losses = system.s_losses
                w_losses = system.w_losses
                return [nodes_data, branches_data, s_losses, w_losses]
            jacobi_matrix = JacobiMatrix.get_jacobi_matrix(nodes, y_matrix)
            delta_voltage = LAESolver.linear_algebraic_equation_solver(nodes, imbalances_s, jacobi_matrix)
            NodeClass.voltage_correction(nodes, delta_voltage)