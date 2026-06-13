"""
================================================================================
PROJECT: Interactive Algorithm Visualizer
DESCRIPTION: Demonstrates deep understanding of computer science fundamentals by 
             visually rendering a Bubble Sort algorithm in real-time. Uses Python 
             Generators ('yield') to pass sorting states to a rendering engine.
================================================================================
"""

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bubble_sort(arr):
    """
    A standard bubble sort algorithm modified into a Python Generator.
    
    Why a generator? 
    Instead of running the entire sort instantly and returning the final result,
    using 'yield' pauses the function's execution after every single swap. 
    This allows our graphics loop to grab the intermediate array and draw it 
    frame-by-frame on the screen.
    """
    n = len(arr)
    
    # Outer loop handles the total number of passes needed
    for i in range(n):
        swapped = False
        
        # Inner loop compares adjacent elements, pushing the largest to the right
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Python tuple unpacking swaps values without needing a temporary variable
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            
            # Pause execution and hand the current array state to Matplotlib
            yield arr
            
        # Optimization: If we made a full pass without any swaps, it's fully sorted
        if not swapped:
            break

def update_graph(arr, rects, text, iteration_tracker):
    """
    Callback function triggered by Matplotlib's FuncAnimation.
    Takes the newly yielded array and updates the physical bar heights.
    """
    # The 'zip' function pairs the physical bar rectangles with the new array integers
    for rect, val in zip(rects, arr):
        rect.set_height(val)
        
    # Increment our operation counter and update the text label
    iteration_tracker[0] += 1
    text.set_text(f"Array Operations: {iteration_tracker[0]}")
    
    return rects

# ==========================================
# GRAPHICAL SETUP & EXECUTION
# ==========================================
if __name__ == "__main__":
    # 1. Initialize our unsorted dataset
    amount_of_numbers = 30
    
    # Creates a list [1, 2, 3... 30] and scrambles it
    arr = [x + 1 for x in range(amount_of_numbers)] 
    random.shuffle(arr)

    # 2. Configure the drawing board (Matplotlib figure)
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0f172a')
    ax.set_title("O(n²) Bubble Sort Real-Time Visualization", fontsize=16, color='white')
    ax.set_facecolor('#0f172a')
    ax.set_xlim(0, amount_of_numbers)
    ax.set_ylim(0, amount_of_numbers + 2)
    ax.axis('off') # Hide axes for a cleaner bar-chart look

    # 3. Create the initial, unsorted physical bars
    rects = ax.bar(range(amount_of_numbers), arr, align="edge", color="#06b6d4", edgecolor="#164e63")
    
    # Setup text telemetry on the screen
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12, color='white')
    
    # We use a list to store the iteration count so it can be mutated inside the function
    iteration_tracker = [0] 

    # 4. Bind the sorting generator to the graphics loop
    # frames=bubble_sort(arr) continuously asks the generator for the next array state
    anim = animation.FuncAnimation(
        fig, 
        func=update_graph, 
        fargs=(rects, text, iteration_tracker), 
        frames=bubble_sort(arr), 
        interval=50,      # Milliseconds to wait between visual updates
        repeat=False,     # Stop when the array is sorted
        cache_frame_data=False
    )

    plt.tight_layout()
    plt.show()