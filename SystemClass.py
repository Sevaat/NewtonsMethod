class System():
    
    def __init__(self, voltage_nom, eps):
        self.voltage_nom = voltage_nom
        self.eps = eps
        self.s_losses = None
        self.w_losses = None
        
    def loss_calculation(self, branches: [any]):
        self.s_losses = sum([branch.s_loss for branch in branches])
        self.w_losses = sum([branch.w_loss for branch in branches])