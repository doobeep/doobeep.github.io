import csv
import random

# Step 1: Get user input from the console
def get_user_input():
    try:
        eng = float(input("Enter energy rating (0-10): "))  # Prompt for energy input
        var = float(input("Enter emotion rating (0-10): "))  # Prompt for emotion input
        
        # Ensure the input is within the valid range
        if not (0 <= eng <= 10) or not (0 <= var <= 10):
            print("Please enter values between 0 and 10.")
            return get_user_input()  # Recursively call to get valid input
        
        return eng, var
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_user_input()  # Recursively call to handle invalid input

# Step 2: Scale the user input to [0, 1]
def scale_input(eng, var):
    scaled_eng = eng / 10
    scaled_var = var / 10
    return scaled_eng, scaled_var

# Step 3: Load the CSV file and parse it
def load_csv(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        tracks = [row for row in csv_reader]
    return tracks

# Step 4: Quicksort algorithm (randomized pivot)
def quicksort(arr, low, high, key):
    if low < high:
        pivot = partition(arr, low, high, key)
        quicksort(arr, low, pivot - 1, key)
        quicksort(arr, pivot + 1, high, key)

# Helper function for partitioning the array
def partition(arr, low, high, key):
    pivot = arr[high][key]
    i = low - 1
    for j in range(low, high):
        if arr[j][key] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Step 5: Find the closest match
def find_closest_song(tracks, scaled_eng, scaled_var):
    # Calculate the energy and valence bounds
    eng_lower = scaled_eng - 0.1
    eng_upper = scaled_eng + 0.1
    var_lower = scaled_var - 0.1
    var_upper = scaled_var + 0.1
    
    # Filter songs based on energy and valence within ±10%
    filtered_tracks = [track for track in tracks if 
                       eng_lower <= float(track['energy']) <= eng_upper and 
                       var_lower <= float(track['valence']) <= var_upper]
    
    # Sort filtered tracks by energy and valence
    quicksort(filtered_tracks, 0, len(filtered_tracks) - 1, 'energy')
    quicksort(filtered_tracks, 0, len(filtered_tracks) - 1, 'valence')
    
    if filtered_tracks:
        # Return the first song that matches
        closest_song = filtered_tracks[0]
        return closest_song['name'], closest_song['album'], closest_song['artists']
    else:
        return None

# Main logic
def main():
    # Step 1: Get user input
    eng, var = get_user_input()
    
    # Step 2: Scale the values
    scaled_eng, scaled_var = scale_input(eng, var)
    
    # Step 3: Load the CSV file
    tracks = load_csv('tracks_features.csv')
    
    # Step 4: Find the closest song
    closest_song = find_closest_song(tracks, scaled_eng, scaled_var)
    
    if closest_song:
        print(f"Closest Song: {closest_song[0]}")
        print(f"Album: {closest_song[1]}")
        print(f"Artists: {closest_song[2]}")
    else:
        print("No matching song found.")

# Run the program
if __name__ == "__main__":
    main()
