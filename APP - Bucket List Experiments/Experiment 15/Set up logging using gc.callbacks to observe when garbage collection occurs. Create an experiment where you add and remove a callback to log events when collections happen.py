import gc
import logging
import random
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def gc_callback(phase, info):
    logger.info(f"GC phase: {phase}")
    if phase == 'stop':
        logger.info(f"GC stop phase completed. {info}")
    elif phase == 'start':
        logger.info(f"GC start phase started. {info}")

def setup_gc_logging():
    logger.info("Setting up GC callback...")
    gc.callbacks.append(gc_callback) 

    create_and_remove_objects()
    
    logger.info("Removing GC callback...")
    gc.callbacks.remove(gc_callback)  

    create_and_remove_objects()

def create_and_remove_objects():
    objects = []
    logger.info("Creating objects...")
    for _ in range(500):
        objects.append([random.randint(0, 1000) for _ in range(100)])

    logger.info("Deleting objects...")
    del objects
    gc.collect() 
def main():
    setup_gc_logging()

if __name__ == "__main__":
    main()
