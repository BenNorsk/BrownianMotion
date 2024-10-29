import pytest
import numpy as np
from pygbm.euler_maruyama_gbm_simulator import EulerMaruyamaGBMSimulator

def test_initialization():
    # Test default initialization
    simulator = EulerMaruyamaGBMSimulator()
    assert simulator.y0 == 1.0
    assert simulator.mu == 0.05
    assert simulator.sigma == 0.2
    assert simulator.T == 1.0
    assert simulator.N == 100
    assert simulator.path == []

def test_getters_and_setters():
    # Test setting and getting values
    simulator = EulerMaruyamaGBMSimulator()
    
    simulator.y0 = 2.0
    assert simulator.y0 == 2.0

    simulator.mu = 0.1
    assert simulator.mu == 0.1

    simulator.sigma = 0.3
    assert simulator.sigma == 0.3

    simulator.T = 2.0
    assert simulator.T == 2.0

    simulator.N = 200
    assert simulator.N == 200

def test_simulate_path_length():
    # Test that the path length matches the number of steps (N + 1)
    simulator = EulerMaruyamaGBMSimulator(N=50)
    path = simulator.simulate_path()
    assert isinstance(path, np.ndarray)
    assert len(path) == 51  # N + 1 because it includes the initial value

def test_simulate_path_positive():
    # Test that all values in the path are positive
    simulator = EulerMaruyamaGBMSimulator()
    path = simulator.simulate_path()
    assert np.all(path > 0), "Path contains non-positive values, which is unexpected in GBM."

def test_path_updates_after_simulation():
    # Test that the _path attribute updates after calling simulate_path
    simulator = EulerMaruyamaGBMSimulator()
    simulator.simulate_path()
    assert simulator.path is not None
    assert len(simulator.path) == simulator.N + 1  # Check that _path has the expected length
    assert np.all(simulator.path > 0), "Path contains non-positive values."
