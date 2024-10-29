import argparse
import numpy as np
from gbm_simulator import GBMSimulator
from euler_maruyama_gbm_simulator import EulerMaruyamaGBMSimulator
from milstein_gbm_simulator import MilsteinGBMSimulator
from uniplot import plot
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(description="Geometric Brownian Motion (GBM) Simulator CLI")
    
    subparsers = parser.add_subparsers(dest="command")
    
    # 'simulate' command
    simulate_parser = subparsers.add_parser("simulate", help="Simulate a GBM path")
    simulate_parser.add_argument("--y0", type=float, default=1.0, help="Initial value of GBM")
    simulate_parser.add_argument("--mu", type=float, default=0.05, help="Drift parameter")
    simulate_parser.add_argument("--sigma", type=float, default=0.2, help="Volatility parameter")
    simulate_parser.add_argument("--T", type=float, default=1.0, help="Time horizon")
    simulate_parser.add_argument("--N", type=int, default=100, help="Number of time steps")
    simulate_parser.add_argument("--method", choices=["gbm", "euler", "milstein"], default="gbm", help="Simulation method")
    simulate_parser.add_argument("--output", type=str, default="gbm_plot.png", help="Output file name for the plot")
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    if args.command == "simulate":
        # Choose the appropriate simulator based on the method
        if args.method == "gbm":
            simulator = GBMSimulator(y0=args.y0, mu=args.mu, sigma=args.sigma, T=args.T, N=args.N)
        elif args.method == "euler":
            simulator = EulerMaruyamaGBMSimulator(y0=args.y0, mu=args.mu, sigma=args.sigma, T=args.T, N=args.N)
        elif args.method == "milstein":
            simulator = MilsteinGBMSimulator(y0=args.y0, mu=args.mu, sigma=args.sigma, T=args.T, N=args.N)
        
        # Simulate the path
        data = simulator.simulate_path()

        # Plot and save the plot to the specified output file
        simulator.plot()

        # Save a matplotlib plot

        print(f"Plot saved as '{args.output}'.")

if __name__ == "__main__":
    main()
