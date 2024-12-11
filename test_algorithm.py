""" 
Testing the functionality of song_recommendation.py -- works
"""

import time
import random
from unittest.mock import patch  # To mock the input function
import song_recommendation  # Assuming song_recommendation.py is in the same folder

# Step 1: Simulate random user input (same as in song_recommendation.py)
def generate_random_input():
    eng = random.uniform(0, 10)
    var = random.uniform(0, 10)
    return eng, var

# Step 2: Test the runtime of the recommendation algorithm
def test_runtime(num_tests):
    total_time = 0
    
    for _ in range(num_tests):
        # Generate random input
        eng, var = generate_random_input()
        
        # Mocking the user input for both energy and emotion
        with patch('builtins.input', side_effect=[str(eng), str(var)]):
            # Measure the start time
            start_time = time.time()
            
            # Run the song recommendation function (assuming it's a part of the main function)
            song_recommendation.find_closest_song(song_recommendation.load_csv('tracks_features.csv'), 
                                                  eng / 10, var / 10)
            
            # Measure the end time and calculate the elapsed time
            end_time = time.time()
            elapsed_time = end_time - start_time
            total_time += elapsed_time
            
            print(f"Test {_ + 1}: {elapsed_time:.4f} seconds")
    
    # Step 3: Calculate and print the average time
    average_time = total_time / num_tests
    print(f"Average time for {num_tests} tests: {average_time:.4f} seconds")

# Run the test with a specified number of iterations (e.g., 10)
if __name__ == "__main__":
    test_runtime(10)
