#Enable debugging flags in the gc module using gc.set_debug(), 
#then create and collect objects. Print out debug information to understand garbage collection operations.

import gc
import random

def gc_debugging_experiment():
    gc.set_debug(gc.DEBUG_LEAK | gc.DEBUG_STATS | gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)

    objects = []
    print("Creating objects...")
    for _ in range(1000): 
        objects.append([random.randint(0, 1000) for _ in range(100)])
    
    print("Objects created. Deleting them now...")

    del objects

    gc.collect()

    gc.set_debug(0)

def main():
    gc_debugging_experiment()

if __name__ == "__main__":
    main()
