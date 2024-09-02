import pandas as pd
import random
import hashlib

# Define the size of each chunk to be processed
chunk_size = 10000
input_file = "input.csv"

# Function to anonymize a value using SHA-256 hashing
def anonymize_value(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

# Function to randomize the characters in a value
def randomize_value(value):
    value_list = list(value)  
    random.shuffle(value_list)
    return ''.join(value_list)


df_chunks = []
iteration = 0
header = True

# Process the CSV file in chunks
for df_chunk in pd.read_csv(input_file, chunksize=chunk_size):        
    df_chunk['first_name'] = df_chunk['first_name'].apply(randomize_value)
    df_chunk['last_name'] = df_chunk['last_name'].apply(randomize_value)
    df_chunk['address'] = df_chunk['address'].apply(anonymize_value)
    
    # To ensure the header is not written again
    if iteration > 0:
        header = False

    # Increment the iteration counter
    iteration = iteration + 1         
    df_chunk.to_csv('output.csv', mode='a', index=False, header=header)