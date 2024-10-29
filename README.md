# BrownianMotion
A package which simulates Brownian Motion.

# Example usage:
# Create a GBMSimulator instance with default parameters
simulator = GBMSimulator(y0=1.0, mu=0.05, sigma=0.2, T=1.0, N=30)
simulator.simulate_path()
simulator.plot_path()
print(simulator.path)
