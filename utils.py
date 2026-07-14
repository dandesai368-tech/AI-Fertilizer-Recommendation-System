"""
Utility functions for AI Fertilizer Recommendation System
"""

import pandas as pd

def load_data(file_path):
    """Load dataset from CSV file."""
    return pd.read_csv(file_path)

def validate_inputs(n, p, k, temperature, humidity, moisture, ph):
    """Validate user inputs."""
    if n < 0 or p < 0 or k < 0:
        return False
    return True
