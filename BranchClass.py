class Branch():
    
    def __init__(self, node_s, node_e, r_resistance, x_resistance, b_conductivity, t_max = 8760):
        self.node_s = node_s
        self.node_e = node_e
        self.z_resistance = complex(r_resistance, x_resistance)
        self.b_conductivity = b_conductivity
        self.s_loss = None
        self.w_loss = None
        self.t_max = t_max
        
def power_losses(branches: [Branch], nodes: [any]):
    for branch in branches:
        number_node = [None, None]
        for i, node in enumerate(nodes):
            if branch.node_s == node.name:
                number_node[0] = i
            if branch.node_e == node.name:
                number_node[1] = i
        voltage_drop = nodes[number_node[0]].voltage - nodes[number_node[1]].voltage
        element_current = voltage_drop / branch.z_resistance / 3**0.5
        branch.s_loss = abs(element_current)**2 * branch.z_resistance
        tau = (0.124 + branch.t_max / 10000)**2 * 8760
        branch.w_loss = tau * branch.s_loss.real
    
    return branches
        
def output_branches(branches: [Branch]):
    output_data = []
    for branch in branches:
        output_data.append([branch.node_s, branch.node_e, branch.s_loss, branch.w_loss])
    
    return output_data