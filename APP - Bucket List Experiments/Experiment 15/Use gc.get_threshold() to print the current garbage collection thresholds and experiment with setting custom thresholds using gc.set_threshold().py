#Use gc.get_threshold() to print the current garbage collection thresholds and experiment with setting custom thresholds using gc.set_threshold().

import gc

def show_gc_thresholds():
    print("Current GC thresholds:")
    thresholds = gc.get_threshold()
    print(f"Generation 0: {thresholds[0]}, Generation 1: {thresholds[1]}, Generation 2: {thresholds[2]}")

def experiment_with_thresholds():
    print("\nExperiment with default thresholds:")
    show_gc_thresholds()
    simulate_gc_activity()

    print("\nSetting custom thresholds...")
    gc.set_threshold(500, 10, 5)
    show_gc_thresholds()
    simulate_gc_activity()

    print("\nResetting thresholds to default...")
    gc.set_threshold(700, 10, 10)  
    show_gc_thresholds()
    simulate_gc_activity()

def simulate_gc_activity():
    large_objects = []
    print("Simulating object creation...")
    for _ in range(1000): 
        large_objects.append([0] * 1000)
    del large_objects
    print("Objects deleted. Triggering garbage collection manually.")
    gc.collect()

experiment_with_thresholds()
