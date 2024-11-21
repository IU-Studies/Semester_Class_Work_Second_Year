import gc
import random
import time

def show_gc_generations():
    # Get the count of objects in each generation
    gen_count = gc.get_count()
    print(f"Generation 0: {gen_count[0]} objects")
    print(f"Generation 1: {gen_count[1]} objects")
    print(f"Generation 2: {gen_count[2]} objects")
    
def track_object_generations():
    gc.collect()  # Run initial garbage collection to clean up any leftover objects
    print("Initial garbage collection completed.")
    show_gc_generations()

    # Create some objects and track their generations
    created_objects = []
    print("\nCreating objects...")
    for _ in range(1000):  # Create many objects
        created_objects.append([random.randint(0, 1000) for _ in range(100)])
    print(f"{len(created_objects)} objects created.")
    show_gc_generations()

    # Simulate a delay to give objects time to move between generations
    time.sleep(2)

    # Now delete objects and track the garbage collection
    del created_objects
    print("\nObjects deleted.")
    show_gc_generations()
    
    # Manually trigger garbage collection
    gc.collect()
    print("\nManual garbage collection triggered.")
    show_gc_generations()

def print_all_objects():
    # Optionally print all objects and their generations for inspection
    all_objects = gc.get_objects()
    print(f"\nTotal objects tracked: {len(all_objects)}")
    gen0_objects = [obj for obj in all_objects if gc.get_count()[0] > 0]
    gen1_objects = [obj for obj in all_objects if gc.get_count()[1] > 0]
    gen2_objects = [obj for obj in all_objects if gc.get_count()[2] > 0]
    print(f"Objects in Generation 0: {len(gen0_objects)}")
    print(f"Objects in Generation 1: {len(gen1_objects)}")
    print(f"Objects in Generation 2: {len(gen2_objects)}")

# Track object generations
track_object_generations()

# Optionally, print all objects and their generation distribution
print_all_objects()
