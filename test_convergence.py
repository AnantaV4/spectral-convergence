from spectral_convergence import run_operator
import numpy as np

def test_run_operator_basic():
    hist = run_operator(dim=1000, steps=10)
    assert isinstance(hist, np.ndarray)
    assert hist.shape == (10,)
    assert np.all(np.isfinite(hist))
