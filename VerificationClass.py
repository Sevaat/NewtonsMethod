from SystemClass import System
from NodeClass import Node


class Verification():
    
    @staticmethod
    def get_next_iteration(nodes: [Node], imbalances_s: list, system: System) -> bool:
        for i, imb_s in enumerate(imbalances_s):
            if nodes[i].type_node != 0:
                if abs(imb_s.real) > system.eps:
                    return True
                if abs(imb_s.imag) > system.eps:
                    return True
        return False