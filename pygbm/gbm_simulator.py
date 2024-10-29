import numpy as np
from uniplot import plot

class GBMSimulator:
    """
    This class simulates a path of the Geometric Brownian Motion.
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
        # Initialize parameters with default values
        self._y0 = y0
        self._mu = mu
        self._sigma = sigma
        self._T = T
        self._N = N
        self._path = []
        self._plot_title = "Geometric Brownian Motion Path"

    # Getter and Setter for y0
    @property
    def y0(self):
        return self._y0

    @y0.setter
    def y0(self, value):
        self._y0 = value

    # Getter and Setter for mu
    @property
    def mu(self):
        return self._mu

    @mu.setter
    def mu(self, value):
        self._mu = value

    # Getter and Setter for sigma
    @property
    def sigma(self):
        return self._sigma

    @sigma.setter
    def sigma(self, value):
        self._sigma = value

    # Getter and Setter for T
    @property
    def T(self):
        return self._T

    @T.setter
    def T(self, value):
        self._T = value

    # Getter and Setter for N
    @property
    def N(self):
        return self._N

    @N.setter
    def N(self, value):
        self._N = value
    
    # Getter and Setter for path
    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, value):
        self._path = value

    # Method to simulate the GBM path
    def simulate_path(self):
        """
        This method simulates a path of the Geometric Brownian Motion.
        Args:
            None
        Returns:
            numpy.ndarray: An array containing the simulated path
        """
        dt = self._T / self._N  # time step
        path = [self._y0]  # initial value

        for _ in range(1, self._N + 1):
            # Generate a random Brownian increment
            dW = np.random.normal(0, np.sqrt(dt))
            # Calculate the next value using the GBM formula
            next_value = path[-1] * np.exp((self._mu - 0.5 * self._sigma ** 2) * dt + self._sigma * dW)
            path.append(next_value)
        self._path = np.array(path)
        return np.array(path)
    
    def plot(self):
        """
        This method plots the simulated path of the Geometric Brownian Motion in the CLI."
        Args:
            None
        Returns:
            None
        """
        plot(self._path, title=self._plot_title)
        return None


