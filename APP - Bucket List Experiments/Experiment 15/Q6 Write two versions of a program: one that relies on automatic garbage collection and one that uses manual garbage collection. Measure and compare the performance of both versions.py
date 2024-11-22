#Write two versions of a program: one that relies on automatic garbage collection and one that uses manual garbage collection. 
#Measure and compare the performance of both versions.

import gc
import random
import tracemalloc
import time

def automatic_gc_version():
    tracemalloc.start()
    start_time = time.time()

    objects = []
    for _ in range(1000):
        objects.append([random.randint(0, 1000) for _ in range(1000)])

    del objects  
    end_time = time.time()

    snapshot = tracemalloc.take_snapshot()
    print("Automatic GC version - Memory usage after deletion:")
    print_top_memory(snapshot)
    print(f"Time taken for automatic GC version: {end_time - start_time:.4f} seconds")

def manual_gc_version():
    tracemalloc.start()
    start_time = time.time()

    objects = []
    for _ in range(1000):
        objects.append([random.randint(0, 1000) for _ in range(1000)])

    del objects
    gc.collect()  
    end_time = time.time()

    snapshot = tracemalloc.take_snapshot()
    print("Manual GC version - Memory usage after manual GC:")
    print_top_memory(snapshot)
    print(f"Time taken for manual GC version: {end_time - start_time:.4f} seconds")

def print_top_memory(snapshot):
    top_stats = snapshot.statistics('lineno')
    print(f"Total memory used: {snapshot.statistics('traceback')[0].size / 1024:.2f} KB")
    print("Top 3 memory usage stats:")
    for stat in top_stats[:3]:
        print(stat)

print("Running Automatic Garbage Collection Version...")
automatic_gc_version()
print("\n" + "="*50 + "\nRunning Manual Garbage Collection Version...")
manual_gc_version()
