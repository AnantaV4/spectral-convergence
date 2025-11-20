import matplotlib.pyplot as plt
import numpy as np

def plot_convergence(history, save=True, path="img/convergence_plot.png"):
    plt.figure(figsize=(8,5))
    plt.plot(history)
    plt.xlabel("Iteration")
    plt.ylabel("Mean Absolute Value")
    plt.title("Spectral Convergence")
    plt.tight_layout()

    if save:
        plt.savefig(path, dpi=300)

    plt.show()
