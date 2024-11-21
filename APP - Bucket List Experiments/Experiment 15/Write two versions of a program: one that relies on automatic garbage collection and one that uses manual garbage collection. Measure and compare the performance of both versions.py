import gc
import random
import tracemalloc
import time

# Function to simulate object creation and deletion with automatic garbage collection
def automatic_gc_version():
    tracemalloc.start()
    start_time = time.time()

    # Simulating object creation
    objects = []
    for _ in range(1000):
        objects.append([random.randint(0, 1000) for _ in range(1000)])

    # Allow garbage collection to happen automatically when memory threshold is exceeded
    del objects  # Objects are deleted, but GC runs automatically at some point
    end_time = time.time()

    # Measure memory usage
    snapshot = tracemalloc.take_snapshot()
    print("Automatic GC version - Memory usage after deletion:")
    print_top_memory(snapshot)
    print(f"Time taken for automatic GC version: {end_time - start_time:.4f} seconds")

# Function to simulate object creation and deletion with manual garbage collection
def manual_gc_version():
    tracemalloc.start()
    start_time = time.time()

    # Simulating object creation
    objects = []
    for _ in range(1000):
        objects.append([random.randint(0, 1000) for _ in range(1000)])

    # Manually trigger garbage collection after object deletion
    del objects
    gc.collect()  # Manually trigger garbage collection
    end_time = time.time()

    # Measure memory usage
    snapshot = tracemalloc.take_snapshot()
    print("Manual GC version - Memory usage after manual GC:")
    print_top_memory(snapshot)
    print(f"Time taken for manual GC version: {end_time - start_time:.4f} seconds")

# Helper function to print top memory usage statistics
def print_top_memory(snapshot):
    top_stats = snapshot.statistics('lineno')
    print(f"Total memory used: {snapshot.statistics('traceback')[0].size / 1024:.2f} KB")
    print("Top 3 memory usage stats:")
    for stat in top_stats[:3]:
        print(stat)

# Run both versions
print("Running Automatic Garbage Collection Version...")
automatic_gc_version()
print("\n" + "="*50 + "\nRunning Manual Garbage Collection Version...")
manual_gc_version()
