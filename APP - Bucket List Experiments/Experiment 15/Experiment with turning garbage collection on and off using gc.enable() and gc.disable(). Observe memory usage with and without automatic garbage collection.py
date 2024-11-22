#Experiment with turning garbage collection on and off using gc.enable() and gc.disable(). 
#Observe memory usage with and without automatic garbage collection.

import gc
import tracemalloc
import time

def create_large_list():
    return [x for x in range(10**6)]

def experiment_with_gc():
    tracemalloc.start()
    gc.disable()
    print("Garbage collection is disabled")
    start_time = time.time()
    large_list = [create_large_list() for _ in range(10)]
    end_time = time.time()
    snapshot = tracemalloc.take_snapshot()
    print("Memory usage with GC disabled:")
    for stat in snapshot.statistics('lineno')[:5]:
        print(stat)
    del large_list
    gc.collect()  # Manually triggering garbage collection
    print("Garbage collected manually")
    print("Time taken:", end_time - start_time)
    snapshot = tracemalloc.take_snapshot()
    print("Memory usage after manual GC:")
    for stat in snapshot.statistics('lineno')[:5]:
        print(stat)

def experiment_without_gc():
    tracemalloc.start()
    gc.enable()
    print("Garbage collection is enabled")
    start_time = time.time()
    large_list = [create_large_list() for _ in range(10)]
    end_time = time.time()
    snapshot = tracemalloc.take_snapshot()
    print("Memory usage with GC enabled:")
    for stat in snapshot.statistics('lineno')[:5]:
        print(stat)
    del large_list
    print("Garbage collected automatically")
    print("Time taken:", end_time - start_time)
    snapshot = tracemalloc.take_snapshot()
    print("Memory usage after automatic GC:")
    for stat in snapshot.statistics('lineno')[:5]:
        print(stat)

experiment_with_gc()
print("=" * 50)
experiment_without_gc()
