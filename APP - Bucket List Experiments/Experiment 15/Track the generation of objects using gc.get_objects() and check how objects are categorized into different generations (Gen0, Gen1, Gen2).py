import gc
import random
import time

def show_gc_generations():
    gen_count = gc.get_count()
    print(f"Generation 0: {gen_count[0]} objects")
    print(f"Generation 1: {gen_count[1]} objects")
    print(f"Generation 2: {gen_count[2]} objects")
    
def track_object_generations():
    gc.collect()  
    print("Initial garbage collection completed.")
    show_gc_generations()

    created_objects = []
    print("\nCreating objects...")
    for _ in range(1000): 
        created_objects.append([random.randint(0, 1000) for _ in range(100)])
    print(f"{len(created_objects)} objects created.")
    show_gc_generations()

    time.sleep(2)

    del created_objects
    print("\nObjects deleted.")
    show_gc_generations()

    gc.collect()
    print("\nManual garbage collection triggered.")
    show_gc_generations()

def print_all_objects():
    all_objects = gc.get_objects()
    print(f"\nTotal objects tracked: {len(all_objects)}")
    gen0_objects = [obj for obj in all_objects if gc.get_count()[0] > 0]
    gen1_objects = [obj for obj in all_objects if gc.get_count()[1] > 0]
    gen2_objects = [obj for obj in all_objects if gc.get_count()[2] > 0]
    print(f"Objects in Generation 0: {len(gen0_objects)}")
    print(f"Objects in Generation 1: {len(gen1_objects)}")
    print(f"Objects in Generation 2: {len(gen2_objects)}")

track_object_generations()

print_all_objects()
