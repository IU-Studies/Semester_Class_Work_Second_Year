import logging

# Configure the logger
logging.basicConfig(
    level=logging.ERROR,  # Log only error messages and above
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='error.log',
    filemode='a'
)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.exception("Exception occurred in divide function")
        return None

def main():
    numbers = [(10, 2), (5, 0), (8, 4), (7, 0)]
    for num, denom in numbers:
        result = divide(num, denom)
        if result is not None:
            print(f"Result of {num} / {denom} = {result}")
        else:
            print(f"Division of {num} by {denom} failed.")

main()