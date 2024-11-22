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
    obj_a = A()
    obj_b = B()
    obj_a.ref = obj_b
    obj_b.ref = obj_a

    return obj_a, obj_b

def experiment_with_circular_references():
    print("Creating circular references...")
    obj_a, obj_b = create_circular_references()

    del obj_a
    del obj_b

    print("\nForcing garbage collection...")
    gc.collect()

    print("\nUnreachable objects (if any) in gc.garbage:")
    for obj in gc.garbage:
        print(f"Unreachable object: {obj}")

    gc.garbage.clear()

def main():
    gc.set_debug(gc.DEBUG_LEAK)

    gc.collect()

    experiment_with_circular_references()

if __name__ == "__main__":
    main()
