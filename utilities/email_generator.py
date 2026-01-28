import random
import time
from pathlib import Path

DATA_FILE = Path("data/user_data.json")
def generate_unique_email():
    random_number = random.randint(1000, 9999)
    timestamp = int(time.time()) % 100000
    return f"ori{random_number}{timestamp}.peles@gmail.com"



