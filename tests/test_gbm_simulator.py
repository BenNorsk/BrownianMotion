import pytest
import numpy as np
from pygbm.gbm_simulator import GBMSimulator


def test_initialization():
    # Test default initialization
    simulator = GBMSimulator()
    assert simulator.y0 == 1.0
    assert simulator.mu == 0.05
    assert simulator.sigma == 0.2
    assert simulator.T == 1.0
    assert simulator.N == 100
    assert simulator.path == []

def test_getters_setters():
    # Test setting and getting attributes
    simulator = GBMSimulator()
    
    simulator.y0 = 2.0
    simulator.mu = 0.1
    simulator.sigma = 0.3
    simulator.T = 2.0
    simulator.N = 200
    
    assert simulator.y0 == 2.0
    assert simulator.mu == 0.1
    assert simulator.sigma == 0.3
    assert simulator.T == 2.0
    assert simulator.N == 200

def test_simulate_path():
    # Test the simulate_path method
    simulator = GBMSimulator(y0=1.0, mu=0.05, sigma=0.2, T=1.0, N=100)
    path = simulator.simulate_path()
    
    # Check the path length matches the number of time steps + 1 (including the initial value)
    assert len(path) == simulator.N + 1
    
    # Check the path starts at y0
    assert path[0] == simulator.y0
    
    # Check that path is an instance of numpy.ndarray
    assert isinstance(path, np.ndarray)
    
    # Check that the path is stored in the simulator object
    assert np.array_equal(simulator.path, path)

def test_plot_method():
    # Test the plot method, ensuring it can be called without error
    simulator = GBMSimulator()
    simulator.simulate_path()  # Generate a path before plotting
    
    try:
        simulator.plot()  # Plot the path
    except Exception as e:
        pytest.fail(f"Plot method raised an exception: {e}")
