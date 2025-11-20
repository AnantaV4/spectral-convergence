import numpy as np
from tqdm import tqdm
from .operators import SpectralOperator

def run_operator(dim=144000, steps=200):
    op = SpectralOperator(dim)

    x = np.random.randn(dim)
    history = []

    for _ in tqdm(range(steps)):
        x = op.step(x)
        history.append(np.mean(np.abs(x)))

    return np.array(history)
