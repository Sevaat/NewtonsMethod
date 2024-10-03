class Node():
    
    def __init__(self, name, p_power, q_power, type_node):
        self.s_power = complex(p_power, q_power)
        self.voltage = None
        self.type_node = type_node # 0 - ИП, 1 - ОИП, 2 - Н
        self.name = name
        
    def initial_voltage(self, system):
        if self.type_node == 0:
            self.voltage = complex(1.1 * system.voltage_nom, 0)
        else:
            self.voltage = complex(system.voltage_nom, 0)
            
    def _node_voltage_correction(self, delta_voltage: complex):
        self.voltage = self.voltage + delta_voltage
        
def voltage_correction(nodes: [Node], delta_voltage: list):
    j = 0
    for i in range(len(nodes)):
        if nodes[i].type_node != 0:
            nodes[i].voltage = nodes[i].voltage + delta_voltage[j]
            j += 1
            
def output_nodes(nodes: [Node]):
    output_data = []
    for node in nodes:
        output_data.append([node.name, node.voltage, abs(node.voltage)])
    
    return output_data