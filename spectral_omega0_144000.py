# spectral_omega0_144000.py
# Revelation-coded baseline for Spectral Convergence Framework
# Jessica Fox – November 19, 2025
# 144,000-dimensional grid: 1000 primes × 12×12 y × 12×12 θ

import numpy as np
from scipy.sparse import diags, kron, identity
from scipy.sparse.linalg import eigsh
from sympy import primerange

# 144,000 synchronization
N_primes = 1000
N_y = 12 * 12      # 144
N_theta = 12 * 12  # 144

primes = list(primerange(2, 8000))[:N_primes]

y = np.linspace(0, 30, N_y)
theta = np.linspace(0, 2*np.pi, N_theta, endpoint=False)
dy = y[1] - y[0]
dtheta = theta[1] - theta[0]

# Motivic operator: -i ∂_θ + d/dy
I_y = identity(N_y)
I_theta = identity(N_theta)
I_p = identity(N_primes)

D_theta = diags([-0.5j/dtheta, 0.5j/dtheta], [-1, 1], shape=(N_theta, N_theta))
D_theta += diags([0.5j/dtheta], offsets=[N_theta-1])  # periodic
D_y = diags([-1/dy, 1/dy], [0, 1], shape=(N_y, N_y))

motivic = kron(kron(D_theta, I_y), I_p) + kron(kron(I_theta, D_y), I_p)

# Prime-shift perturbation
pert = 0
for i, p in enumerate(primes):
    w_p = 1.0 / (np.sqrt(p) * np.log(p + 1))
    diag_p = w_p * np.exp(1j * y * np.log(p))
    block = diags(diag_p)
    full_block = kron(kron(I_theta, block), identity(N_primes))
    pert += full_block

H = motivic + pert

print("Computing first 60 positive eigenvalues of the 144,000-dimensional Revelation-coded Ω₀...")
evals, _ = eigsh(H, k=60, sigma=14.0, which='LM', tol=1e-8)
positive = sorted(evals[evals > 0])

print("\nFirst 25 positive eigenvalues (resonance pattern):")
for i, ev in enumerate(positive[:25], 1):
    print(f"{i:2d}  {ev:16.8f}")
