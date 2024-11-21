import gc

class A:
    def __init__(self):
        self.ref = None

    def __del__(self):
        print(f"Object A with id {id(self)} is being finalized.")

class B:
    def __init__(self):
        self.ref = None

    def __del__(self):
        print(f"Object B with id {id(self)} is being finalized.")

def create_circular_references():
    # Create circular references between instances of A and B
    obj_a = A()
    obj_b = B()
    obj_a.ref = obj_b
    obj_b.ref = obj_a

    # Return the objects to break external references
    return obj_a, obj_b

def experiment_with_circular_references():
    print("Creating circular references...")
    # Create circular references
    obj_a, obj_b = create_circular_references()

    # Break external references to the objects
    del obj_a
    del obj_b

    # Force garbage collection
    print("\nForcing garbage collection...")
    gc.collect()

    # Check for unreachable objects in gc.garbage
    print("\nUnreachable objects (if any) in gc.garbage:")
    for obj in gc.garbage:
        print(f"Unreachable object: {obj}")

    # Clear gc.garbage
    gc.garbage.clear()

def main():
    # Enable garbage collection debugging
    gc.set_debug(gc.DEBUG_LEAK)

    # Manually run garbage collection
    gc.collect()

    # Run the experiment with circular references and garbage collection
    experiment_with_circular_references()

if __name__ == "__main__":
    main()
