import csv
import os
import random
import uuid

from faker import Faker

# Initialize Faker
fake = Faker()

# Generate random values
name = fake.name()
age = random.randint(1, 100)

source_dir = 'data/source'
os.makedirs(source_dir, exist_ok=True)

# Generate a unique random file name
filename = f"{source_dir}/data_{uuid.uuid4().hex}.csv"

# Write to CSV
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])  # header
    writer.writerow([name, age])      # single record

print(f"CSV file '{filename}' created with values: name={name}, age={age}")