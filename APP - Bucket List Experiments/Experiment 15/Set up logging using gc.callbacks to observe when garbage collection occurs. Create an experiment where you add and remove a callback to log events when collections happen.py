import gc
import logging
import random
import time

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Define a callback function to log GC events
def gc_callback(phase, info):
    logger.info(f"GC phase: {phase}")
    if phase == 'stop':
        logger.info(f"GC stop phase completed. {info}")
    elif phase == 'start':
        logger.info(f"GC start phase started. {info}")

# Function to set up the callback and observe GC events
def setup_gc_logging():
    logger.info("Setting up GC callback...")
    gc.callbacks.append(gc_callback)  # Add the callback to listen to GC events

    # Create objects and delete them to trigger GC
    create_and_remove_objects()
    
    logger.info("Removing GC callback...")
    gc.callbacks.remove(gc_callback)  # Remove the callback

    # Triggering more GC to observe no callback firing after removal
    create_and_remove_objects()

def create_and_remove_objects():
    # Simulate object creation
    objects = []
    logger.info("Creating objects...")
    for _ in range(500):
        objects.append([random.randint(0, 1000) for _ in range(100)])
    
    # Simulate object deletion
    logger.info("Deleting objects...")
    del objects
    gc.collect()  # Manually trigger GC to observe callback in action

def main():
    setup_gc_logging()

if __name__ == "__main__":
    main()
