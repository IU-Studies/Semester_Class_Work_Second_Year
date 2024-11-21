import gc
import tracemalloc

class LargeObject:
    def __init__(self, size):
        self.data = [0] * size

def create_and_delete_objects():
    tracemalloc.start()
    print("Initial memory usage:")
    print_memory_usage()

    # Create objects
    objects = [LargeObject(10**6) for _ in range(5)]
    print("\nMemory usage after creating objects:")
    print_memory_usage()

    # Delete objects
    del objects
    print("\nMemory usage after deleting objects (before gc.collect):")
    print_memory_usage()

    # Manually trigger garbage collection
    gc.collect()
    print("\nMemory usage after gc.collect():")
    print_memory_usage()

def print_memory_usage():
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print(f"Total memory used: {snapshot.statistics('traceback')[0].size / 1024:.2f} KB")
    print("Top 3 memory usage stats:")
    for stat in top_stats[:3]:
        print(stat)

create_and_delete_objects()
