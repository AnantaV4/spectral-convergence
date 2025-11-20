import numpy as np

class SpectralOperator:
    def __init__(self, dim=144000):
        self.dim = dim

    def step(self, x):
        # Replace with your actual operator logic
        return np.sin(x) + 0.001 * np.random.randn(*x.shape)
