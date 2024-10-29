import numpy as np
from .gbm_simulator import GBMSimulator

class MilsteinGBMSimulator(GBMSimulator):
    """
    This class simulates a path of the Geometric Brownian Motion using the Milstein method.
    Args:
        y0 (float): The initial value of the GBM
        mu (float): The drift parameter
        sigma (float): The volatility parameter
        T (float): The time horizon
        N (int): The number of time steps
    Attributes:
        y0 (float): The initial value of the GBM
        mu (float): The drift parameter
        sigma (float): The volatility parameter
        T (float): The time horizon
        N (int): The number of time steps
        path (numpy.ndarray): The simulated path of the GBM
    """
    def __init__(self, y0=1.0, mu=0.05, sigma=0.2, T=1.0, N=100):
        super().__init__(y0, mu, sigma, T, N)
        self._plot_title = "Milstein GBM Path"

    # Overriding the simulate_path method to use the Milstein method
    def simulate_path(self):
        """
        This method simulates a path of the Geometric Brownian Motion using the Milstein method.
        Args:
            None
        Returns:
            numpy.ndarray: An array containing the simulated path
        """
        dt = self._T / self._N  # time step
        path = [self._y0]  # initial value
        
        for _ in range(1, self._N + 1):
            prev_value = path[-1]
            dW = np.random.normal(0, np.sqrt(dt))  # Brownian increment
            # Milstein approximation formula with additional correction term
            next_value = (prev_value 
                          + self._mu * prev_value * dt 
                          + self._sigma * prev_value * dW 
                          + 0.5 * self._sigma**2 * prev_value * (dW**2 - dt))
            path.append(next_value)
        
        self._path = np.array(path)
        return self._path