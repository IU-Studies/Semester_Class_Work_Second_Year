import gc
import random

# Function to enable garbage collection debugging and create objects
def gc_debugging_experiment():
    # Enable garbage collection debugging flags
    gc.set_debug(gc.DEBUG_LEAK | gc.DEBUG_STATS | gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)

    # Create some objects to trigger garbage collection
    objects = []
    print("Creating objects...")
    for _ in range(1000):  # Create many objects
        objects.append([random.randint(0, 1000) for _ in range(100)])
    
    print("Objects created. Deleting them now...")
    
    # Delete the objects to make them eligible for collection
    del objects

    # Manually trigger garbage collection and print debug information
    gc.collect()

    # Clean up by disabling the debug flags
    gc.set_debug(0)

def main():
    gc_debugging_experiment()

if __name__ == "__main__":
    main()
