import random
import time

def generate_unique_email(prefix: str = "testuser") -> str:
    random_number = random.randint(1000, 9999)
    timestamp = int(time.time()) % 100000
    return f"{prefix}{random_number}{timestamp}@gmail.com"



