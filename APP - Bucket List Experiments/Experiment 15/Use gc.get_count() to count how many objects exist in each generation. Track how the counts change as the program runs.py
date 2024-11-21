import gc
import random
import time

def show_gc_counts():
    gen_counts = gc.get_count()
    print(f"Generation 0: {gen_counts[0]} objects")
    print(f"Generation 1: {gen_counts[1]} objects")
    print(f"Generation 2: {gen_counts[2]} objects")

def track_gc_counts():
    print("Initial state:")
    show_gc_counts()

    # Create objects to populate Generation 0
    print("\nCreating objects...")
    temp_objects = []
    for _ in range(5000):  # Creating a large number of objects
        temp_objects.append([random.randint(0, 100) for _ in range(100)])
    show_gc_counts()

    # Simulate some idle time
    print("\nSimulating idle time...")
    time.sleep(1)
    show_gc_counts()

    # Delete objects
    print("\nDeleting objects...")
    del temp_objects
    show_gc_counts()

    # Trigger garbage collection manually
    print("\nTriggering garbage collection manually...")
    gc.collect()
    show_gc_counts()

# Run the tracking
track_gc_counts()
