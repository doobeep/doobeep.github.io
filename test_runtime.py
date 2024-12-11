"""
Creates temporary csv files IN MEMORY ranging from size n = 0 to 10,000, 
where n is the number of rows, with columns [name, album, artists, energy, valence],
and fills them with dummy data.  

** should not create actual csv files!! just temp dictionaries

Then creates a two column csv data file, "runtime_test_results.csv", documenting 
the relationship between row size (position/column 0) and alg run time of of 
that row size (position/column 1). Tests in increments of 100.

Using this to graph the results of the algorithm.
"""

import csv
import random
import time
from unittest.mock import patch
from song_recommendation import find_closest_song

# Step 1: Generate Dummy Data
def generate_dummy_data(n):
    """Generate dummy data as a list of dictionaries."""
    data = []
    for _ in range(n):
        name = f"Song_{random.randint(1, 10000)}"
        album = f"Album_{random.randint(1, 1000)}"
        artists = f"Artist_{random.randint(1, 500)}"  # Corrected key to 'artists'
        energy = random.uniform(0.0, 1.0)
        valence = random.uniform(0.0, 1.0)
        data.append({"name": name, "album": album, "artists": artists, "energy": energy, "valence": valence})
    return data


# Step 2: Test Runtime on Dummy Data
def test_runtime_on_dummy_data(n):
    """Test the runtime of song_recommendation.py using dummy data with n rows."""
    # Generate dummy data
    dummy_data = generate_dummy_data(n)

    # Generate random input
    eng = random.uniform(0, 10)
    var = random.uniform(0, 10)

    # Mock user input
    with patch('builtins.input', side_effect=[str(eng), str(var)]):
        # Measure runtime
        start_time = time.time()
        find_closest_song(dummy_data, eng / 10, var / 10)
        end_time = time.time()

        # Return runtime in milliseconds
        return (end_time - start_time) * 1000

# Step 3: Generate Runtime Test Results
def generate_runtime_test_results():
    """Generate runtime test results and save to runtime_test_results.csv."""
    results_file = "runtime_test_results.csv"

    with open(results_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["Number of Rows", "Runtime (ms)"])

        # Test for n ranging from 0 to 10,000 with at least 99 data points
        step = 50
        for n in range(0, 20000, step):
            runtime = test_runtime_on_dummy_data(n)
            writer.writerow([n, runtime])
            print(f"Tested n={n}, Runtime={runtime:.2f} ms")

if __name__ == "__main__":
    generate_runtime_test_results()
