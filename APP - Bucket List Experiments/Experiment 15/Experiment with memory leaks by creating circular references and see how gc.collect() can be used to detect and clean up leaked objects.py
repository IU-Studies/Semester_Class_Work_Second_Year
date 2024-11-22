import gc

class CircularReference:
    def __init__(self):
        self.ref = None

def create_circular_references():
    obj1 = CircularReference()
    obj2 = CircularReference()

    obj1.ref = obj2
    obj2.ref = obj1

    return obj1, obj2

def experiment_with_circular_references():
    print("Initial garbage collection:")
    gc.collect() 
    show_unreachable_objects()

    print("\nCreating circular references...")
    obj1, obj2 = create_circular_references()
    print(f"Objects created: {obj1}, {obj2}")

    del obj1, obj2
    print("References deleted.")

    print("\nBefore running gc.collect():")
    show_unreachable_objects()

    print("\nRunning gc.collect()...")
    collected = gc.collect()
    print(f"Garbage collector cleaned up {collected} objects.")

    print("\nAfter running gc.collect():")
    show_unreachable_objects()

def show_unreachable_objects():
    unreachable = gc.garbage
    if unreachable:
        print(f"Unreachable objects: {len(unreachable)}")
        for obj in unreachable[:5]: 
            print(f"  {obj}")
    else:
        print("No unreachable objects found.")

gc.set_debug(gc.DEBUG_LEAK)

experiment_with_circular_references()
