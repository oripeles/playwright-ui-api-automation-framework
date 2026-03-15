import random
import time

def generate_unique_email():
    random_number = random.randint(1000, 9999)
    timestamp = int(time.time()) % 100000
    return f"ori{random_number}{timestamp}.peles@gmail.com"



