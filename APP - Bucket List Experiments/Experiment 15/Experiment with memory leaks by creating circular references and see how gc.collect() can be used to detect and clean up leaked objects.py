import gc

class CircularReference:
    def __init__(self):
        self.ref = None

def create_circular_references():
    obj1 = CircularReference()
    obj2 = CircularReference()

    # Create a circular reference
    obj1.ref = obj2
    obj2.ref = obj1

    return obj1, obj2

def experiment_with_circular_references():
    print("Initial garbage collection:")
    gc.collect()  # Clean up any leftover objects
    show_unreachable_objects()

    # Create circular references
    print("\nCreating circular references...")
    obj1, obj2 = create_circular_references()
    print(f"Objects created: {obj1}, {obj2}")

    # Delete references to the objects
    del obj1, obj2
    print("References deleted.")

    # Check for unreachable objects before and after running gc.collect()
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
        for obj in unreachable[:5]:  # Show details of up to 5 objects
            print(f"  {obj}")
    else:
        print("No unreachable objects found.")

# Enable debugging of the garbage collector to track leaks
gc.set_debug(gc.DEBUG_LEAK)

# Run the experiment
experiment_with_circular_references()
