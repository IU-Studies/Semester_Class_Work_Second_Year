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

    print("\nCreating objects...")
    temp_objects = []
    for _ in range(5000):  
        temp_objects.append([random.randint(0, 100) for _ in range(100)])
    show_gc_counts()

    print("\nSimulating idle time...")
    time.sleep(1)
    show_gc_counts()

    print("\nDeleting objects...")
    del temp_objects
    show_gc_counts()

    print("\nTriggering garbage collection manually...")
    gc.collect()
    show_gc_counts()

track_gc_counts()
